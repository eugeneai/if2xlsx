from if2xlsx.interfaces import IEditable, IClonable, ICell, IColumn, IRow, IWorkSheet, IDocument, IWorkSheets
from zope.component import adapter
from zope.interface import implementer

from if2xlsx.xlsx import OfficeDocument, WorkSheets, WorkSheet, Document
import os.path


@adapter(OfficeDocument)
@implementer(IDocument)
class OfficeDocumentToIDocumentAdapter(object):
    def __init__(self, context):
        self.context = context

    @property
    def ws(self):
        return IWorkSheets(self.context.ws)


@adapter(Document)
@implementer(IDocument)
class DocumentToIDocumentAdapter(object):
    def __init__(self, context):
        self.context = context
        context.load()
        self.xl = context.xl  # NOTE: Suppose that xl will always be OfficeDocument

    @property
    def ws(self):
        self.xl.load()        # NOTE: This might happened in constructor.
        return IWorkSheets(self.xl.ws)


@adapter(WorkSheets)
@implementer(IWorkSheets)
class WorkSheetsToIWorkSheetsAdapter(object):
    def __init__(self, context):
        self.context = context

    def __getitem__(self, index):
        return IWorkSheet(self.context[index])

    def __len__(self):
        return len(self.context)


@adapter(WorkSheet)
@implementer(IWorkSheet)
class WorkSheetToIWorkSheetAdapter(object):
    def __init__(self, context):
        self.context = context

    @property
    def name(self):
        filename = self.context.filename
        nameext = os.path.split(filename)[-1]
        name, ext = os.path.splitext(nameext)
        return name


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
