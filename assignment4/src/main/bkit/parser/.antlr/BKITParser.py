# Generated from /media/thanhnguyen2612/01D3670DD5838B40/Tien Thanh/HK201/Programming Languages/Assignment/assignment4/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u013a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\5\2G\n\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\7\3N\n\3\f\3\16\3Q\13\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4X\n\4\3\5\7\5[\n\5\f\5\16\5^\13\5\3\5\7\5a\n\5")
        buf.write("\f\5\16\5d\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\7\7p\n\7\f\7\16\7s\13\7\3\b\3\b\7\bw\n\b\f\b\16\bz")
        buf.write("\13\b\3\b\3\b\5\b~\n\b\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u008f\n\f\f\f\16")
        buf.write("\f\u0092\13\f\3\f\3\f\5\f\u0096\n\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\5\30\u00cf\n\30\3\30\3")
        buf.write("\30\3\31\7\31\u00d4\n\31\f\31\16\31\u00d7\13\31\3\31\7")
        buf.write("\31\u00da\n\31\f\31\16\31\u00dd\13\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\5\32\u00e8\n\32\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u00ee\n\33\3\33\3\33\3\34\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\5\36")
        buf.write("\u00ff\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37\u0108")
        buf.write("\n\37\3 \3 \3 \3 \3 \3 \5 \u0110\n \3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \6 \u0120\n \r \16 \u0121\7 \u0124")
        buf.write("\n \f \16 \u0127\13 \3!\3!\3!\3!\3!\3!\3!\5!\u0130\n!")
        buf.write("\3\"\3\"\3\"\7\"\u0135\n\"\f\"\16\"\u0138\13\"\3\"\2\3")
        buf.write(">#\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@B\2\6\3\2\3\4\3\2\6\n\4\2\3\4\13\f\3\2\r")
        buf.write("\16\2\u013e\2D\3\2\2\2\4J\3\2\2\2\6W\3\2\2\2\b\\\3\2\2")
        buf.write("\2\ng\3\2\2\2\fl\3\2\2\2\16t\3\2\2\2\20\177\3\2\2\2\22")
        buf.write("\u0083\3\2\2\2\24\u0085\3\2\2\2\26\u008a\3\2\2\2\30\u009a")
        buf.write("\3\2\2\2\32\u009e\3\2\2\2\34\u00a7\3\2\2\2\36\u00ad\3")
        buf.write("\2\2\2 \u00b1\3\2\2\2\"\u00b3\3\2\2\2$\u00b5\3\2\2\2&")
        buf.write("\u00bc\3\2\2\2(\u00c3\3\2\2\2*\u00c6\3\2\2\2,\u00c9\3")
        buf.write("\2\2\2.\u00cc\3\2\2\2\60\u00d5\3\2\2\2\62\u00e7\3\2\2")
        buf.write("\2\64\u00e9\3\2\2\2\66\u00f1\3\2\2\28\u00f5\3\2\2\2:\u00fb")
        buf.write("\3\2\2\2<\u0107\3\2\2\2>\u010f\3\2\2\2@\u012f\3\2\2\2")
        buf.write("B\u0131\3\2\2\2DF\7)\2\2EG\5\4\3\2FE\3\2\2\2FG\3\2\2\2")
        buf.write("GH\3\2\2\2HI\7*\2\2I\3\3\2\2\2JO\5\6\4\2KL\7-\2\2LN\5")
        buf.write("\6\4\2MK\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\5\3\2")
        buf.write("\2\2QO\3\2\2\2RX\7\61\2\2SX\7\62\2\2TX\7\63\2\2UX\7\64")
        buf.write("\2\2VX\5\2\2\2WR\3\2\2\2WS\3\2\2\2WT\3\2\2\2WU\3\2\2\2")
        buf.write("WV\3\2\2\2X\7\3\2\2\2Y[\5\n\6\2ZY\3\2\2\2[^\3\2\2\2\\")
        buf.write("Z\3\2\2\2\\]\3\2\2\2]b\3\2\2\2^\\\3\2\2\2_a\5\64\33\2")
        buf.write("`_\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2ce\3\2\2\2db\3")
        buf.write("\2\2\2ef\7\2\2\3f\t\3\2\2\2gh\7\37\2\2hi\7+\2\2ij\5\f")
        buf.write("\7\2jk\7.\2\2k\13\3\2\2\2lq\5\16\b\2mn\7-\2\2np\5\16\b")
        buf.write("\2om\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2r\r\3\2\2\2")
        buf.write("sq\3\2\2\2tx\7\60\2\2uw\5\20\t\2vu\3\2\2\2wz\3\2\2\2x")
        buf.write("v\3\2\2\2xy\3\2\2\2y}\3\2\2\2zx\3\2\2\2{|\7$\2\2|~\5\22")
        buf.write("\n\2}{\3\2\2\2}~\3\2\2\2~\17\3\2\2\2\177\u0080\7\'\2\2")
        buf.write("\u0080\u0081\7\61\2\2\u0081\u0082\7(\2\2\u0082\21\3\2")
        buf.write("\2\2\u0083\u0084\5\6\4\2\u0084\23\3\2\2\2\u0085\u0086")
        buf.write("\5<\37\2\u0086\u0087\7$\2\2\u0087\u0088\5<\37\2\u0088")
        buf.write("\u0089\7.\2\2\u0089\25\3\2\2\2\u008a\u008b\7\33\2\2\u008b")
        buf.write("\u0090\5\30\r\2\u008c\u008d\7\24\2\2\u008d\u008f\5\30")
        buf.write("\r\2\u008e\u008c\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e")
        buf.write("\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0095\3\2\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0093\u0094\7\23\2\2\u0094\u0096\5\60\31")
        buf.write("\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u0098\7\26\2\2\u0098\u0099\7,\2\2\u0099")
        buf.write("\27\3\2\2\2\u009a\u009b\5<\37\2\u009b\u009c\7\36\2\2\u009c")
        buf.write("\u009d\5\60\31\2\u009d\31\3\2\2\2\u009e\u009f\7\31\2\2")
        buf.write("\u009f\u00a0\7%\2\2\u00a0\u00a1\5\34\17\2\u00a1\u00a2")
        buf.write("\7&\2\2\u00a2\u00a3\7\22\2\2\u00a3\u00a4\5\60\31\2\u00a4")
        buf.write("\u00a5\7\27\2\2\u00a5\u00a6\7,\2\2\u00a6\33\3\2\2\2\u00a7")
        buf.write("\u00a8\5\36\20\2\u00a8\u00a9\7-\2\2\u00a9\u00aa\5 \21")
        buf.write("\2\u00aa\u00ab\7-\2\2\u00ab\u00ac\5\"\22\2\u00ac\35\3")
        buf.write("\2\2\2\u00ad\u00ae\7\60\2\2\u00ae\u00af\7$\2\2\u00af\u00b0")
        buf.write("\5<\37\2\u00b0\37\3\2\2\2\u00b1\u00b2\5<\37\2\u00b2!\3")
        buf.write("\2\2\2\u00b3\u00b4\5<\37\2\u00b4#\3\2\2\2\u00b5\u00b6")
        buf.write("\7 \2\2\u00b6\u00b7\5<\37\2\u00b7\u00b8\7\22\2\2\u00b8")
        buf.write("\u00b9\5\60\31\2\u00b9\u00ba\7\30\2\2\u00ba\u00bb\7,\2")
        buf.write("\2\u00bb%\3\2\2\2\u00bc\u00bd\7\22\2\2\u00bd\u00be\5\60")
        buf.write("\31\2\u00be\u00bf\7 \2\2\u00bf\u00c0\5<\37\2\u00c0\u00c1")
        buf.write("\7!\2\2\u00c1\u00c2\7,\2\2\u00c2\'\3\2\2\2\u00c3\u00c4")
        buf.write("\7\20\2\2\u00c4\u00c5\7.\2\2\u00c5)\3\2\2\2\u00c6\u00c7")
        buf.write("\7\21\2\2\u00c7\u00c8\7.\2\2\u00c8+\3\2\2\2\u00c9\u00ca")
        buf.write("\5:\36\2\u00ca\u00cb\7.\2\2\u00cb-\3\2\2\2\u00cc\u00ce")
        buf.write("\7\35\2\2\u00cd\u00cf\5<\37\2\u00ce\u00cd\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\7.\2\2")
        buf.write("\u00d1/\3\2\2\2\u00d2\u00d4\5\n\6\2\u00d3\u00d2\3\2\2")
        buf.write("\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6")
        buf.write("\3\2\2\2\u00d6\u00db\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8")
        buf.write("\u00da\5\62\32\2\u00d9\u00d8\3\2\2\2\u00da\u00dd\3\2\2")
        buf.write("\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\61\3")
        buf.write("\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00e8\5\24\13\2\u00df")
        buf.write("\u00e8\5\26\f\2\u00e0\u00e8\5\32\16\2\u00e1\u00e8\5$\23")
        buf.write("\2\u00e2\u00e8\5&\24\2\u00e3\u00e8\5(\25\2\u00e4\u00e8")
        buf.write("\5*\26\2\u00e5\u00e8\5,\27\2\u00e6\u00e8\5.\30\2\u00e7")
        buf.write("\u00de\3\2\2\2\u00e7\u00df\3\2\2\2\u00e7\u00e0\3\2\2\2")
        buf.write("\u00e7\u00e1\3\2\2\2\u00e7\u00e2\3\2\2\2\u00e7\u00e3\3")
        buf.write("\2\2\2\u00e7\u00e4\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e6")
        buf.write("\3\2\2\2\u00e8\63\3\2\2\2\u00e9\u00ea\7\32\2\2\u00ea\u00eb")
        buf.write("\7+\2\2\u00eb\u00ed\7\60\2\2\u00ec\u00ee\5\66\34\2\u00ed")
        buf.write("\u00ec\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2")
        buf.write("\u00ef\u00f0\58\35\2\u00f0\65\3\2\2\2\u00f1\u00f2\7\34")
        buf.write("\2\2\u00f2\u00f3\7+\2\2\u00f3\u00f4\5\f\7\2\u00f4\67\3")
        buf.write("\2\2\2\u00f5\u00f6\7\17\2\2\u00f6\u00f7\7+\2\2\u00f7\u00f8")
        buf.write("\5\60\31\2\u00f8\u00f9\7\25\2\2\u00f9\u00fa\7,\2\2\u00fa")
        buf.write("9\3\2\2\2\u00fb\u00fc\7\60\2\2\u00fc\u00fe\7%\2\2\u00fd")
        buf.write("\u00ff\5B\"\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100\u0101\7&\2\2\u0101;\3\2\2\2")
        buf.write("\u0102\u0103\5> \2\u0103\u0104\7/\2\2\u0104\u0105\5> ")
        buf.write("\2\u0105\u0108\3\2\2\2\u0106\u0108\5> \2\u0107\u0102\3")
        buf.write("\2\2\2\u0107\u0106\3\2\2\2\u0108=\3\2\2\2\u0109\u010a")
        buf.write("\b \1\2\u010a\u010b\t\2\2\2\u010b\u0110\5> \b\u010c\u010d")
        buf.write("\7\5\2\2\u010d\u0110\5> \7\u010e\u0110\5@!\2\u010f\u0109")
        buf.write("\3\2\2\2\u010f\u010c\3\2\2\2\u010f\u010e\3\2\2\2\u0110")
        buf.write("\u0125\3\2\2\2\u0111\u0112\f\6\2\2\u0112\u0113\t\3\2\2")
        buf.write("\u0113\u0124\5> \7\u0114\u0115\f\5\2\2\u0115\u0116\t\4")
        buf.write("\2\2\u0116\u0124\5> \6\u0117\u0118\f\4\2\2\u0118\u0119")
        buf.write("\t\5\2\2\u0119\u0124\5> \5\u011a\u011f\f\t\2\2\u011b\u011c")
        buf.write("\7\'\2\2\u011c\u011d\5<\37\2\u011d\u011e\7(\2\2\u011e")
        buf.write("\u0120\3\2\2\2\u011f\u011b\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124\3")
        buf.write("\2\2\2\u0123\u0111\3\2\2\2\u0123\u0114\3\2\2\2\u0123\u0117")
        buf.write("\3\2\2\2\u0123\u011a\3\2\2\2\u0124\u0127\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126?\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0128\u0129\7%\2\2\u0129\u012a\5<\37\2")
        buf.write("\u012a\u012b\7&\2\2\u012b\u0130\3\2\2\2\u012c\u0130\5")
        buf.write(":\36\2\u012d\u0130\7\60\2\2\u012e\u0130\5\6\4\2\u012f")
        buf.write("\u0128\3\2\2\2\u012f\u012c\3\2\2\2\u012f\u012d\3\2\2\2")
        buf.write("\u012f\u012e\3\2\2\2\u0130A\3\2\2\2\u0131\u0136\5<\37")
        buf.write("\2\u0132\u0133\7-\2\2\u0133\u0135\5<\37\2\u0134\u0132")
        buf.write("\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137C\3\2\2\2\u0138\u0136\3\2\2\2\31F")
        buf.write("OW\\bqx}\u0090\u0095\u00ce\u00d5\u00db\u00e7\u00ed\u00fe")
        buf.write("\u0107\u010f\u0121\u0123\u0125\u012f\u0136")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'-.'", "'!'", "'*'", "'*.'", "'\\'", 
                     "'\\.'", "'%'", "'+'", "'+.'", "'&&'", "'||'", "'Body'", 
                     "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
                     "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", 
                     "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
                     "'Var'", "'While'", "'EndDo'", "<INVALID>", "<INVALID>", 
                     "'='", "'('", "')'", "'['", "']'", "'{'", "'}'", "':'", 
                     "'.'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                      "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "ENDDO", "WS", "CMT", "EQ", "LP", 
                      "RP", "LS", "RS", "LB", "RB", "COLON", "DOT", "COMMA", 
                      "SEMI", "RELOP", "ID", "INTLIT", "FLOATLIT", "BOOLLIT", 
                      "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR" ]

    RULE_arraylit = 0
    RULE_litlist = 1
    RULE_literal = 2
    RULE_program = 3
    RULE_vardecl = 4
    RULE_varlist = 5
    RULE_variable = 6
    RULE_dim = 7
    RULE_init = 8
    RULE_assignstmt = 9
    RULE_ifstmt = 10
    RULE_condblock = 11
    RULE_forstmt = 12
    RULE_iterblock = 13
    RULE_iterinit = 14
    RULE_itercond = 15
    RULE_iterupdate = 16
    RULE_whilestmt = 17
    RULE_dowhilestmt = 18
    RULE_breakstmt = 19
    RULE_continuestmt = 20
    RULE_callstmt = 21
    RULE_returnstmt = 22
    RULE_stmtlist = 23
    RULE_stmt = 24
    RULE_funcdecl = 25
    RULE_paramdecl = 26
    RULE_bodydecl = 27
    RULE_call = 28
    RULE_expr = 29
    RULE_relexpr = 30
    RULE_operand = 31
    RULE_exprlist = 32

    ruleNames =  [ "arraylit", "litlist", "literal", "program", "vardecl", 
                   "varlist", "variable", "dim", "init", "assignstmt", "ifstmt", 
                   "condblock", "forstmt", "iterblock", "iterinit", "itercond", 
                   "iterupdate", "whilestmt", "dowhilestmt", "breakstmt", 
                   "continuestmt", "callstmt", "returnstmt", "stmtlist", 
                   "stmt", "funcdecl", "paramdecl", "bodydecl", "call", 
                   "expr", "relexpr", "operand", "exprlist" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    BODY=13
    BREAK=14
    CONTINUE=15
    DO=16
    ELSE=17
    ELSEIF=18
    ENDBODY=19
    ENDIF=20
    ENDFOR=21
    ENDWHILE=22
    FOR=23
    FUNCTION=24
    IF=25
    PARAMETER=26
    RETURN=27
    THEN=28
    VAR=29
    WHILE=30
    ENDDO=31
    WS=32
    CMT=33
    EQ=34
    LP=35
    RP=36
    LS=37
    RS=38
    LB=39
    RB=40
    COLON=41
    DOT=42
    COMMA=43
    SEMI=44
    RELOP=45
    ID=46
    INTLIT=47
    FLOATLIT=48
    BOOLLIT=49
    STRINGLIT=50
    UNCLOSE_STRING=51
    ILLEGAL_ESCAPE=52
    UNTERMINATED_COMMENT=53
    ERROR_CHAR=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ArraylitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def litlist(self):
            return self.getTypedRuleContext(BKITParser.LitlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_arraylit




    def arraylit(self):

        localctx = BKITParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_arraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(BKITParser.LB)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 67
                self.litlist()


            self.state = 70
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKITParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_litlist




    def litlist(self):

        localctx = BKITParser.LitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_litlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.literal()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 73
                self.match(BKITParser.COMMA)
                self.state = 74
                self.literal()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKITParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(BKITParser.ArraylitContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_literal




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(BKITParser.INTLIT)
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(BKITParser.FLOATLIT)
                pass
            elif token in [BKITParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.match(BKITParser.BOOLLIT)
                pass
            elif token in [BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.match(BKITParser.STRINGLIT)
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 84
                self.arraylit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKITParser.VardeclContext,i)


        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(BKITParser.FuncdeclContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 87
                self.vardecl()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 93
                self.funcdecl()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def varlist(self):
            return self.getTypedRuleContext(BKITParser.VarlistContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_vardecl




    def vardecl(self):

        localctx = BKITParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(BKITParser.VAR)
            self.state = 102
            self.match(BKITParser.COLON)
            self.state = 103
            self.varlist()
            self.state = 104
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VariableContext)
            else:
                return self.getTypedRuleContext(BKITParser.VariableContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_varlist




    def varlist(self):

        localctx = BKITParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.variable()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 107
                self.match(BKITParser.COMMA)
                self.state = 108
                self.variable()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dim(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.DimContext)
            else:
                return self.getTypedRuleContext(BKITParser.DimContext,i)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def init(self):
            return self.getTypedRuleContext(BKITParser.InitContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(BKITParser.ID)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LS:
                self.state = 115
                self.dim()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.EQ:
                self.state = 121
                self.match(BKITParser.EQ)
                self.state = 122
                self.init()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(BKITParser.LS, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def RS(self):
            return self.getToken(BKITParser.RS, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dim




    def dim(self):

        localctx = BKITParser.DimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(BKITParser.LS)
            self.state = 126
            self.match(BKITParser.INTLIT)
            self.state = 127
            self.match(BKITParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init




    def init(self):

        localctx = BKITParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assignstmt




    def assignstmt(self):

        localctx = BKITParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.expr()
            self.state = 132
            self.match(BKITParser.EQ)
            self.state = 133
            self.expr()
            self.state = 134
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def condblock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.CondblockContext)
            else:
                return self.getTypedRuleContext(BKITParser.CondblockContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(BKITParser.StmtlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_ifstmt




    def ifstmt(self):

        localctx = BKITParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(BKITParser.IF)
            self.state = 137
            self.condblock()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 138
                self.match(BKITParser.ELSEIF)
                self.state = 139
                self.condblock()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 145
                self.match(BKITParser.ELSE)
                self.state = 146
                self.stmtlist()


            self.state = 149
            self.match(BKITParser.ENDIF)
            self.state = 150
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondblockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(BKITParser.StmtlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_condblock




    def condblock(self):

        localctx = BKITParser.CondblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_condblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.expr()
            self.state = 153
            self.match(BKITParser.THEN)
            self.state = 154
            self.stmtlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def iterblock(self):
            return self.getTypedRuleContext(BKITParser.IterblockContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(BKITParser.StmtlistContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_forstmt




    def forstmt(self):

        localctx = BKITParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(BKITParser.FOR)
            self.state = 157
            self.match(BKITParser.LP)
            self.state = 158
            self.iterblock()
            self.state = 159
            self.match(BKITParser.RP)
            self.state = 160
            self.match(BKITParser.DO)
            self.state = 161
            self.stmtlist()
            self.state = 162
            self.match(BKITParser.ENDFOR)
            self.state = 163
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterblockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iterinit(self):
            return self.getTypedRuleContext(BKITParser.IterinitContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def itercond(self):
            return self.getTypedRuleContext(BKITParser.ItercondContext,0)


        def iterupdate(self):
            return self.getTypedRuleContext(BKITParser.IterupdateContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_iterblock




    def iterblock(self):

        localctx = BKITParser.IterblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_iterblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.iterinit()
            self.state = 166
            self.match(BKITParser.COMMA)
            self.state = 167
            self.itercond()
            self.state = 168
            self.match(BKITParser.COMMA)
            self.state = 169
            self.iterupdate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterinitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_iterinit




    def iterinit(self):

        localctx = BKITParser.IterinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_iterinit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(BKITParser.ID)
            self.state = 172
            self.match(BKITParser.EQ)
            self.state = 173
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItercondContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_itercond




    def itercond(self):

        localctx = BKITParser.ItercondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_itercond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterupdateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_iterupdate




    def iterupdate(self):

        localctx = BKITParser.IterupdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_iterupdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(BKITParser.StmtlistContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_whilestmt




    def whilestmt(self):

        localctx = BKITParser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(BKITParser.WHILE)
            self.state = 180
            self.expr()
            self.state = 181
            self.match(BKITParser.DO)
            self.state = 182
            self.stmtlist()
            self.state = 183
            self.match(BKITParser.ENDWHILE)
            self.state = 184
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(BKITParser.StmtlistContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dowhilestmt




    def dowhilestmt(self):

        localctx = BKITParser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(BKITParser.DO)
            self.state = 187
            self.stmtlist()
            self.state = 188
            self.match(BKITParser.WHILE)
            self.state = 189
            self.expr()
            self.state = 190
            self.match(BKITParser.ENDDO)
            self.state = 191
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_breakstmt




    def breakstmt(self):

        localctx = BKITParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(BKITParser.BREAK)
            self.state = 194
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continuestmt




    def continuestmt(self):

        localctx = BKITParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(BKITParser.CONTINUE)
            self.state = 197
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_callstmt




    def callstmt(self):

        localctx = BKITParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.call()
            self.state = 200
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_returnstmt




    def returnstmt(self):

        localctx = BKITParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(BKITParser.RETURN)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__0) | (1 << BKITParser.T__1) | (1 << BKITParser.T__2) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.ID) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 203
                self.expr()


            self.state = 206
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKITParser.VardeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_stmtlist




    def stmtlist(self):

        localctx = BKITParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmtlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 208
                self.vardecl()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 214
                    self.stmt() 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(BKITParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(BKITParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(BKITParser.ForstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(BKITParser.WhilestmtContext,0)


        def dowhilestmt(self):
            return self.getTypedRuleContext(BKITParser.DowhilestmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(BKITParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(BKITParser.ContinuestmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(BKITParser.CallstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(BKITParser.ReturnstmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 224
                self.dowhilestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 225
                self.breakstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 226
                self.continuestmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 227
                self.callstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 228
                self.returnstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def bodydecl(self):
            return self.getTypedRuleContext(BKITParser.BodydeclContext,0)


        def paramdecl(self):
            return self.getTypedRuleContext(BKITParser.ParamdeclContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKITParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(BKITParser.FUNCTION)
            self.state = 232
            self.match(BKITParser.COLON)
            self.state = 233
            self.match(BKITParser.ID)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 234
                self.paramdecl()


            self.state = 237
            self.bodydecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def varlist(self):
            return self.getTypedRuleContext(BKITParser.VarlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_paramdecl




    def paramdecl(self):

        localctx = BKITParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(BKITParser.PARAMETER)
            self.state = 240
            self.match(BKITParser.COLON)
            self.state = 241
            self.varlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodydeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(BKITParser.StmtlistContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_bodydecl




    def bodydecl(self):

        localctx = BKITParser.BodydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_bodydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(BKITParser.BODY)
            self.state = 244
            self.match(BKITParser.COLON)
            self.state = 245
            self.stmtlist()
            self.state = 246
            self.match(BKITParser.ENDBODY)
            self.state = 247
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKITParser.ExprlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call




    def call(self):

        localctx = BKITParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(BKITParser.ID)
            self.state = 250
            self.match(BKITParser.LP)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__0) | (1 << BKITParser.T__1) | (1 << BKITParser.T__2) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.ID) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 251
                self.exprlist()


            self.state = 254
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.RelexprContext)
            else:
                return self.getTypedRuleContext(BKITParser.RelexprContext,i)


        def RELOP(self):
            return self.getToken(BKITParser.RELOP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr




    def expr(self):

        localctx = BKITParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.relexpr(0)
                self.state = 257
                self.match(BKITParser.RELOP)
                self.state = 258
                self.relexpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.relexpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.RelexprContext)
            else:
                return self.getTypedRuleContext(BKITParser.RelexprContext,i)


        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def LS(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LS)
            else:
                return self.getToken(BKITParser.LS, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def RS(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RS)
            else:
                return self.getToken(BKITParser.RS, i)

        def getRuleIndex(self):
            return BKITParser.RULE_relexpr



    def relexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.RelexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_relexpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.T__0, BKITParser.T__1]:
                self.state = 264
                _la = self._input.LA(1)
                if not(_la==BKITParser.T__0 or _la==BKITParser.T__1):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 265
                self.relexpr(6)
                pass
            elif token in [BKITParser.T__2]:
                self.state = 266
                self.match(BKITParser.T__2)
                self.state = 267
                self.relexpr(5)
                pass
            elif token in [BKITParser.LP, BKITParser.LB, BKITParser.ID, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.BOOLLIT, BKITParser.STRINGLIT]:
                self.state = 268
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 289
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.RelexprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relexpr)
                        self.state = 271
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 272
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__3) | (1 << BKITParser.T__4) | (1 << BKITParser.T__5) | (1 << BKITParser.T__6) | (1 << BKITParser.T__7))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 273
                        self.relexpr(5)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.RelexprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relexpr)
                        self.state = 274
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 275
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__0) | (1 << BKITParser.T__1) | (1 << BKITParser.T__8) | (1 << BKITParser.T__9))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 276
                        self.relexpr(4)
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.RelexprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relexpr)
                        self.state = 277
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 278
                        _la = self._input.LA(1)
                        if not(_la==BKITParser.T__10 or _la==BKITParser.T__11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 279
                        self.relexpr(3)
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.RelexprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relexpr)
                        self.state = 280
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 285 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 281
                                self.match(BKITParser.LS)
                                self.state = 282
                                self.expr()
                                self.state = 283
                                self.match(BKITParser.RS)

                            else:
                                raise NoViableAltException(self)
                            self.state = 287 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                        pass

             
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_operand)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(BKITParser.LP)
                self.state = 295
                self.expr()
                self.state = 296
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 299
                self.match(BKITParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 300
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_exprlist




    def exprlist(self):

        localctx = BKITParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exprlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.expr()
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 304
                self.match(BKITParser.COMMA)
                self.state = 305
                self.expr()
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[30] = self.relexpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def relexpr_sempred(self, localctx:RelexprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         




