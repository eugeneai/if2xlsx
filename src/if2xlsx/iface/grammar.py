from antlr4 import InputStream, CommonTokenStream
from .gram.ExcelLexer import ExcelLexer
from .gram.ExcelParser import ExcelParser


def parse_string(input):
    istream = InputStream(input)
    lexer = ExcelLexer(istream)
    lstream = CommonTokenStream(lexer)
    parer = ExcelParser(lstream)
    tree = parer.chunk()

    return tree
