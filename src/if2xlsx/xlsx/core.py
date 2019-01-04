from zipfile import ZipFile
#from abc import ABC, abstractmethod
from lxml import etree


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
        self._def_structs()

    def _def_structs(self):
        """Define object structures reflecting
        XLSX file structures"""

    def load(self):
        """Lazy load structures into memory.
        By default load it as XML,
        supposing filename field to exist"""
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


class Rels(LazyLoader):
    """Loader for _rels/.rels-file of a XLSX file

    """
    __filename__ = '_rels/.rels'


class Document(LazyLoader):
    """An Excel document, either loaded or generated from
    a scratch file.
    """

    def load(self):
        """Lazy load structures into memory"""
        self.rels = Rels(self.stream)
        self.rels.load()
