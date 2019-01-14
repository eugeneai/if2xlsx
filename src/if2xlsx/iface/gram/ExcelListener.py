# Generated from Excel.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExcelParser import ExcelParser
else:
    from ExcelParser import ExcelParser

# This class defines a complete listener for a parse tree produced by ExcelParser.
class ExcelListener(ParseTreeListener):

    # Enter a parse tree produced by ExcelParser#chunk.
    def enterChunk(self, ctx:ExcelParser.ChunkContext):
        pass

    # Exit a parse tree produced by ExcelParser#chunk.
    def exitChunk(self, ctx:ExcelParser.ChunkContext):
        pass


    # Enter a parse tree produced by ExcelParser#explist.
    def enterExplist(self, ctx:ExcelParser.ExplistContext):
        pass

    # Exit a parse tree produced by ExcelParser#explist.
    def exitExplist(self, ctx:ExcelParser.ExplistContext):
        pass


    # Enter a parse tree produced by ExcelParser#exp.
    def enterExp(self, ctx:ExcelParser.ExpContext):
        pass

    # Exit a parse tree produced by ExcelParser#exp.
    def exitExp(self, ctx:ExcelParser.ExpContext):
        pass


    # Enter a parse tree produced by ExcelParser#funcCall.
    def enterFuncCall(self, ctx:ExcelParser.FuncCallContext):
        pass

    # Exit a parse tree produced by ExcelParser#funcCall.
    def exitFuncCall(self, ctx:ExcelParser.FuncCallContext):
        pass


    # Enter a parse tree produced by ExcelParser#selector.
    def enterSelector(self, ctx:ExcelParser.SelectorContext):
        pass

    # Exit a parse tree produced by ExcelParser#selector.
    def exitSelector(self, ctx:ExcelParser.SelectorContext):
        pass


    # Enter a parse tree produced by ExcelParser#sheetname.
    def enterSheetname(self, ctx:ExcelParser.SheetnameContext):
        pass

    # Exit a parse tree produced by ExcelParser#sheetname.
    def exitSheetname(self, ctx:ExcelParser.SheetnameContext):
        pass


    # Enter a parse tree produced by ExcelParser#localSel.
    def enterLocalSel(self, ctx:ExcelParser.LocalSelContext):
        pass

    # Exit a parse tree produced by ExcelParser#localSel.
    def exitLocalSel(self, ctx:ExcelParser.LocalSelContext):
        pass


    # Enter a parse tree produced by ExcelParser#selList.
    def enterSelList(self, ctx:ExcelParser.SelListContext):
        pass

    # Exit a parse tree produced by ExcelParser#selList.
    def exitSelList(self, ctx:ExcelParser.SelListContext):
        pass


    # Enter a parse tree produced by ExcelParser#xlTable.
    def enterXlTable(self, ctx:ExcelParser.XlTableContext):
        pass

    # Exit a parse tree produced by ExcelParser#xlTable.
    def exitXlTable(self, ctx:ExcelParser.XlTableContext):
        pass


    # Enter a parse tree produced by ExcelParser#operatorOr.
    def enterOperatorOr(self, ctx:ExcelParser.OperatorOrContext):
        pass

    # Exit a parse tree produced by ExcelParser#operatorOr.
    def exitOperatorOr(self, ctx:ExcelParser.OperatorOrContext):
        pass


    # Enter a parse tree produced by ExcelParser#operatorAnd.
    def enterOperatorAnd(self, ctx:ExcelParser.OperatorAndContext):
        pass

    # Exit a parse tree produced by ExcelParser#operatorAnd.
    def exitOperatorAnd(self, ctx:ExcelParser.OperatorAndContext):
        pass


    # Enter a parse tree produced by ExcelParser#operatorComparison.
    def enterOperatorComparison(self, ctx:ExcelParser.OperatorComparisonContext):
        pass

    # Exit a parse tree produced by ExcelParser#operatorComparison.
    def exitOperatorComparison(self, ctx:ExcelParser.OperatorComparisonContext):
        pass


    # Enter a parse tree produced by ExcelParser#operatorAddSub.
    def enterOperatorAddSub(self, ctx:ExcelParser.OperatorAddSubContext):
        pass

    # Exit a parse tree produced by ExcelParser#operatorAddSub.
    def exitOperatorAddSub(self, ctx:ExcelParser.OperatorAddSubContext):
        pass


    # Enter a parse tree produced by ExcelParser#operatorMulDivMod.
    def enterOperatorMulDivMod(self, ctx:ExcelParser.OperatorMulDivModContext):
        pass

    # Exit a parse tree produced by ExcelParser#operatorMulDivMod.
    def exitOperatorMulDivMod(self, ctx:ExcelParser.OperatorMulDivModContext):
        pass


    # Enter a parse tree produced by ExcelParser#operatorBitwise.
    def enterOperatorBitwise(self, ctx:ExcelParser.OperatorBitwiseContext):
        pass

    # Exit a parse tree produced by ExcelParser#operatorBitwise.
    def exitOperatorBitwise(self, ctx:ExcelParser.OperatorBitwiseContext):
        pass


    # Enter a parse tree produced by ExcelParser#operatorUnary.
    def enterOperatorUnary(self, ctx:ExcelParser.OperatorUnaryContext):
        pass

    # Exit a parse tree produced by ExcelParser#operatorUnary.
    def exitOperatorUnary(self, ctx:ExcelParser.OperatorUnaryContext):
        pass


    # Enter a parse tree produced by ExcelParser#operatorPower.
    def enterOperatorPower(self, ctx:ExcelParser.OperatorPowerContext):
        pass

    # Exit a parse tree produced by ExcelParser#operatorPower.
    def exitOperatorPower(self, ctx:ExcelParser.OperatorPowerContext):
        pass


    # Enter a parse tree produced by ExcelParser#number.
    def enterNumber(self, ctx:ExcelParser.NumberContext):
        pass

    # Exit a parse tree produced by ExcelParser#number.
    def exitNumber(self, ctx:ExcelParser.NumberContext):
        pass


    # Enter a parse tree produced by ExcelParser#string.
    def enterString(self, ctx:ExcelParser.StringContext):
        pass

    # Exit a parse tree produced by ExcelParser#string.
    def exitString(self, ctx:ExcelParser.StringContext):
        pass


