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
        self._stream = stream
        if filename is None:
            filename = self.__class__.__filename__
        self._filename = filename
        self._xml = None
        self._def_structs()

    def _def_structs(self):
        """Define object structures reflecting
        XLSX file structures"""

    def load(self):
        """Lazy load structures into memory.
        By default load it as XML,
        supposing filename field to exist"""
        if self._filename:
            self._xml = self.load_xml(self._filename)

    def open(self, name, mode='r'):
        """Helper function for initiating file streams
        by names."""
        return self._stream.open(name=name, mode=mode, force_zip64=True)

    def load_xml(self, name):
        """Read ZipFile File as lxml etree XML"""
        i = self.open(name)
        self._xml = etree.parse(i)
        return self._xml

    @property
    def xml(self):
        return self._xml


class Rels(LazyLoader):
    """Loader for _rels/.rels-file of a XLSX file

    """
    __filename__ = '_rels/.rels'


class Document(LazyLoader):
    """An Excel document, either loaded or generated from
    a scratch file.
    """

    def _def_structs(self):
        """Lazy load structures into memory"""
        self.rels = Rels(self._stream)
        self.rels.load()
