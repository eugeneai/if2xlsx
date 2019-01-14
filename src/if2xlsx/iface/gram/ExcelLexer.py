# Generated from Excel.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .check import check_func_name, check_a_selector, check_rc_selector


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2/")
        buf.write("\u01dc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3\"\6\"\u00c5\n\"\r\"\16\"")
        buf.write("\u00c6\3#\3#\3#\6#\u00cc\n#\r#\16#\u00cd\3$\6$\u00d1\n")
        buf.write("$\r$\16$\u00d2\3$\3$\7$\u00d7\n$\f$\16$\u00da\13$\3$\5")
        buf.write("$\u00dd\n$\3$\3$\6$\u00e1\n$\r$\16$\u00e2\3$\5$\u00e6")
        buf.write("\n$\3$\6$\u00e9\n$\r$\16$\u00ea\3$\3$\5$\u00ef\n$\3%\3")
        buf.write("%\3%\6%\u00f4\n%\r%\16%\u00f5\3%\3%\7%\u00fa\n%\f%\16")
        buf.write("%\u00fd\13%\3%\5%\u0100\n%\3%\3%\3%\3%\6%\u0106\n%\r%")
        buf.write("\16%\u0107\3%\5%\u010b\n%\3%\3%\3%\6%\u0110\n%\r%\16%")
        buf.write("\u0111\3%\3%\5%\u0116\n%\3&\3&\5&\u011a\n&\3&\6&\u011d")
        buf.write("\n&\r&\16&\u011e\3\'\3\'\5\'\u0123\n\'\3\'\6\'\u0126\n")
        buf.write("\'\r\'\16\'\u0127\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(")
        buf.write("\u0135\n(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\6*\u0141\n*\r")
        buf.write("*\16*\u0142\3*\3*\3+\3+\3,\3,\3-\3-\3-\7-\u014e\n-\f-")
        buf.write("\16-\u0151\13-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\7\60\u015c")
        buf.write("\n\60\f\60\16\60\u015f\13\60\3\61\3\61\3\61\3\61\7\61")
        buf.write("\u0165\n\61\f\61\16\61\u0168\13\61\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\5\64\u0170\n\64\3\64\6\64\u0173\n\64\r\64\16")
        buf.write("\64\u0174\3\64\5\64\u0178\n\64\3\64\6\64\u017b\n\64\r")
        buf.write("\64\16\64\u017c\3\64\3\64\3\64\5\64\u0182\n\64\3\64\6")
        buf.write("\64\u0185\n\64\r\64\16\64\u0186\3\64\5\64\u018a\n\64\3")
        buf.write("\64\6\64\u018d\n\64\r\64\16\64\u018e\5\64\u0191\n\64\3")
        buf.write("\65\3\65\3\65\6\65\u0196\n\65\r\65\16\65\u0197\3\65\3")
        buf.write("\65\3\65\3\65\6\65\u019e\n\65\r\65\16\65\u019f\3\65\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\7\67\u01ab\n\67")
        buf.write("\f\67\16\67\u01ae\13\67\3\67\3\67\38\38\38\78\u01b5\n")
        buf.write("8\f8\168\u01b8\138\38\38\39\39\39\39\39\39\79\u01c2\n")
        buf.write("9\f9\169\u01c5\139\39\59\u01c8\n9\3:\3:\3:\3:\5:\u01ce")
        buf.write("\n:\3:\3:\3:\3:\5:\u01d4\n:\3;\6;\u01d7\n;\r;\16;\u01d8")
        buf.write("\3;\3;\3\u01c3\2<\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\2M\2O\2Q\2S\2U\2W\2Y\'[\2]\2_\2a\2c(e)g*i")
        buf.write("+k,m-o.q\2s\2u/\3\2\26\4\2ZZzz\4\2GGgg\4\2--//\4\2RRr")
        buf.write("r\3\2\62\64\3\2\62;\5\2\62;CHch\4\2\f\f\17\17\5\2C\\a")
        buf.write("ac|\6\2C\\aac|\u0412\u0451\3\2\60\60\3\2&&\4\2TTtt\3\2")
        buf.write("]]\3\2__\4\2EEee\4\2$$^^\4\2))^^\f\2$$))^^cdhhppttvvx")
        buf.write("x||\5\2\13\f\16\17\"\"\2\u0205\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2Y\3\2\2\2\2c\3\2\2\2\2")
        buf.write("e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2")
        buf.write("\2o\3\2\2\2\2u\3\2\2\2\3w\3\2\2\2\5y\3\2\2\2\7{\3\2\2")
        buf.write("\2\t}\3\2\2\2\13\177\3\2\2\2\r\u0081\3\2\2\2\17\u0083")
        buf.write("\3\2\2\2\21\u0085\3\2\2\2\23\u0087\3\2\2\2\25\u0089\3")
        buf.write("\2\2\2\27\u008b\3\2\2\2\31\u008e\3\2\2\2\33\u0092\3\2")
        buf.write("\2\2\35\u0094\3\2\2\2\37\u0096\3\2\2\2!\u0099\3\2\2\2")
        buf.write("#\u009c\3\2\2\2%\u009f\3\2\2\2\'\u00a2\3\2\2\2)\u00a4")
        buf.write("\3\2\2\2+\u00a6\3\2\2\2-\u00a8\3\2\2\2/\u00aa\3\2\2\2")
        buf.write("\61\u00ac\3\2\2\2\63\u00af\3\2\2\2\65\u00b1\3\2\2\2\67")
        buf.write("\u00b3\3\2\2\29\u00b5\3\2\2\2;\u00b8\3\2\2\2=\u00bb\3")
        buf.write("\2\2\2?\u00bf\3\2\2\2A\u00c1\3\2\2\2C\u00c4\3\2\2\2E\u00c8")
        buf.write("\3\2\2\2G\u00ee\3\2\2\2I\u0115\3\2\2\2K\u0117\3\2\2\2")
        buf.write("M\u0120\3\2\2\2O\u0134\3\2\2\2Q\u0136\3\2\2\2S\u013b\3")
        buf.write("\2\2\2U\u0146\3\2\2\2W\u0148\3\2\2\2Y\u014a\3\2\2\2[\u0154")
        buf.write("\3\2\2\2]\u0156\3\2\2\2_\u0158\3\2\2\2a\u0160\3\2\2\2")
        buf.write("c\u0169\3\2\2\2e\u016b\3\2\2\2g\u0190\3\2\2\2i\u0192\3")
        buf.write("\2\2\2k\u01a4\3\2\2\2m\u01a7\3\2\2\2o\u01b1\3\2\2\2q\u01c7")
        buf.write("\3\2\2\2s\u01d3\3\2\2\2u\u01d6\3\2\2\2wx\7?\2\2x\4\3\2")
        buf.write("\2\2yz\7.\2\2z\6\3\2\2\2{|\7*\2\2|\b\3\2\2\2}~\7+\2\2")
        buf.write("~\n\3\2\2\2\177\u0080\7}\2\2\u0080\f\3\2\2\2\u0081\u0082")
        buf.write("\7\177\2\2\u0082\16\3\2\2\2\u0083\u0084\7<\2\2\u0084\20")
        buf.write("\3\2\2\2\u0085\u0086\7]\2\2\u0086\22\3\2\2\2\u0087\u0088")
        buf.write("\7\60\2\2\u0088\24\3\2\2\2\u0089\u008a\7_\2\2\u008a\26")
        buf.write("\3\2\2\2\u008b\u008c\7q\2\2\u008c\u008d\7t\2\2\u008d\30")
        buf.write("\3\2\2\2\u008e\u008f\7c\2\2\u008f\u0090\7p\2\2\u0090\u0091")
        buf.write("\7f\2\2\u0091\32\3\2\2\2\u0092\u0093\7>\2\2\u0093\34\3")
        buf.write("\2\2\2\u0094\u0095\7@\2\2\u0095\36\3\2\2\2\u0096\u0097")
        buf.write("\7>\2\2\u0097\u0098\7?\2\2\u0098 \3\2\2\2\u0099\u009a")
        buf.write("\7@\2\2\u009a\u009b\7?\2\2\u009b\"\3\2\2\2\u009c\u009d")
        buf.write("\7\u0080\2\2\u009d\u009e\7?\2\2\u009e$\3\2\2\2\u009f\u00a0")
        buf.write("\7?\2\2\u00a0\u00a1\7?\2\2\u00a1&\3\2\2\2\u00a2\u00a3")
        buf.write("\7-\2\2\u00a3(\3\2\2\2\u00a4\u00a5\7/\2\2\u00a5*\3\2\2")
        buf.write("\2\u00a6\u00a7\7,\2\2\u00a7,\3\2\2\2\u00a8\u00a9\7\61")
        buf.write("\2\2\u00a9.\3\2\2\2\u00aa\u00ab\7\'\2\2\u00ab\60\3\2\2")
        buf.write("\2\u00ac\u00ad\7\61\2\2\u00ad\u00ae\7\61\2\2\u00ae\62")
        buf.write("\3\2\2\2\u00af\u00b0\7(\2\2\u00b0\64\3\2\2\2\u00b1\u00b2")
        buf.write("\7~\2\2\u00b2\66\3\2\2\2\u00b3\u00b4\7\u0080\2\2\u00b4")
        buf.write("8\3\2\2\2\u00b5\u00b6\7>\2\2\u00b6\u00b7\7>\2\2\u00b7")
        buf.write(":\3\2\2\2\u00b8\u00b9\7@\2\2\u00b9\u00ba\7@\2\2\u00ba")
        buf.write("<\3\2\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd\7q\2\2\u00bd")
        buf.write("\u00be\7v\2\2\u00be>\3\2\2\2\u00bf\u00c0\7%\2\2\u00c0")
        buf.write("@\3\2\2\2\u00c1\u00c2\7`\2\2\u00c2B\3\2\2\2\u00c3\u00c5")
        buf.write("\5U+\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c4")
        buf.write("\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7D\3\2\2\2\u00c8\u00c9")
        buf.write("\7\62\2\2\u00c9\u00cb\t\2\2\2\u00ca\u00cc\5W,\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cb\3\2\2\2")
        buf.write("\u00cd\u00ce\3\2\2\2\u00ceF\3\2\2\2\u00cf\u00d1\5U+\2")
        buf.write("\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d0\3")
        buf.write("\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d8")
        buf.write("\7\60\2\2\u00d5\u00d7\5U+\2\u00d6\u00d5\3\2\2\2\u00d7")
        buf.write("\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dd\5")
        buf.write("K&\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00ef")
        buf.write("\3\2\2\2\u00de\u00e0\7\60\2\2\u00df\u00e1\5U+\2\u00e0")
        buf.write("\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e0\3\2\2\2")
        buf.write("\u00e2\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e6\5")
        buf.write("K&\2\u00e5\u00e4\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00ef")
        buf.write("\3\2\2\2\u00e7\u00e9\5U+\2\u00e8\u00e7\3\2\2\2\u00e9\u00ea")
        buf.write("\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\u00ed\5K&\2\u00ed\u00ef\3\2\2\2\u00ee")
        buf.write("\u00d0\3\2\2\2\u00ee\u00de\3\2\2\2\u00ee\u00e8\3\2\2\2")
        buf.write("\u00efH\3\2\2\2\u00f0\u00f1\7\62\2\2\u00f1\u00f3\t\2\2")
        buf.write("\2\u00f2\u00f4\5W,\2\u00f3\u00f2\3\2\2\2\u00f4\u00f5\3")
        buf.write("\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7")
        buf.write("\3\2\2\2\u00f7\u00fb\7\60\2\2\u00f8\u00fa\5W,\2\u00f9")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2")
        buf.write("\u00fb\u00fc\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3")
        buf.write("\2\2\2\u00fe\u0100\5M\'\2\u00ff\u00fe\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\u0116\3\2\2\2\u0101\u0102\7\62\2\2\u0102")
        buf.write("\u0103\t\2\2\2\u0103\u0105\7\60\2\2\u0104\u0106\5W,\2")
        buf.write("\u0105\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0105\3")
        buf.write("\2\2\2\u0107\u0108\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u010b")
        buf.write("\5M\'\2\u010a\u0109\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u0116\3\2\2\2\u010c\u010d\7\62\2\2\u010d\u010f\t\2\2")
        buf.write("\2\u010e\u0110\5W,\2\u010f\u010e\3\2\2\2\u0110\u0111\3")
        buf.write("\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0114\5M\'\2\u0114\u0116\3\2\2\2\u0115")
        buf.write("\u00f0\3\2\2\2\u0115\u0101\3\2\2\2\u0115\u010c\3\2\2\2")
        buf.write("\u0116J\3\2\2\2\u0117\u0119\t\3\2\2\u0118\u011a\t\4\2")
        buf.write("\2\u0119\u0118\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011c")
        buf.write("\3\2\2\2\u011b\u011d\5U+\2\u011c\u011b\3\2\2\2\u011d\u011e")
        buf.write("\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f")
        buf.write("L\3\2\2\2\u0120\u0122\t\5\2\2\u0121\u0123\t\4\2\2\u0122")
        buf.write("\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2")
        buf.write("\u0124\u0126\5U+\2\u0125\u0124\3\2\2\2\u0126\u0127\3\2")
        buf.write("\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128N\3")
        buf.write("\2\2\2\u0129\u012a\7^\2\2\u012a\u0135\5U+\2\u012b\u012c")
        buf.write("\7^\2\2\u012c\u012d\5U+\2\u012d\u012e\5U+\2\u012e\u0135")
        buf.write("\3\2\2\2\u012f\u0130\7^\2\2\u0130\u0131\t\6\2\2\u0131")
        buf.write("\u0132\5U+\2\u0132\u0133\5U+\2\u0133\u0135\3\2\2\2\u0134")
        buf.write("\u0129\3\2\2\2\u0134\u012b\3\2\2\2\u0134\u012f\3\2\2\2")
        buf.write("\u0135P\3\2\2\2\u0136\u0137\7^\2\2\u0137\u0138\7z\2\2")
        buf.write("\u0138\u0139\5W,\2\u0139\u013a\5W,\2\u013aR\3\2\2\2\u013b")
        buf.write("\u013c\7^\2\2\u013c\u013d\7w\2\2\u013d\u013e\7}\2\2\u013e")
        buf.write("\u0140\3\2\2\2\u013f\u0141\5W,\2\u0140\u013f\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144\u0145\7\177\2\2\u0145T\3\2")
        buf.write("\2\2\u0146\u0147\t\7\2\2\u0147V\3\2\2\2\u0148\u0149\t")
        buf.write("\b\2\2\u0149X\3\2\2\2\u014a\u014b\7%\2\2\u014b\u014f\7")
        buf.write("#\2\2\u014c\u014e\n\t\2\2\u014d\u014c\3\2\2\2\u014e\u0151")
        buf.write("\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write("\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0153\b-\2\2")
        buf.write("\u0153Z\3\2\2\2\u0154\u0155\t\n\2\2\u0155\\\3\2\2\2\u0156")
        buf.write("\u0157\t\13\2\2\u0157^\3\2\2\2\u0158\u015d\5]/\2\u0159")
        buf.write("\u015c\5]/\2\u015a\u015c\5U+\2\u015b\u0159\3\2\2\2\u015b")
        buf.write("\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2")
        buf.write("\u015d\u015e\3\2\2\2\u015e`\3\2\2\2\u015f\u015d\3\2\2")
        buf.write("\2\u0160\u0166\5[.\2\u0161\u0165\5[.\2\u0162\u0165\5U")
        buf.write("+\2\u0163\u0165\t\f\2\2\u0164\u0161\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0164\u0163\3\2\2\2\u0165\u0168\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167b\3\2\2\2\u0168")
        buf.write("\u0166\3\2\2\2\u0169\u016a\5_\60\2\u016ad\3\2\2\2\u016b")
        buf.write("\u016c\5a\61\2\u016c\u016d\6\63\2\2\u016df\3\2\2\2\u016e")
        buf.write("\u0170\t\r\2\2\u016f\u016e\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0172\3\2\2\2\u0171\u0173\5[.\2\u0172\u0171\3\2")
        buf.write("\2\2\u0173\u0174\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0178\t\r\2\2\u0177")
        buf.write("\u0176\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017a\3\2\2\2")
        buf.write("\u0179\u017b\5U+\2\u017a\u0179\3\2\2\2\u017b\u017c\3\2")
        buf.write("\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017e\u017f\6\64\3\2\u017f\u0191\3\2\2\2\u0180")
        buf.write("\u0182\t\r\2\2\u0181\u0180\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0184\3\2\2\2\u0183\u0185\5[.\2\u0184\u0183\3\2")
        buf.write("\2\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187")
        buf.write("\3\2\2\2\u0187\u0191\3\2\2\2\u0188\u018a\t\r\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2")
        buf.write("\u018b\u018d\5U+\2\u018c\u018b\3\2\2\2\u018d\u018e\3\2")
        buf.write("\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0191")
        buf.write("\3\2\2\2\u0190\u016f\3\2\2\2\u0190\u0181\3\2\2\2\u0190")
        buf.write("\u0189\3\2\2\2\u0191h\3\2\2\2\u0192\u0193\t\16\2\2\u0193")
        buf.write("\u0195\t\17\2\2\u0194\u0196\5U+\2\u0195\u0194\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3")
        buf.write("\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\t\20\2\2\u019a")
        buf.write("\u019b\t\21\2\2\u019b\u019d\t\17\2\2\u019c\u019e\5U+\2")
        buf.write("\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d\3")
        buf.write("\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2")
        buf.write("\t\20\2\2\u01a2\u01a3\6\65\4\2\u01a3j\3\2\2\2\u01a4\u01a5")
        buf.write("\5_\60\2\u01a5\u01a6\7#\2\2\u01a6l\3\2\2\2\u01a7\u01ac")
        buf.write("\7$\2\2\u01a8\u01ab\5s:\2\u01a9\u01ab\n\22\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01af\3\2\2\2")
        buf.write("\u01ae\u01ac\3\2\2\2\u01af\u01b0\7$\2\2\u01b0n\3\2\2\2")
        buf.write("\u01b1\u01b6\7)\2\2\u01b2\u01b5\5s:\2\u01b3\u01b5\n\23")
        buf.write("\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5\u01b8")
        buf.write("\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7")
        buf.write("\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\7)\2\2")
        buf.write("\u01bap\3\2\2\2\u01bb\u01bc\7?\2\2\u01bc\u01bd\5q9\2\u01bd")
        buf.write("\u01be\7?\2\2\u01be\u01c8\3\2\2\2\u01bf\u01c3\7]\2\2\u01c0")
        buf.write("\u01c2\13\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2")
        buf.write("\2\u01c3\u01c4\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c6")
        buf.write("\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c8\7_\2\2\u01c7")
        buf.write("\u01bb\3\2\2\2\u01c7\u01bf\3\2\2\2\u01c8r\3\2\2\2\u01c9")
        buf.write("\u01ca\7^\2\2\u01ca\u01d4\t\24\2\2\u01cb\u01cd\7^\2\2")
        buf.write("\u01cc\u01ce\7\17\2\2\u01cd\u01cc\3\2\2\2\u01cd\u01ce")
        buf.write("\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d4\7\f\2\2\u01d0")
        buf.write("\u01d4\5O(\2\u01d1\u01d4\5Q)\2\u01d2\u01d4\5S*\2\u01d3")
        buf.write("\u01c9\3\2\2\2\u01d3\u01cb\3\2\2\2\u01d3\u01d0\3\2\2\2")
        buf.write("\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4t\3\2\2")
        buf.write("\2\u01d5\u01d7\t\25\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01d8")
        buf.write("\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9")
        buf.write("\u01da\3\2\2\2\u01da\u01db\b;\3\2\u01dbv\3\2\2\2\62\2")
        buf.write("\u00c6\u00cd\u00d2\u00d8\u00dc\u00e2\u00e5\u00ea\u00ee")
        buf.write("\u00f5\u00fb\u00ff\u0107\u010a\u0111\u0115\u0119\u011e")
        buf.write("\u0122\u0127\u0134\u0142\u014f\u015b\u015d\u0164\u0166")
        buf.write("\u016f\u0174\u0177\u017c\u0181\u0186\u0189\u018e\u0190")
        buf.write("\u0197\u019f\u01aa\u01ac\u01b4\u01b6\u01c3\u01c7\u01cd")
        buf.write("\u01d3\u01d8\4\2\3\2\b\2\2")
        return buf.getvalue()


class ExcelLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    INT = 33
    HEX = 34
    FLOAT = 35
    HEX_FLOAT = 36
    SHEBANG = 37
    NAME = 38
    FUNCNAME = 39
    ASELECTOR = 40
    RCSELECTOR = 41
    SHEETNAME = 42
    NORMALSTRING = 43
    CHARSTRING = 44
    WS = 45

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "','", "'('", "')'", "'{'", "'}'", "':'", "'['", "'.'", 
            "']'", "'or'", "'and'", "'<'", "'>'", "'<='", "'>='", "'~='", 
            "'=='", "'+'", "'-'", "'*'", "'/'", "'%'", "'//'", "'&'", "'|'", 
            "'~'", "'<<'", "'>>'", "'not'", "'#'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "HEX", "FLOAT", "HEX_FLOAT", "SHEBANG", "NAME", "FUNCNAME", 
            "ASELECTOR", "RCSELECTOR", "SHEETNAME", "NORMALSTRING", "CHARSTRING", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "INT", "HEX", "FLOAT", "HEX_FLOAT", "ExponentPart", "HexExponentPart", 
                  "DecimalEscape", "HexEscape", "UtfEscape", "Digit", "HexDigit", 
                  "SHEBANG", "SelChar", "IdChar", "IdWord", "IdFunc", "NAME", 
                  "FUNCNAME", "ASELECTOR", "RCSELECTOR", "SHEETNAME", "NORMALSTRING", 
                  "CHARSTRING", "NESTED_STR", "EscapeSequence", "WS" ]

    grammarFileName = "Excel.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[49] = self.FUNCNAME_sempred
            preds[50] = self.ASELECTOR_sempred
            preds[51] = self.RCSELECTOR_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def FUNCNAME_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return check_func_name(self.text)
         

    def ASELECTOR_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 1:
                return check_a_selector(self.text)
         

    def RCSELECTOR_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 2:
                return check_rc_selector(self.text)
         


