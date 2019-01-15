from if2xlsx.iface.grammar import parse_string, parser_helper
from if2xlsx.iface.grammar import Visitor

# Simple test formulae
inputs = [
    '=1+3+5',
    '=3 * 4 + 5',
    '=50',
    '=1+1',
    '=$A1',
    '=$B$2',
    '=$B2',
    '=Sheet1!$B2',
    '=B2',
    '=SUM(B2)',
    '=SUM($B5:B$15)',
    '=SUM(B5:B15)',
    '=SUM(B5:B15,D5:D15)',
    '=SUM(B5:B15 A7:D7)',
    '=SUM(sheet1!$A$1:$B$2)',
    '=[data.xls]sheet1!$A$1',
    '=SUM(($1:$2))',
    '=SUM((1:2))',
    '=SUM((A:A $1:$2))',
    '=SUM((A:A 1:1))',
    '=SUM((A:A,1:1))',
    '=SUM((A:A A1:B1))',
    '=SUM(D9:D11,E9:E11,F9:F11)',
    '=SUM((D9:D11,(E9:E11,F9:F11)))',
    '=IF(P5=1.0,"NA",IF(P5=2.0,"A",IF(P5=3.0,'
    '"B",IF(P5=4.0,"C",IF(P5=5.0,"D",IF(P5=6.0,'
    '"E",IF(P5=7.0,"F",IF(P5=8.0,"G"))))))))',
    '={SUM(B2:D2*B3:D3)}',
    '=SUM(123 + SUM(456) + (45DATE(2002,1,6),0,'
    'IF(ISERROR(R[41]C[2]),0,IF(R13C3>=R[41]C[2],0, '
    'IF(AND(R[23]C[11]>=55,R[24]C[11]>=20),R53C3,0)))))',
    '=IF(R[39]C[11]>65,R[25]C[42],ROUND((R[11]C[11]*IF(OR(AND(R[39]C[11]>=55, ' +
    'R[40]C[11]>=20),AND(R[40]C[11]>=20,R11C3="YES")),'
    'R[44]C[11],R[43]C[11]))+(R[14]C[11] ' +
    '*IF(OR(AND(R[39]C[11]>=55,R[40]C[11]>=20),AND(R[40]C[11]>=20,R11C3="YES")), ' +
    'R[45]C[11],R[43]C[11])),0))',
]


class TestEscelParser(object):
    """Testing excel parser

    """

    def test_range_expr(self):
        expr = '''=SUM($A$1:$A$10)'''
        tree = parse_string(expr)
        # print("Tree:", tree.toStringTree())
        assert tree is not None

    def setUp(self):
        self.p = parser_helper('=1')

    def test_expr_1(self):
        expr = """=LEFT((RIGHT((RIGHT(A2,LEN(A2)-FIND(";",A2))),LEN((RIGHT(A2,LEN(A2)-FIND(";",A2))))-FIND(";",(RIGHT(A2,LEN(A2)-FIND(";",A2)))))),FIND(";",(RIGHT((RIGHT(A2,LEN(A2)-FIND(";",A2))),LEN((RIGHT(A2,LEN(A2)-FIND(";",A2))))-FIND(";",(RIGHT(A2,LEN(A2)-FIND(";",A2)))))),1)-1)"""
        tree = parse_string(expr)
        # print("Tree:", tree.toStringTree())
        assert tree is not None

    def test_str_expr(self):
        expr = '''=SUM(INDIRECT("'"&"Sheet1"&"'!"&"data"))'''
        tree = parse_string(expr)
        # print("Tree:", tree.toStringTree())
        assert tree is not None

    def test_inputs(self):
        # print("-"*20)
        error_onece = False
        for f in inputs:
            tree, parser = parse_string(f, add_parser=True)
            if parser.parsing_exception_happened:
                print("Input: {}".format(f))
                print("COUNT:", parser.parsing_exception_count)
                error_onece = True
                print("Output: {}".format(tree.toStringTree(recog=self.p)))
                print("-"*20)
            else:
                visitor=Visitor()
                visitor.visit(tree)

        assert not error_onece, "Some expressions failed"
