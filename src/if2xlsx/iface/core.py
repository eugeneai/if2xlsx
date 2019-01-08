from if2xlsx.interfaces import IEditable, IClonable, ICell, IColumn, IRow, IWorkSheet, IDocument, IWorkSheets
from zope.component import adapter
from zope.interface import implementer

from if2xlsx.xlsx import OfficeDocument, WorkSheets, WorkSheet, Document
import os.path
import if2xlsx.xlsx.tools as tools


@adapter(OfficeDocument)
@implementer(IDocument)
class OfficeDocumentToIDocumentAdapter(object):
    def __init__(self, context):
        self.context = context
        self._ws = None

    @property
    def ws(self):
        if self._ws is None:
            self.context.load()
            self._ws = answer = IWorkSheets(self.context.ws)
            answer.doc = self
        else:
            answer = self._ws
        return answer

    def __getitem__(self, what):
        """Return a selection described by what,
        e.g. Sheet1!$A$1:$B$1"""
        # Check what to contain a '<WorkSheet name>!' part

        parts = what.split('!', 1)
        if len(parts) != 2:
            raise KeyError(
                "argument does not contain '<WorkSheet name>!' part "
                "or it is a wrong expression")

        sheet, selection = parts

        sheet = self.ws[sheet]
        return sheet[selection]


@adapter(Document)
@implementer(IDocument)
class DocumentToIDocumentAdapter(object):
    def __init__(self, context):
        self.context = context
        context.load()
        self.xl = context.xl  # NOTE: Suppose that xl will always be OfficeDocument
        self.doc = IDocument(self.xl)

    @property
    def ws(self):
        return self.doc.ws

    def __getitem__(self, what):
        return self.doc[what]


@adapter(WorkSheets)
@implementer(IWorkSheets)
class WorkSheetsToIWorkSheetsAdapter(object):
    def __init__(self, context):
        self.context = context
        self.doc = None  # it is set by caller

    def __getitem__(self, index):
        try:
            # Return a WorkSheet by name
            ws = self.context.root.root.xldoc.get_sheet(index)
        except KeyError:
            ws = self.context[index]

        aws = IWorkSheet(ws)
        aws.doc = self.doc

        return(aws)

    def __len__(self):
        return len(self.context)


@adapter(WorkSheet)
@implementer(IWorkSheet)
class WorkSheetToIWorkSheetAdapter(object):
    def __init__(self, context):
        self.context = context
        self.doc = None  # Set by caller

    @property
    def name(self):
        ctx = self.context
        st = ctx.state
        if st.name is not None:
            return st.name
        return tools.name(ctx.filename)

    @name.setter
    def name(self, value):
        # FIXME: We can rename table only onece
        ctx = self.context
        ctx.load()
        ctx.state.name = value
        old_fn = ctx.filename
        ctx.filename = tools.renamed(old_fn, value)
        ctx.xldoc.tablename_changed(old_fn, value)

    def __getitem__(self, what):
        """Get Excel rows, columns, cells according to `what` argument."""

        # Check if it contains absolute '<WorkSheet name>!' part

        parts = what.split('!', 1)
        if len(parts) == 2:
            return self.doc[what]
        print(what)


ADAPTER_REGISTERED = False


def register_adapters():
    global ADAPTER_REGISTERED

    if ADAPTER_REGISTERED:
        return

    from zope.component import getSiteManager

    GSM = getSiteManager()

    for a in [WorkSheetsToIWorkSheetsAdapter,
              OfficeDocumentToIDocumentAdapter,
              DocumentToIDocumentAdapter,
              WorkSheetToIWorkSheetAdapter,
              ]:
        GSM.registerAdapter(a)

    ADAPTER_REGISTERED = True


register_adapters()
