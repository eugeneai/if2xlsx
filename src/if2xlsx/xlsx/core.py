from zipfile import ZipFile, ZIP_DEFLATED
#from abc import ABC, abstractmethod
from lxml import etree
from collections import OrderedDict, namedtuple
import os.path
from itertools import cycle
import tempfile

NS = {
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
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
        self.loaded = False
        self.ids = OrderedDict()
        self.struct()

    @property
    def state(self):
        self.root.zipparts[self.filename]

    @property
    def changed(self):
        return self.state.changed

    @changed.setter
    def set_changed(self, value):
        self.state.changed = value

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
        if self.loaded:
            return
        if self.filename:
            self.xml = self.load_xml(self.filename)

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
            return etree.tostring(self.xml, encoding='utf-8', xml_declaration=True, inclusive_ns_prefixes=True)

    def pretty(self, noprint=False):
        answer = etree.tostring(self.xml,
                                encoding=str,
                                pretty_print=True)
        if not noprint:
            print(answer)
        return answer

    def xpath(self, query):
        return self.xml.xpath(query, namespaces=NS)


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
            yield Relationship(id=id, type=type, target=target)


Relationship = namedtuple('Relationship', ['id', 'type', 'target'])


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

            self.ids[rel.id] = obj


class DirRels(Rels):
    def __init__(self, root, relative_to):
        pfilename = relative_to.filename
        name = os.path.split(pfilename)[0]
        filename = os.path.join(name,
                                self.__class__.__filename__, )
        super(DirRels, self).__init__(root=root,
                                      filename=filename)


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
                obj = SharedStrings(self.root,
                                    filename=rel.target)
                setattr(target, 'sharedStrings', obj)

            # TODO: calcChain, styles, theme
            self.ids[rel.id] = obj


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

    def __init__(self,  root, filename):
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


FileState = namedtuple(
    "FileState", ['name', 'obj', 'loaded', 'changed', 'deleted'])


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

        self.zipparts = dict(zip(stream.namelist(), cycle(
            [FileState(None, None, False, False, False)])))
        # print(self.zipparts)

    def struct(self):
        """Lazy load structures into memory"""
        self.rels = DocumentRels(self.root)

    def load(self):
        self.rels.register_attrs(self)

    def save(self, filename):
        """Save ZipFile as Excel file copy with content changed."""
        o = ZipFile(filename, mode='w',
                    compression=ZIP_DEFLATED, compresslevel=ZIP_COMPRESSION_LEVEL)
        i = self.root.stream
        for comp_name in self.zipparts.keys():
            cin = i.open(comp_name)
            cout = o.open(comp_name, mode='w', force_zip64=True)
            cout.write(cin.read())  # FIXME: Do it with finite size buffer
            cout.close()
            cin.close()
        o.close()
