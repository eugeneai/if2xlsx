from if2xlsx.interfaces import IEditable, IClonable, ICell, IColumn, IRow, IWorkSheet, IDocument, IWorkSheets
from zope.component import adapter
from zope.interface import implementer

from if2xlsx.xlsx import OfficeDocument, WorkSheets, WorkSheet, Document


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
        return IWorkSheets(self.xl.ws)


@adapter(WorkSheets)
@implementer(IWorkSheets)
class WorkSheetsToIWorkSheetsAdapter(object):
    def __init__(self, context):
        self.context = context

    def __getitem__(self, index):
        return self.context[index]


ADAPTER_REGISTERED = False


def register_adapters():
    global ADAPTER_REGISTERED

    if ADAPTER_REGISTERED:
        return

    from zope.component import getSiteManager

    GSM = getSiteManager()

    for a in [WorkSheetsToIWorkSheetsAdapter,
              OfficeDocumentToIDocumentAdapter,
              DocumentToIDocumentAdapter]:
        GSM.registerAdapter(a)

    ADAPTER_REGISTERED = True


register_adapters()
