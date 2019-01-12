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


    # Enter a parse tree produced by ExcelParser#funcname.
    def enterFuncname(self, ctx:ExcelParser.FuncnameContext):
        pass

    # Exit a parse tree produced by ExcelParser#funcname.
    def exitFuncname(self, ctx:ExcelParser.FuncnameContext):
        pass


    # Enter a parse tree produced by ExcelParser#varlist.
    def enterVarlist(self, ctx:ExcelParser.VarlistContext):
        pass

    # Exit a parse tree produced by ExcelParser#varlist.
    def exitVarlist(self, ctx:ExcelParser.VarlistContext):
        pass


    # Enter a parse tree produced by ExcelParser#namelist.
    def enterNamelist(self, ctx:ExcelParser.NamelistContext):
        pass

    # Exit a parse tree produced by ExcelParser#namelist.
    def exitNamelist(self, ctx:ExcelParser.NamelistContext):
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


    # Enter a parse tree produced by ExcelParser#prefixexp.
    def enterPrefixexp(self, ctx:ExcelParser.PrefixexpContext):
        pass

    # Exit a parse tree produced by ExcelParser#prefixexp.
    def exitPrefixexp(self, ctx:ExcelParser.PrefixexpContext):
        pass


    # Enter a parse tree produced by ExcelParser#functioncall.
    def enterFunctioncall(self, ctx:ExcelParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by ExcelParser#functioncall.
    def exitFunctioncall(self, ctx:ExcelParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by ExcelParser#varOrExp.
    def enterVarOrExp(self, ctx:ExcelParser.VarOrExpContext):
        pass

    # Exit a parse tree produced by ExcelParser#varOrExp.
    def exitVarOrExp(self, ctx:ExcelParser.VarOrExpContext):
        pass


    # Enter a parse tree produced by ExcelParser#var.
    def enterVar(self, ctx:ExcelParser.VarContext):
        pass

    # Exit a parse tree produced by ExcelParser#var.
    def exitVar(self, ctx:ExcelParser.VarContext):
        pass


    # Enter a parse tree produced by ExcelParser#varSuffix.
    def enterVarSuffix(self, ctx:ExcelParser.VarSuffixContext):
        pass

    # Exit a parse tree produced by ExcelParser#varSuffix.
    def exitVarSuffix(self, ctx:ExcelParser.VarSuffixContext):
        pass


    # Enter a parse tree produced by ExcelParser#nameAndArgs.
    def enterNameAndArgs(self, ctx:ExcelParser.NameAndArgsContext):
        pass

    # Exit a parse tree produced by ExcelParser#nameAndArgs.
    def exitNameAndArgs(self, ctx:ExcelParser.NameAndArgsContext):
        pass


    # Enter a parse tree produced by ExcelParser#selector.
    def enterSelector(self, ctx:ExcelParser.SelectorContext):
        pass

    # Exit a parse tree produced by ExcelParser#selector.
    def exitSelector(self, ctx:ExcelParser.SelectorContext):
        pass


    # Enter a parse tree produced by ExcelParser#rangedef.
    def enterRangedef(self, ctx:ExcelParser.RangedefContext):
        pass

    # Exit a parse tree produced by ExcelParser#rangedef.
    def exitRangedef(self, ctx:ExcelParser.RangedefContext):
        pass


    # Enter a parse tree produced by ExcelParser#rowSelector.
    def enterRowSelector(self, ctx:ExcelParser.RowSelectorContext):
        pass

    # Exit a parse tree produced by ExcelParser#rowSelector.
    def exitRowSelector(self, ctx:ExcelParser.RowSelectorContext):
        pass


    # Enter a parse tree produced by ExcelParser#colSelector.
    def enterColSelector(self, ctx:ExcelParser.ColSelectorContext):
        pass

    # Exit a parse tree produced by ExcelParser#colSelector.
    def exitColSelector(self, ctx:ExcelParser.ColSelectorContext):
        pass


    # Enter a parse tree produced by ExcelParser#cellSelector.
    def enterCellSelector(self, ctx:ExcelParser.CellSelectorContext):
        pass

    # Exit a parse tree produced by ExcelParser#cellSelector.
    def exitCellSelector(self, ctx:ExcelParser.CellSelectorContext):
        pass


    # Enter a parse tree produced by ExcelParser#args.
    def enterArgs(self, ctx:ExcelParser.ArgsContext):
        pass

    # Exit a parse tree produced by ExcelParser#args.
    def exitArgs(self, ctx:ExcelParser.ArgsContext):
        pass


    # Enter a parse tree produced by ExcelParser#parlist.
    def enterParlist(self, ctx:ExcelParser.ParlistContext):
        pass

    # Exit a parse tree produced by ExcelParser#parlist.
    def exitParlist(self, ctx:ExcelParser.ParlistContext):
        pass


    # Enter a parse tree produced by ExcelParser#tableconstructor.
    def enterTableconstructor(self, ctx:ExcelParser.TableconstructorContext):
        pass

    # Exit a parse tree produced by ExcelParser#tableconstructor.
    def exitTableconstructor(self, ctx:ExcelParser.TableconstructorContext):
        pass


    # Enter a parse tree produced by ExcelParser#fieldlist.
    def enterFieldlist(self, ctx:ExcelParser.FieldlistContext):
        pass

    # Exit a parse tree produced by ExcelParser#fieldlist.
    def exitFieldlist(self, ctx:ExcelParser.FieldlistContext):
        pass


    # Enter a parse tree produced by ExcelParser#field.
    def enterField(self, ctx:ExcelParser.FieldContext):
        pass

    # Exit a parse tree produced by ExcelParser#field.
    def exitField(self, ctx:ExcelParser.FieldContext):
        pass


    # Enter a parse tree produced by ExcelParser#fieldsep.
    def enterFieldsep(self, ctx:ExcelParser.FieldsepContext):
        pass

    # Exit a parse tree produced by ExcelParser#fieldsep.
    def exitFieldsep(self, ctx:ExcelParser.FieldsepContext):
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


    # Enter a parse tree produced by ExcelParser#operatorStrcat.
    def enterOperatorStrcat(self, ctx:ExcelParser.OperatorStrcatContext):
        pass

    # Exit a parse tree produced by ExcelParser#operatorStrcat.
    def exitOperatorStrcat(self, ctx:ExcelParser.OperatorStrcatContext):
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


