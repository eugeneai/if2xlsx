from if2xlsx.iface.grammar import parse_string


class TestEscelParser(object):
    """Testing excel parser

    """

    def test_range_expr(self):
        expr = '''=SUM($A$1:$A$10)'''
        tree = parse_string(expr)
        # print("Tree:", tree.toStringTree())
        assert tree is not None

    def setUp(self):
        pass

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
