from nose.plugins.skip import SkipTest
from nose.tools import assert_raises, nottest
import os.path
from zipfile import ZipFile

from if2xlsx import Document
from if2xlsx.interfaces import IDocument
from if2xlsx.iface import register_adapters

INPUT_DIR = os.path.abspath(
    os.path.join(os.path.split(__file__)[0],
                 '..', 'input'))

TEST_FILE = os.path.join(INPUT_DIR, "book.xlsx")

# register_adapters()

# @SkipTest


class TestBasic:

    def setUp(self):
        self.xl = Document(TEST_FILE)
        self.xl.load()

    def test_zip_open(self):
        assert isinstance(self.xl.stream, ZipFile)

    def test_loading_by_force(self):
        assert self.xl.rels.xml is not None

    def test_xl(self):
        assert hasattr(self.xl, 'xl')
        assert self.xl.xl is not None

    def test_pretty(self):
        self.xl.xl.load()
        # assert self.xl.xl.rels.pretty() is not None

    def test_ws_indexing(self):
        self.xl.xl.load()
        self.xl.xl.ws[0]
        w = self.xl.xl.ws['sheet1']
        w.load()
        # w.pretty()

    def tearDown(self):
        pass


class TestInterface:

    def setUp(self):
        self.xldoc = Document(TEST_FILE)
        self.doc = IDocument(self.xldoc)

    def test_document_interface(self):
        assert IDocument.providedBy(self.doc)

    def test_wb_name(self):
        assert len(self.doc.ws) == 3
        wb1 = self.doc.ws['sheet1']
        wb2 = self.doc.ws[0]
        # print(wb1.name, wb2.name)
        # assert wb1.name == wb2.name
