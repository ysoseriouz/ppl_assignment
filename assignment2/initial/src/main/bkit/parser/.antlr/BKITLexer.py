# Generated from /media/thanhnguyen2612/01D3670DD5838B40/Tien Thanh/HK201/Programming Languages/Assignment/assignment2/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u01fb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3!\6!\u0110\n!\r!\16!\u0111\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\7\"\u011a\n\"\f\"\16\"\u011d\13\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*")
        buf.write("\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0150\n.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\5\63\u015f\n\63\3\64\3\64\3\64\3\64\7\64\u0165\n\64\f")
        buf.write("\64\16\64\u0168\13\64\3\65\3\65\7\65\u016c\n\65\f\65\16")
        buf.write("\65\u016f\13\65\3\65\3\65\3\65\3\65\5\65\u0175\n\65\3")
        buf.write("\65\3\65\7\65\u0179\n\65\f\65\16\65\u017c\13\65\3\65\3")
        buf.write("\65\3\65\3\65\5\65\u0182\n\65\3\65\3\65\7\65\u0186\n\65")
        buf.write("\f\65\16\65\u0189\13\65\3\65\5\65\u018c\n\65\3\66\6\66")
        buf.write("\u018f\n\66\r\66\16\66\u0190\3\66\3\66\7\66\u0195\n\66")
        buf.write("\f\66\16\66\u0198\13\66\3\66\3\66\5\66\u019c\n\66\3\66")
        buf.write("\6\66\u019f\n\66\r\66\16\66\u01a0\5\66\u01a3\n\66\3\66")
        buf.write("\6\66\u01a6\n\66\r\66\16\66\u01a7\3\66\5\66\u01ab\n\66")
        buf.write("\3\66\7\66\u01ae\n\66\f\66\16\66\u01b1\13\66\3\66\3\66")
        buf.write("\5\66\u01b5\n\66\3\66\6\66\u01b8\n\66\r\66\16\66\u01b9")
        buf.write("\5\66\u01bc\n\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\5\67\u01c7\n\67\38\38\78\u01cb\n8\f8\168\u01ce")
        buf.write("\138\38\38\38\39\39\79\u01d5\n9\f9\169\u01d8\139\39\5")
        buf.write("9\u01db\n9\39\39\3:\3:\7:\u01e1\n:\f:\16:\u01e4\13:\3")
        buf.write(":\3:\3:\3:\5:\u01ea\n:\3:\3:\3;\3;\3;\3;\7;\u01f2\n;\f")
        buf.write(";\16;\u01f5\13;\3;\3;\3;\3<\3<\4\u011b\u01cc\2=\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\2_\2a\2c\2e\2g\60i\61k\62m\63o\64q\65s\66u\67")
        buf.write("w8\3\2\23\5\2\13\f\16\17\"\"\4\2>>@@\4\2C\\c|\3\2\62;")
        buf.write("\4\2\62;CH\3\2\629\6\2\f\f$$))^^\t\2))^^ddhhppttvv\3\2")
        buf.write("c|\3\2\63;\4\2\63;CH\3\2\639\4\2GGgg\4\2--//\3\2$$\3\3")
        buf.write("\f\f\3\2,,\2\u021e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2")
        buf.write("\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write("\2\3y\3\2\2\2\5{\3\2\2\2\7~\3\2\2\2\t\u0080\3\2\2\2\13")
        buf.write("\u0082\3\2\2\2\r\u0085\3\2\2\2\17\u0087\3\2\2\2\21\u008a")
        buf.write("\3\2\2\2\23\u008c\3\2\2\2\25\u008e\3\2\2\2\27\u0091\3")
        buf.write("\2\2\2\31\u0094\3\2\2\2\33\u0097\3\2\2\2\35\u009c\3\2")
        buf.write("\2\2\37\u00a2\3\2\2\2!\u00ab\3\2\2\2#\u00ae\3\2\2\2%\u00b3")
        buf.write("\3\2\2\2\'\u00ba\3\2\2\2)\u00c2\3\2\2\2+\u00c8\3\2\2\2")
        buf.write("-\u00cf\3\2\2\2/\u00d8\3\2\2\2\61\u00dc\3\2\2\2\63\u00e5")
        buf.write("\3\2\2\2\65\u00e8\3\2\2\2\67\u00f2\3\2\2\29\u00f9\3\2")
        buf.write("\2\2;\u00fe\3\2\2\2=\u0102\3\2\2\2?\u0108\3\2\2\2A\u010f")
        buf.write("\3\2\2\2C\u0115\3\2\2\2E\u0123\3\2\2\2G\u0125\3\2\2\2")
        buf.write("I\u0127\3\2\2\2K\u0129\3\2\2\2M\u012b\3\2\2\2O\u012d\3")
        buf.write("\2\2\2Q\u012f\3\2\2\2S\u0131\3\2\2\2U\u0133\3\2\2\2W\u0135")
        buf.write("\3\2\2\2Y\u0137\3\2\2\2[\u014f\3\2\2\2]\u0151\3\2\2\2")
        buf.write("_\u0153\3\2\2\2a\u0155\3\2\2\2c\u0157\3\2\2\2e\u015e\3")
        buf.write("\2\2\2g\u0160\3\2\2\2i\u018b\3\2\2\2k\u01bb\3\2\2\2m\u01c6")
        buf.write("\3\2\2\2o\u01c8\3\2\2\2q\u01d2\3\2\2\2s\u01de\3\2\2\2")
        buf.write("u\u01ed\3\2\2\2w\u01f9\3\2\2\2yz\7/\2\2z\4\3\2\2\2{|\7")
        buf.write("/\2\2|}\7\60\2\2}\6\3\2\2\2~\177\7#\2\2\177\b\3\2\2\2")
        buf.write("\u0080\u0081\7,\2\2\u0081\n\3\2\2\2\u0082\u0083\7,\2\2")
        buf.write("\u0083\u0084\7\60\2\2\u0084\f\3\2\2\2\u0085\u0086\7^\2")
        buf.write("\2\u0086\16\3\2\2\2\u0087\u0088\7^\2\2\u0088\u0089\7\60")
        buf.write("\2\2\u0089\20\3\2\2\2\u008a\u008b\7\'\2\2\u008b\22\3\2")
        buf.write("\2\2\u008c\u008d\7-\2\2\u008d\24\3\2\2\2\u008e\u008f\7")
        buf.write("-\2\2\u008f\u0090\7\60\2\2\u0090\26\3\2\2\2\u0091\u0092")
        buf.write("\7(\2\2\u0092\u0093\7(\2\2\u0093\30\3\2\2\2\u0094\u0095")
        buf.write("\7~\2\2\u0095\u0096\7~\2\2\u0096\32\3\2\2\2\u0097\u0098")
        buf.write("\7D\2\2\u0098\u0099\7q\2\2\u0099\u009a\7f\2\2\u009a\u009b")
        buf.write("\7{\2\2\u009b\34\3\2\2\2\u009c\u009d\7D\2\2\u009d\u009e")
        buf.write("\7t\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1")
        buf.write("\7m\2\2\u00a1\36\3\2\2\2\u00a2\u00a3\7E\2\2\u00a3\u00a4")
        buf.write("\7q\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7k\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7w\2\2\u00a9\u00aa")
        buf.write("\7g\2\2\u00aa \3\2\2\2\u00ab\u00ac\7F\2\2\u00ac\u00ad")
        buf.write("\7q\2\2\u00ad\"\3\2\2\2\u00ae\u00af\7G\2\2\u00af\u00b0")
        buf.write("\7n\2\2\u00b0\u00b1\7u\2\2\u00b1\u00b2\7g\2\2\u00b2$\3")
        buf.write("\2\2\2\u00b3\u00b4\7G\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6")
        buf.write("\7u\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7K\2\2\u00b8\u00b9")
        buf.write("\7h\2\2\u00b9&\3\2\2\2\u00ba\u00bb\7G\2\2\u00bb\u00bc")
        buf.write("\7p\2\2\u00bc\u00bd\7f\2\2\u00bd\u00be\7D\2\2\u00be\u00bf")
        buf.write("\7q\2\2\u00bf\u00c0\7f\2\2\u00c0\u00c1\7{\2\2\u00c1(\3")
        buf.write("\2\2\2\u00c2\u00c3\7G\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5")
        buf.write("\7f\2\2\u00c5\u00c6\7K\2\2\u00c6\u00c7\7h\2\2\u00c7*\3")
        buf.write("\2\2\2\u00c8\u00c9\7G\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb")
        buf.write("\7f\2\2\u00cb\u00cc\7H\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7t\2\2\u00ce,\3\2\2\2\u00cf\u00d0\7G\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7f\2\2\u00d2\u00d3\7Y\2\2\u00d3\u00d4")
        buf.write("\7j\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7.\3\2\2\2\u00d8\u00d9\7H\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7t\2\2\u00db\60\3\2\2\2\u00dc\u00dd")
        buf.write("\7H\2\2\u00dd\u00de\7w\2\2\u00de\u00df\7p\2\2\u00df\u00e0")
        buf.write("\7e\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3")
        buf.write("\7q\2\2\u00e3\u00e4\7p\2\2\u00e4\62\3\2\2\2\u00e5\u00e6")
        buf.write("\7K\2\2\u00e6\u00e7\7h\2\2\u00e7\64\3\2\2\2\u00e8\u00e9")
        buf.write("\7R\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec")
        buf.write("\7c\2\2\u00ec\u00ed\7o\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef")
        buf.write("\7v\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7t\2\2\u00f1\66")
        buf.write("\3\2\2\2\u00f2\u00f3\7T\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f88\3\2\2\2\u00f9\u00fa\7V\2\2\u00fa\u00fb")
        buf.write("\7j\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7p\2\2\u00fd:\3")
        buf.write("\2\2\2\u00fe\u00ff\7X\2\2\u00ff\u0100\7c\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101<\3\2\2\2\u0102\u0103\7Y\2\2\u0103\u0104")
        buf.write("\7j\2\2\u0104\u0105\7k\2\2\u0105\u0106\7n\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107>\3\2\2\2\u0108\u0109\7G\2\2\u0109\u010a")
        buf.write("\7p\2\2\u010a\u010b\7f\2\2\u010b\u010c\7F\2\2\u010c\u010d")
        buf.write("\7q\2\2\u010d@\3\2\2\2\u010e\u0110\t\2\2\2\u010f\u010e")
        buf.write("\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u010f\3\2\2\2\u0111")
        buf.write("\u0112\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114\b!\2\2")
        buf.write("\u0114B\3\2\2\2\u0115\u0116\7,\2\2\u0116\u0117\7,\2\2")
        buf.write("\u0117\u011b\3\2\2\2\u0118\u011a\13\2\2\2\u0119\u0118")
        buf.write("\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u011c\3\2\2\2\u011b")
        buf.write("\u0119\3\2\2\2\u011c\u011e\3\2\2\2\u011d\u011b\3\2\2\2")
        buf.write("\u011e\u011f\7,\2\2\u011f\u0120\7,\2\2\u0120\u0121\3\2")
        buf.write("\2\2\u0121\u0122\b\"\2\2\u0122D\3\2\2\2\u0123\u0124\7")
        buf.write("?\2\2\u0124F\3\2\2\2\u0125\u0126\7*\2\2\u0126H\3\2\2\2")
        buf.write("\u0127\u0128\7+\2\2\u0128J\3\2\2\2\u0129\u012a\7]\2\2")
        buf.write("\u012aL\3\2\2\2\u012b\u012c\7_\2\2\u012cN\3\2\2\2\u012d")
        buf.write("\u012e\7}\2\2\u012eP\3\2\2\2\u012f\u0130\7\177\2\2\u0130")
        buf.write("R\3\2\2\2\u0131\u0132\7<\2\2\u0132T\3\2\2\2\u0133\u0134")
        buf.write("\7\60\2\2\u0134V\3\2\2\2\u0135\u0136\7.\2\2\u0136X\3\2")
        buf.write("\2\2\u0137\u0138\7=\2\2\u0138Z\3\2\2\2\u0139\u013a\7?")
        buf.write("\2\2\u013a\u0150\7?\2\2\u013b\u013c\7#\2\2\u013c\u0150")
        buf.write("\7?\2\2\u013d\u0150\t\3\2\2\u013e\u013f\7>\2\2\u013f\u0150")
        buf.write("\7?\2\2\u0140\u0141\7@\2\2\u0141\u0150\7?\2\2\u0142\u0143")
        buf.write("\7?\2\2\u0143\u0144\7\61\2\2\u0144\u0150\7?\2\2\u0145")
        buf.write("\u0146\7>\2\2\u0146\u0150\7\60\2\2\u0147\u0148\7@\2\2")
        buf.write("\u0148\u0150\7\60\2\2\u0149\u014a\7>\2\2\u014a\u014b\7")
        buf.write("?\2\2\u014b\u0150\7\60\2\2\u014c\u014d\7@\2\2\u014d\u014e")
        buf.write("\7?\2\2\u014e\u0150\7\60\2\2\u014f\u0139\3\2\2\2\u014f")
        buf.write("\u013b\3\2\2\2\u014f\u013d\3\2\2\2\u014f\u013e\3\2\2\2")
        buf.write("\u014f\u0140\3\2\2\2\u014f\u0142\3\2\2\2\u014f\u0145\3")
        buf.write("\2\2\2\u014f\u0147\3\2\2\2\u014f\u0149\3\2\2\2\u014f\u014c")
        buf.write("\3\2\2\2\u0150\\\3\2\2\2\u0151\u0152\t\4\2\2\u0152^\3")
        buf.write("\2\2\2\u0153\u0154\t\5\2\2\u0154`\3\2\2\2\u0155\u0156")
        buf.write("\t\6\2\2\u0156b\3\2\2\2\u0157\u0158\t\7\2\2\u0158d\3\2")
        buf.write("\2\2\u0159\u015f\n\b\2\2\u015a\u015b\7^\2\2\u015b\u015f")
        buf.write("\t\t\2\2\u015c\u015d\7)\2\2\u015d\u015f\7$\2\2\u015e\u0159")
        buf.write("\3\2\2\2\u015e\u015a\3\2\2\2\u015e\u015c\3\2\2\2\u015f")
        buf.write("f\3\2\2\2\u0160\u0166\t\n\2\2\u0161\u0165\5]/\2\u0162")
        buf.write("\u0165\5_\60\2\u0163\u0165\7a\2\2\u0164\u0161\3\2\2\2")
        buf.write("\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2\u0165\u0168\3")
        buf.write("\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167h")
        buf.write("\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016d\t\13\2\2\u016a")
        buf.write("\u016c\5_\60\2\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2")
        buf.write("\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u018c\3")
        buf.write("\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171\7\62\2\2\u0171")
        buf.write("\u0175\7z\2\2\u0172\u0173\7\62\2\2\u0173\u0175\7Z\2\2")
        buf.write("\u0174\u0170\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176\u017a\t\f\2\2\u0177\u0179\5a\61\2\u0178\u0177")
        buf.write("\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u018c\3\2\2\2\u017c\u017a\3\2\2\2")
        buf.write("\u017d\u017e\7\62\2\2\u017e\u0182\7q\2\2\u017f\u0180\7")
        buf.write("\62\2\2\u0180\u0182\7Q\2\2\u0181\u017d\3\2\2\2\u0181\u017f")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0187\t\r\2\2\u0184")
        buf.write("\u0186\5c\62\2\u0185\u0184\3\2\2\2\u0186\u0189\3\2\2\2")
        buf.write("\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u018c\3")
        buf.write("\2\2\2\u0189\u0187\3\2\2\2\u018a\u018c\7\62\2\2\u018b")
        buf.write("\u0169\3\2\2\2\u018b\u0174\3\2\2\2\u018b\u0181\3\2\2\2")
        buf.write("\u018b\u018a\3\2\2\2\u018cj\3\2\2\2\u018d\u018f\5_\60")
        buf.write("\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u018e")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0192\3\2\2\2\u0192")
        buf.write("\u0196\5U+\2\u0193\u0195\5_\60\2\u0194\u0193\3\2\2\2\u0195")
        buf.write("\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197\u01a2\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019b\t")
        buf.write("\16\2\2\u019a\u019c\t\17\2\2\u019b\u019a\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019c\u019e\3\2\2\2\u019d\u019f\5_\60\2")
        buf.write("\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u019e\3")
        buf.write("\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a3\3\2\2\2\u01a2\u0199")
        buf.write("\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01bc\3\2\2\2\u01a4")
        buf.write("\u01a6\5_\60\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2")
        buf.write("\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3")
        buf.write("\2\2\2\u01a9\u01ab\5U+\2\u01aa\u01a9\3\2\2\2\u01aa\u01ab")
        buf.write("\3\2\2\2\u01ab\u01af\3\2\2\2\u01ac\u01ae\5_\60\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2")
        buf.write("\u01af\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01af\3")
        buf.write("\2\2\2\u01b2\u01b4\t\16\2\2\u01b3\u01b5\t\17\2\2\u01b4")
        buf.write("\u01b3\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b7\3\2\2\2")
        buf.write("\u01b6\u01b8\5_\60\2\u01b7\u01b6\3\2\2\2\u01b8\u01b9\3")
        buf.write("\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bc")
        buf.write("\3\2\2\2\u01bb\u018e\3\2\2\2\u01bb\u01a5\3\2\2\2\u01bc")
        buf.write("l\3\2\2\2\u01bd\u01be\7V\2\2\u01be\u01bf\7t\2\2\u01bf")
        buf.write("\u01c0\7w\2\2\u01c0\u01c7\7g\2\2\u01c1\u01c2\7H\2\2\u01c2")
        buf.write("\u01c3\7c\2\2\u01c3\u01c4\7n\2\2\u01c4\u01c5\7u\2\2\u01c5")
        buf.write("\u01c7\7g\2\2\u01c6\u01bd\3\2\2\2\u01c6\u01c1\3\2\2\2")
        buf.write("\u01c7n\3\2\2\2\u01c8\u01cc\7$\2\2\u01c9\u01cb\5e\63\2")
        buf.write("\u01ca\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01cd\3")
        buf.write("\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc")
        buf.write("\3\2\2\2\u01cf\u01d0\7$\2\2\u01d0\u01d1\b8\3\2\u01d1p")
        buf.write("\3\2\2\2\u01d2\u01d6\7$\2\2\u01d3\u01d5\n\20\2\2\u01d4")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3")
        buf.write("\2\2\2\u01d9\u01db\t\21\2\2\u01da\u01d9\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dc\u01dd\b9\4\2\u01ddr\3\2\2\2\u01de")
        buf.write("\u01e2\7$\2\2\u01df\u01e1\5e\63\2\u01e0\u01df\3\2\2\2")
        buf.write("\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3")
        buf.write("\2\2\2\u01e3\u01e9\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e6")
        buf.write("\7^\2\2\u01e6\u01ea\n\t\2\2\u01e7\u01e8\7)\2\2\u01e8\u01ea")
        buf.write("\n\20\2\2\u01e9\u01e5\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea")
        buf.write("\u01eb\3\2\2\2\u01eb\u01ec\b:\5\2\u01ect\3\2\2\2\u01ed")
        buf.write("\u01ee\7,\2\2\u01ee\u01ef\7,\2\2\u01ef\u01f3\3\2\2\2\u01f0")
        buf.write("\u01f2\n\22\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01f5\3\2\2")
        buf.write("\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f6")
        buf.write("\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01f7\7,\2\2\u01f7")
        buf.write("\u01f8\n\22\2\2\u01f8v\3\2\2\2\u01f9\u01fa\13\2\2\2\u01fa")
        buf.write("x\3\2\2\2!\2\u0111\u011b\u014f\u015e\u0164\u0166\u016d")
        buf.write("\u0174\u017a\u0181\u0187\u018b\u0190\u0196\u019b\u01a0")
        buf.write("\u01a2\u01a7\u01aa\u01af\u01b4\u01b9\u01bb\u01c6\u01cc")
        buf.write("\u01d6\u01da\u01e2\u01e9\u01f3\6\b\2\2\38\2\39\3\3:\4")
        return buf.getvalue()


class BKITLexer(Lexer):

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
    BODY = 13
    BREAK = 14
    CONTINUE = 15
    DO = 16
    ELSE = 17
    ELSEIF = 18
    ENDBODY = 19
    ENDIF = 20
    ENDFOR = 21
    ENDWHILE = 22
    FOR = 23
    FUNCTION = 24
    IF = 25
    PARAMETER = 26
    RETURN = 27
    THEN = 28
    VAR = 29
    WHILE = 30
    ENDDO = 31
    WS = 32
    CMT = 33
    EQ = 34
    LP = 35
    RP = 36
    LS = 37
    RS = 38
    LB = 39
    RB = 40
    COLON = 41
    DOT = 42
    COMMA = 43
    SEMI = 44
    RELOP = 45
    ID = 46
    INTLIT = 47
    FLOATLIT = 48
    BOOLLIT = 49
    STRINGLIT = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52
    UNTERMINATED_COMMENT = 53
    ERROR_CHAR = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'", "'-.'", "'!'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", 
            "'+'", "'+.'", "'&&'", "'||'", "'Body'", "'Break'", "'Continue'", 
            "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
            "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
            "'Return'", "'Then'", "'Var'", "'While'", "'EndDo'", "'='", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "':'", "'.'", "','", 
            "';'" ]

    symbolicNames = [ "<INVALID>",
            "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "ENDDO", "WS", "CMT", "EQ", 
            "LP", "RP", "LS", "RS", "LB", "RB", "COLON", "DOT", "COMMA", 
            "SEMI", "RELOP", "ID", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "ENDDO", "WS", "CMT", 
                  "EQ", "LP", "RP", "LS", "RS", "LB", "RB", "COLON", "DOT", 
                  "COMMA", "SEMI", "RELOP", "LETTER", "DIGIT", "HEX", "OCT", 
                  "CHAR", "ID", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.STRINGLIT_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             
                        self.text = self.text[1:-1] 
                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
                        self.text = self.text[1:]
                    
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             
                        self.text = self.text[1:]
                    
     


