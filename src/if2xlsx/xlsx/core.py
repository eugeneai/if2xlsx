from zipfile import ZipFile, ZIP_DEFLATED
#from abc import ABC, abstractmethod
from lxml import etree
from collections import OrderedDict, namedtuple
import os.path
from itertools import cycle
import tempfile
import if2xlsx.xlsx.tools as tools

NS = {
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
    "type": "http://schemas.openxmlformats.org/package/2006/content-types"
}

ZIP_COMPRESSION_LEVEL = 5


class Root(object):
    """Associates the root node of ZipFile structure with
    a ZipFile itself."""

    def __init__(self, root, stream):
        self.root = root
        self.stream = stream


class LazyLoader(object):
    """Base cless for lazy loading structures from a stream"""

    __filename__ = None

    def __init__(self, root=None, filename=None, mode='r'):
        """Initialize and open file of Excel Document"""
        if not isinstance(root, Root):
            raise ValueError('first parameter must be instance of Root')
        self.root = root
        if filename is None:
            filename = self.__class__.__filename__
        self.filename = filename
        self.xml = None
        self.ids = OrderedDict()
        self.struct()

    @property
    def xldoc(self):
        return self.root.root.xl

    @property
    def state(self):
        return self.root.root.zipparts[self.filename]

    @property
    def changed(self):
        return self.state.changed

    @changed.setter
    def changed(self, value):
        s = self.state
        assert s.obj == self
        s.changed = value

    def invalidate(self):
        self.changed = True

    @property
    def stream(self):
        return self.root.stream

    def struct(self):
        """Define object structures reflecting
        XLSX file structures"""

    def load(self):
        """Lazy load structures into memory.
        By default load it as XML,
        supposing filename field to exist"""
        if self.state.loaded:
            return
        if self.filename is not None:
            self._register_at_root()
            self.xml = self.load_xml(self.filename)
            self.state.loaded = True

    def _register_at_root(self):
        """Registers itself as ZipFile content negotiator."""
        s = self.state.register(self)

    def open(self, name, mode='r'):
        """Helper function for initiating file streams
        by names."""
        return self.stream.open(name=name, mode=mode, force_zip64=True)

    def load_xml(self, name):
        """Read ZipFile File as lxml etree XML"""
        i = self.open(name)
        self.xml = etree.parse(i)
        return self.xml

    def content(self):
        """Return the content as a part of ZipFile, bytes.
        By default just serialize XML"""
        if self.xml is not None:
            return etree.tostring(
                self.xml,
                encoding='utf-8',
                xml_declaration=True,
                inclusive_ns_prefixes=True)

    def pretty(self, noprint=False):
        answer = etree.tostring(self.xml, encoding=str, pretty_print=True)
        if not noprint:
            print(answer)
        return answer

    def xpath(self, query):
        return self.xml.xpath(query, namespaces=NS)


class ContentType(LazyLoader):
    """ContentType reflects [Content_Types].xml
    """

    def __init__(self, root, filename='[Content_Types].xml'):
        super(ContentType, self).__init__(root=root, filename=filename)
        self.ovr = OrderedDict()

    def register_overrides(self):
        self.load()
        for node in self.xpath("/type:Types/type:Override"):
            filename = node.attrib["PartName"]
            self.ovr[filename] = node

    def tablename_changed(self, filename, name):
        ofn = "/"+filename
        node = self.ovr[ofn]
        new_name = tools.renamed(node.attrib["PartName"], name)
        del self.ovr[ofn]
        node.attrib["PartName"] = new_name
        self.ovr[new_name] = node
        self.invalidate()


class DocumentProperties(LazyLoader):
    """Object holding document properties
    """

    def register_property(self, name, filename):
        obj = DocumentProperties(self.root, filename=filename)
        setattr(self, name, obj)
        return obj


class Rels(LazyLoader):
    """Loader for _rels/.rels-file of a XLSX file

    """

    def register_attrs(self, target):
        self.load()

    def relations(self):
        for node in self.xpath("/rel:Relationships/rel:Relationship"):
            a = node.attrib
            id = a['Id']
            type = a['Type']
            target = a['Target']
            yield Relationship(id=id, type=type, target=target, element=node)


class Relationship(object):
    """Saves relationship data
    """

    def __init__(self, id, type, target, element, obj=None):
        self.id = id
        self.type = type
        self.target = target
        self.element = element
        self.obj = obj


class DocumentRels(Rels):

    __filename__ = '_rels/.rels'

    def register_attrs(self, target):
        super(DocumentRels, self).register_attrs(target)

        props = DocumentProperties(self.root)
        setattr(target, 'props', props)

        for rel in self.relations():
            t = rel.type
            filename = rel.target
            if t.endswith("-properties"):
                _, propfile = os.path.split(filename)
                name, ext = os.path.splitext(propfile)
                obj = props.register_property(name, filename)

            elif t.endswith("officeDocument"):
                name, _ = os.path.split(filename)
                obj = OfficeDocument(self.root, filename=filename)
                setattr(target, name, obj)

            rel.obj = obj
            self.ids[rel.id] = rel


class DirRels(Rels):
    def __init__(self, root, relative_to):
        pfilename = relative_to.filename
        name = os.path.split(pfilename)[0]
        filename = os.path.join(
            name,
            self.__class__.__filename__,
        )
        super(DirRels, self).__init__(root=root, filename=filename)


