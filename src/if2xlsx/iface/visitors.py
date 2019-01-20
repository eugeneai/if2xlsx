from .gram.ExcelVisitor import ExcelVisitor
from .gram.ExcelParser import ExcelParser


class SheetResolveVisitor(ExcelVisitor):
    def __init__(self, doc):
        self.doc = doc
        self.restore_sheet()

    def restore_sheet(self):
        self.sheet = None

    def visitSheetname(self, ctx: ExcelParser.SheetnameContext):
        super().visitSheetname(ctx)
        sel = ctx.SHEETNAME()
        sel = sel.getText().rstrip('!').strip()
        self.sheet = self.doc.ws[sel]


class CellResolveVisitor(SheetResolveVisitor):
    def visittree(self, ctx):
        super().visit(ctx)
        self.restore_sheet()

    def select_cell(self, sel):
        if self.sheet is not None:
            return self.sheet[sel.getText()]
        else:
            raise ValueError('wrong selection expression')

    def resolve_cell(self, sel, ctx):
        cellref = self.select_cell(sel)
        ctx.cellref = cellref

    def visitLocalSel(self, ctx: ExcelParser.LocalSelContext):
        super().visitLocalSel(ctx)
        sel = None

        sel = ctx.ASELECTOR()
        if sel is not None:
            return self.resolve_cell(sel, ctx)
        sel = ctx.RCSELECTOR()
        if sel is not None:
            return self.resolve_cell(sel, ctx)
        sel = ctx.NAME()
        if sel is not None:
            return self.resolve_cell(sel, ctx)
        sel = ctx.INT()
        if sel is not None:
            return self.resolve_cell(sel, ctx)


class SimpleCellCollector(SheetResolveVisitor):
    def __init__(self, doc):
        super().__init__(doc)
        self.cellref = None
        self.cellrange = None
        self.celllist = None

    def visitLocalSel(self, ctx):
        super().visitLocalSel(ctx)
        self.cellref = ctx.cellref

    def visitSelector(self, ctx):
        # super().visitSelector(ctx)
        if ctx.xlTable() is not None:
            self.visit(ctx.xlTable())
        if ctx.sheetname() is not None:
            self.visit(ctx.sheetname())
        locals = list(ctx.localSel())
        self.visit(locals[0])
        left = self.cellref
        if locals[1] is not None:
            self.visit(locals[1])
            right = self.cellref
            self.cellrange = (left, right)
        else:
            self.cellrange = left

    def visitExplist(self, ctx):
        #n = ctx.getChildCount()
        par = self.celllist
        self.celllist = []
        for exp in ctx.exp():
            self.visit(exp)
            self.celllist.append(self.cellrange)
        if par is not None:
            par.append(self.celllist)
            self.celllist = par
        print("LIST:", self.celllist)
