from zope.interface import Interface, Attribute


class IEditable(Interface):
    """Editable object"""


class IClonable(Interface):
    """An object that can be cloned"""


class ICell(Interface):
    """Cell interface"""


class IColumn(Interface):
    """Column interface"""


class IRow(Interface):
    """Row interface"""


class IWorkSheets(Interface):
    """List of worksheets"""

    def __getitem__(self, index):
        """Return index identified WorkSheet"""


class IWorkSheet(Interface):
    """A Workbook interface"""
    cells = Attribute("Matrix of cells")
    rows = Attribute("List of rows")
    columns = Attribute("List of columns")

    def __getitem__(index_or_slice):
        """Get a Cell or a Row or a Column or a Range"""


class IDocument(Interface):
    """A Spreadsheet document"""

    ws = Attribute("WorkSheets as an indexed object")

    def save(filename):
        """Save the Spreadsheet into a file"""
