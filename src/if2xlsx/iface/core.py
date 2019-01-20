from if2xlsx.interfaces import IEditable, IClonable, ICell, IColumn, IRow
from if2xlsx.interfaces import IWorkSheet, IDocument, IWorkSheets, IDefMapping
from zope.component import adapter, getAdapter
from zope.interface import implementer

from if2xlsx.xlsx import OfficeDocument, WorkSheets, WorkSheet, Document
import os.path
import if2xlsx.xlsx.tools as tools
from collections import OrderedDict

from if2xlsx.iface.grammar import parser
from if2xlsx.xlsx.core import NS
from .visitors import CellResolveVisitor, SimpleCellCollector
import re


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

    @property
    def defines(self):
        return IDefMapping(self.context.names)

    @property
    def parsed_defines(self):
        return getAdapter(self.context.names, IDefMapping, name='parsed')

    def print_ast(self, tree):
        p = tree.parser
        print("AST:", tree.toStringTree(recog=p))

    def intasrefs(self, tree):
        visitor = CellResolveVisitor(self)
        visitor.visit(tree)
        v2 = SimpleCellCollector(self)
        v2.visit(tree)
        return tree


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

    @property
    def defines(self):
        return self.doc.defines

    @property
    def parsed_defines(self):
        return self.doc.parsed_defines

    def intasrefs(self, exp):
        return self.doc.intasrefs(exp)

    def print_ast(self, tree):
        return self.doc.print_ast(tree)


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


RE_ROW = re.compile(r'([$]?)([0-9]+)')


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
        self.context.load()

        parts = what.split('!', 1)
        if len(parts) == 2:
            return self.doc[what]

        addr = what
        answer = None
        m = RE_ROW.match(addr)

        if m is not None:
            absolute = m.group(1) == "$"
            ref = m.group(2)
            row = self.context.select_row(ref, absolute)
            if row is None:
                raise IndexError('wrong row index expression')
            answer = IRow(self)
            answer.row = row
            answer.count = int(ref)

        return answer


@implementer(IDefMapping)
@adapter(dict)
# @adapter(OrderedDict)
class DefMapping(object):

    def __init__(self, dict):
        self.dict = dict

    def __getitem__(self, name):
        val = self.dict[name]
        return val.text

    def __len__(self):
        return len(self.dict)


class ParsedDefMapping(DefMapping):

    def __getitem__(self, name):
        node = self.dict[name]
        t = node.text
        p = parser(t)
        # return t, p.explist().toStringTree(recog=p)

        tree = p.explist()
        tree.parser = p
        return tree


RE_CELL = re.compile(r'([$]?)([A-Z]*)([$]?)([0-9]*)')


@adapter(IWorkSheet)
@implementer(IRow)
class IWorkSheetToIRowAdapter(object):
    def __init__(self, ws):
        self.context = ws
        self.ws = self.context.context
        self.row = None

    def index(self):
        return int(self.row.attrib["r"])

    def __len__(self):
        start, stop = self.spans
        return stop-start+1

    def span(self):
        spans = self.row.attrib('spans').split(':')
        spans = map(int, spans)
        return spans

    def __getitem__(self, index):
        """Returns a cell object by index.
        If `index` is int, then return just i-th child of XML tree (0-based),
        If `index` is string representation of int, then return
                   i-th child (1-based),
        If `index` if of form like 'AB210', then find cell by its reference.
        """

        if type(index) == int:
            cell = ICell(self.context)
            cell.cell = self.row[index]
            return cell
        m = RE_CELL.match(index)
        if m:
            b1, l, b2, n = m.groups()
            if b1 or b2:
                raise IndexError('supposed index without $''s')
            if not l and n:
                n = int(n)
                return self[n-1]
            if l and not n:
                n = self.index
            addr = l+str(n)
            query = './main:c[@r="{}"]'.format(addr)
            c = self.row.xpath(query, namespaces=NS)[0]
            cell = ICell(self.context)
            cell.cell = c
            return cell
        else:
            raise IndexError('wrong index')


@adapter(IWorkSheet)
@implementer(ICell)
class IWorkSheetToICellAdapter(object):
    """Documentation for IWorkSheetToICellAdapter

    """

    def __init__(self, ws):
        super(IWorkSheetToICellAdapter, self).__init__()
        self.context = ws
        self.ws = self.context.context
        self.cell = None

    @property
    def index(self):
        attrs = self.cell.attrib
        return attrs['r']


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
              DefMapping,
              (ParsedDefMapping, 'parsed'),
              IWorkSheetToIRowAdapter,
              IWorkSheetToICellAdapter,
              ]:
        if type(a) == tuple:
            a, name = a
            GSM.registerAdapter(a, name=name)
        else:
            GSM.registerAdapter(a)

    ADAPTER_REGISTERED = True


register_adapters()
