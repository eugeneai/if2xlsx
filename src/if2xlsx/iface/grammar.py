from antlr4 import InputStream, CommonTokenStream, FileStream
from .gram.ExcelLexer import ExcelLexer
from .gram.ExcelParser import ExcelParser
from .gram.ExcelVisitor import ExcelVisitor
from antlr4 import BailErrorStrategy
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
import sys


class Parser(ExcelParser):
    """Adding some useful methods

    """

    def __init__(self, input, output=sys.stdout):
        super(Parser, self).__init__(input, output)
        self._errHandler = ErrorStrategy()
        self.parsing_exception = None
        self.parsing_exception_happened = False
        self.parsing_exception_count = 0

    def reset(self):
        super().reset()
        self.parsing_exception = None
        self.parsing_exception_happened = False
        self.parsing_exception_count = 0


class ErrorStrategy(DefaultErrorStrategy):
    def __init__(self):
        super().__init__()

    def reportError(self, recognizer, e):
        super().reportError(recognizer, e)
        recognizer.parsing_exception = e
        recognizer.parsing_exception_happened = True
        recognizer.parsing_exception_count += 1


class Visitor(ExcelVisitor):
    """Documentation for Visitor
    """

    def visitNumber(self, ctx):
        print("Number:", ctx.INT(), ctx.HEX(), ctx.FLOAT(), ctx.HEX_FLOAT())


def create_parser(input_stream):

    lexer = ExcelLexer(input_stream)
    lstream = CommonTokenStream(lexer)
    parser = Parser(lstream)

    return parser


def parse_string(input, add_parser=False):
    istream = InputStream(input)
    parser = create_parser(istream)
    tree = parser.chunk()

    if add_parser:
        return tree, parser
    else:
        return tree


def parse_file(filelike):
    fstream = FileStream(filelike)
    parser = create_parser(fstream)
    tree = parser.chunk()

    return tree


def parser_helper(input):
    istream = InputStream(input)
    return create_parser(istream)
