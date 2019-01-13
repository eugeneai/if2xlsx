from antlr4 import InputStream, CommonTokenStream, FileStream
from .gram.ExcelLexer import ExcelLexer
from .gram.ExcelParser import ExcelParser


def create_parser(input_stream):

    lexer = ExcelLexer(input_stream)
    lstream = CommonTokenStream(lexer)
    parser = ExcelParser(lstream)

    return parser


def parse_string(input):
    istream = InputStream(input)
    parser = create_parser(istream)
    tree = parser.chunk()

    return tree


def parse_file(filelike):
    fstream = FileStream(filelike)
    parser = create_parser(fstream)
    tree = parser.chunk()

    return tree


def parser_helper(input):
    istream = InputStream(input)
    return create_parser(istream)