class XlRels(DirRels):

    __filename__ = "_rels/workbook.xml.rels"

    def register_attrs(self, target):
        super(DirRels, self).register_attrs(target)
        ws = WorkSheets()
        setattr(target, 'worksheets', ws)
        for rel in self.relations():
            t = os.path.split(rel.type)[-1]
            if t == "worksheet":
                obj = WorkSheet(
                    self.root, filename=rel.target, document=target)
                ws.add(obj)
            elif t == "sharedStrings":
                obj = SharedStrings(self.root, filename=rel.target)
                setattr(target, 'sharedStrings', obj)

            # TODO: calcChain, styles, theme
            rel.obj = obj
            self.ids[rel.id] = rel

    def tablename_changed(self, filename, name):
        for k, rel in self.ids.items():
            if filename.endswith(rel.target):  # FIXME: Bad supposition
                break
        else:
            raise ValueError('object not found')

        rel.element.attrib['Target'] = tools.renamed(rel.target, name)
        self.invalidate()


class WsRels(DirRels):

    __filename__ = "_rels/*"


class WorkSheet(LazyLoader):
    """Defines Worksheet"""

    def __init__(self, root, filename, document):
        dfilename = document.filename
        name = os.path.split(dfilename)[0]
        filename = os.path.join(name, filename)
        super(WorkSheet, self).__init__(root=root, filename=filename)
        self.document = document


class WorkSheets(OrderedDict):
    """Worksheet list"""

    def __init__(self, *args, **kw):
        super(WorkSheets, self).__init__(*args, **kw)
        self.counter = 0

    def add(self, sheet):
        nameext = os.path.split(sheet.filename)[-1]
        name, ext = os.path.splitext(nameext)
        self[name] = sheet
        self[self.counter] = sheet
        # print(self.counter, name)
        self.counter += 1
        return sheet

    def __len__(self):
        return super(WorkSheets, self).__len__() >> 1


class SharedStrings(OrderedDict, LazyLoader):
    """Shared strings holder"""

    def __init__(self, root, filename):
        OrderedDict.__init__(self)
        LazyLoader.__init__(self, root=root, filename=filename)


class OfficeDocument(LazyLoader):
    """Defines list of workbooks
    """

    def struct(self):
        self.rels = XlRels(self.root, relative_to=self)

    def load(self):
        super(OfficeDocument, self).load()
        self.rels.register_attrs(self)

    @property
    def ws(self):
        return self.worksheets

    def tablename_changed(self, filename, name):
        self.rels.tablename_changed(filename, name)
        self.root.root.contentType.tablename_changed(filename, name)
        root = self.root.root
        zpp = root.zipparts
        new_fn = tools.renamed(filename, name)
        fs = zpp[filename]
        assert (fs.obj is not None)
        del zpp[filename]
        zpp[new_fn] = fs
        fs.changed = True


FileState = namedtuple("FileState",
                       ['name', 'obj', 'loaded', 'changed', 'deleted'])


class FileState(object):
    """Defines some flags for ZipExtFile parts state.
    """

    def __init__(self,
                 filename,
                 name=None,
                 obj=None,
                 loaded=False,
                 changed=False,
                 deleted=False):
        self.filename = filename
        self.name = name
        self.obj = obj
        self.loaded = loaded
        self.changed = changed
        self.deleted = deleted

    def register(self, obj):
        assert obj.filename == self.filename
        self.obj = obj


class Document(LazyLoader):
    """An Excel File, either loaded or generated from
    a scratch file.
    """

    def __init__(self, stream=None, filename=None, mode='r'):
        if not isinstance(stream, ZipFile):
            if stream is not None:
                stream = ZipFile(stream, mode=mode)
            else:
                RuntimeError('scratch is not implemented')
                # TODO: Implement scratch

        root = Root(self, stream)

        super(Document, self).__init__(root=root, filename=filename, mode=mode)

        zpp = self.zipparts = {}
        for filename in stream.namelist():
            zpp[filename] = FileState(filename, None,
                                      None, False, False, False)
        # print(self.zipparts)

    def struct(self):
        """Lazy load structures into memory"""
        self.rels = DocumentRels(self.root)
        self.contentType = ContentType(self.root)

    def load(self):
        self.rels.register_attrs(self)
        self.contentType.register_overrides()

    def save(self, filename):
        """Save ZipFile as Excel file copy with content changed."""
        o = ZipFile(
            filename,
            mode='w',
            compression=ZIP_DEFLATED,
            compresslevel=ZIP_COMPRESSION_LEVEL)
        i = self.root.stream
        zpp = self.zipparts
        for comp_name in zpp.keys():
            content = None
            zc = zpp[comp_name]
            open_name = comp_name
            if zc.deleted:
                # Skip adding this file to the target Excel file
                continue
            if zc.name is not None:
                # Name of file is changing
                open_name = tools.renamed(open_name, zc.name)
            if zc.changed:
                content = zc.obj.content()
                assert(comp_name == zc.obj.filename)
                cin = None
            else:
                cin = i.open(comp_name)
            cout = o.open(open_name, mode='w', force_zip64=True)
            if content is not None:
                cout.write(content)
            else:
                cout.write(cin.read())  # FIXME: Do it with finite size buffer
            cout.close()
            if cin is not None:
                cin.close()
        o.close()
