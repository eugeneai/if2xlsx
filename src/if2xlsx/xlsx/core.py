from zipfile import ZipFile
#from abc import ABC, abstractmethod
from lxml import etree
from collections import OrderedDict
import os.path

NS = {
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}


class LazyLoader(object):
    """Base cless for lazy loading structures from a stream"""

    __filename__ = None

    def __init__(self, stream=None, mode='r', filename=None):
        """Initialize and open file of Excel Document"""
        if not isinstance(stream, ZipFile):
            stream = ZipFile(stream, mode=mode)
        self.stream = stream
        if filename is None:
            filename = self.__class__.__filename__
        self.filename = filename
        self.xml = None
        self.loaded = False
        self.ids = OrderedDict()
        self.struct()

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
    """Object holding document ptoperties
    """

    def register_property(self, name, filename):
        obj = DocumentProperties(self.stream, filename=filename)
        setattr(self, name, obj)
        return obj


class Rels(LazyLoader):
    """Loader for _rels/.rels-file of a XLSX file

    """
    __filename__ = '_rels/.rels'

    def register_attrs(self, target):
        self.load()
        for node in self.xpath("/rel:Relationships/rel:Relationship"):
            a = node.attrib
            id = a['Id']
            t = a['Type']
            filename = a['Target']
            props = DocumentProperties(self.stream)

            if t.endswith("-properties"):
                _, propfile = os.path.split(filename)
                name, ext = os.path.splitext(propfile)
                obj = props.register_property(name, filename)

            elif t.endswith("officeDocument"):
                name, _ = os.path.split(filename)
                obj = OfficeDocument(self.stream, filename=filename)
                setattr(target, name, obj)

            self.ids[id] = obj


class Document(LazyLoader):
    """An Excel document, either loaded or generated from
    a scratch file.
    """

    def struct(self):
        """Lazy load structures into memory"""
        self.rels = Rels(self.stream)

    def load(self):
        self.rels.register_attrs(self)


class OfficeDocument(LazyLoader):
    """Defines list of workbooks
    """
