# Generated from Excel.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExcelParser import ExcelParser
else:
    from ExcelParser import ExcelParser

# This class defines a complete generic visitor for a parse tree produced by ExcelParser.

class ExcelVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExcelParser#chunk.
    def visitChunk(self, ctx:ExcelParser.ChunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#explist.
    def visitExplist(self, ctx:ExcelParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#extExp.
    def visitExtExp(self, ctx:ExcelParser.ExtExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#exp.
    def visitExp(self, ctx:ExcelParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#funcCall.
    def visitFuncCall(self, ctx:ExcelParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#selector.
    def visitSelector(self, ctx:ExcelParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#sheetname.
    def visitSheetname(self, ctx:ExcelParser.SheetnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#localSel.
    def visitLocalSel(self, ctx:ExcelParser.LocalSelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#selectorList.
    def visitSelectorList(self, ctx:ExcelParser.SelectorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#oneCell.
    def visitOneCell(self, ctx:ExcelParser.OneCellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#xlTable.
    def visitXlTable(self, ctx:ExcelParser.XlTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#operatorOr.
    def visitOperatorOr(self, ctx:ExcelParser.OperatorOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#operatorAnd.
    def visitOperatorAnd(self, ctx:ExcelParser.OperatorAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#operatorComparison.
    def visitOperatorComparison(self, ctx:ExcelParser.OperatorComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#operatorAddSub.
    def visitOperatorAddSub(self, ctx:ExcelParser.OperatorAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#operatorMulDivMod.
    def visitOperatorMulDivMod(self, ctx:ExcelParser.OperatorMulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#operatorBitwise.
    def visitOperatorBitwise(self, ctx:ExcelParser.OperatorBitwiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#operatorUnary.
    def visitOperatorUnary(self, ctx:ExcelParser.OperatorUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#operatorPower.
    def visitOperatorPower(self, ctx:ExcelParser.OperatorPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#number.
    def visitNumber(self, ctx:ExcelParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExcelParser#string.
    def visitString(self, ctx:ExcelParser.StringContext):
        return self.visitChildren(ctx)



del ExcelParser