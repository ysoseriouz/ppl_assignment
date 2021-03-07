// Generated from /media/thanhnguyen2612/01D3670DD5838B40/Tien Thanh/HK201/Programming Languages/tutorial2/src/main/bkit/parser/test/BKITtest.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITtestLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		BODY=1, BREAK=2, CONTINUE=3, DO=4, ELSE=5, ELSEIF=6, ENDBODY=7, ENDIF=8, 
		ENDFOR=9, ENDWHILE=10, FOR=11, FUNCTION=12, IF=13, PARAMETER=14, RETURN=15, 
		THEN=16, VAR=17, WHILE=18, TRUE=19, FALSE=20, ENDDO=21, EQ=22, LP=23, 
		RP=24, LS=25, RS=26, LB=27, RB=28, COLON=29, DOT=30, COMMA=31, SEMI=32, 
		ESCAPE=33, WS=34, CMT=35, ID=36, INT=37, FLOAT=38, BOOL=39, STRING=40, 
		ERROR_CHAR=41, UNCLOSE_STRING=42, ILLEGAL_ESCAPE=43, UNTERMINATED_COMMENT=44;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
			"ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
			"THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "EQ", "LP", "RP", "LS", 
			"RS", "LB", "RB", "COLON", "DOT", "COMMA", "SEMI", "ESCAPE", "WS", "CMT", 
			"LETTER", "DIGIT", "HEX", "OCT", "ID", "INT", "FLOAT", "BOOL", "STRING", 
			"ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
			"'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
			"'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", "'True'", 
			"'False'", "'EndDo'", "'='", "'('", "')'", "'['", "']'", "'{'", "'}'", 
			"':'", "'.'", "','", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
			"ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
			"RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "EQ", "LP", 
			"RP", "LS", "RS", "LB", "RB", "COLON", "DOT", "COMMA", "SEMI", "ESCAPE", 
			"WS", "CMT", "ID", "INT", "FLOAT", "BOOL", "STRING", "ERROR_CHAR", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public BKITtestLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BKITtest.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2.\u018d\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\2\3\2\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3"+
		"\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3"+
		"\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3"+
		"\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3"+
		"\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3"+
		"\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\6#\u00ff\n#\r#\16#\u0100\3#\3#\3"+
		"$\3$\3$\3$\7$\u0109\n$\f$\16$\u010c\13$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3\'"+
		"\3\'\3(\3(\3)\3)\3)\3)\7)\u011f\n)\f)\16)\u0122\13)\3*\3*\7*\u0126\n*"+
		"\f*\16*\u0129\13*\3*\3*\3*\3*\5*\u012f\n*\3*\3*\7*\u0133\n*\f*\16*\u0136"+
		"\13*\3*\3*\3*\3*\5*\u013c\n*\3*\3*\7*\u0140\n*\f*\16*\u0143\13*\3*\5*"+
		"\u0146\n*\3+\6+\u0149\n+\r+\16+\u014a\3+\3+\7+\u014f\n+\f+\16+\u0152\13"+
		"+\3+\3+\5+\u0156\n+\5+\u0158\n+\3+\6+\u015b\n+\r+\16+\u015c\3+\6+\u0160"+
		"\n+\r+\16+\u0161\3+\5+\u0165\n+\3+\7+\u0168\n+\f+\16+\u016b\13+\3+\3+"+
		"\5+\u016f\n+\3+\6+\u0172\n+\r+\16+\u0173\5+\u0176\n+\3,\3,\5,\u017a\n"+
		",\3-\3-\3-\7-\u017f\n-\f-\16-\u0182\13-\3-\3-\3.\3.\3/\3/\3\60\3\60\3"+
		"\61\3\61\4\u010a\u0180\2\62\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25"+
		"\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32"+
		"\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I\2K\2M\2O\2Q&S\'U(W)Y*[+],_-a"+
		".\3\2\16\6\2\n\f\16\17))^^\5\2\13\f\17\17\"\"\4\2C\\c|\3\2\62;\4\2\62"+
		";CH\3\2\629\3\2c|\3\2\63;\4\2\63;CH\3\2\639\4\2GGgg\4\2--//\2\u01a3\2"+
		"\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2"+
		"\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2"+
		"\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2"+
		"\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2"+
		"\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2"+
		"\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2"+
		"\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]"+
		"\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\3c\3\2\2\2\5h\3\2\2\2\7n\3\2\2\2\tw\3\2"+
		"\2\2\13z\3\2\2\2\r\177\3\2\2\2\17\u0086\3\2\2\2\21\u008e\3\2\2\2\23\u0094"+
		"\3\2\2\2\25\u009b\3\2\2\2\27\u00a4\3\2\2\2\31\u00a8\3\2\2\2\33\u00b1\3"+
		"\2\2\2\35\u00b4\3\2\2\2\37\u00be\3\2\2\2!\u00c5\3\2\2\2#\u00ca\3\2\2\2"+
		"%\u00ce\3\2\2\2\'\u00d4\3\2\2\2)\u00d9\3\2\2\2+\u00df\3\2\2\2-\u00e5\3"+
		"\2\2\2/\u00e7\3\2\2\2\61\u00e9\3\2\2\2\63\u00eb\3\2\2\2\65\u00ed\3\2\2"+
		"\2\67\u00ef\3\2\2\29\u00f1\3\2\2\2;\u00f3\3\2\2\2=\u00f5\3\2\2\2?\u00f7"+
		"\3\2\2\2A\u00f9\3\2\2\2C\u00fb\3\2\2\2E\u00fe\3\2\2\2G\u0104\3\2\2\2I"+
		"\u0112\3\2\2\2K\u0114\3\2\2\2M\u0116\3\2\2\2O\u0118\3\2\2\2Q\u011a\3\2"+
		"\2\2S\u0145\3\2\2\2U\u0175\3\2\2\2W\u0179\3\2\2\2Y\u017b\3\2\2\2[\u0185"+
		"\3\2\2\2]\u0187\3\2\2\2_\u0189\3\2\2\2a\u018b\3\2\2\2cd\7D\2\2de\7q\2"+
		"\2ef\7f\2\2fg\7{\2\2g\4\3\2\2\2hi\7D\2\2ij\7t\2\2jk\7g\2\2kl\7c\2\2lm"+
		"\7m\2\2m\6\3\2\2\2no\7E\2\2op\7q\2\2pq\7p\2\2qr\7v\2\2rs\7k\2\2st\7p\2"+
		"\2tu\7w\2\2uv\7g\2\2v\b\3\2\2\2wx\7F\2\2xy\7q\2\2y\n\3\2\2\2z{\7G\2\2"+
		"{|\7n\2\2|}\7u\2\2}~\7g\2\2~\f\3\2\2\2\177\u0080\7G\2\2\u0080\u0081\7"+
		"n\2\2\u0081\u0082\7u\2\2\u0082\u0083\7g\2\2\u0083\u0084\7K\2\2\u0084\u0085"+
		"\7h\2\2\u0085\16\3\2\2\2\u0086\u0087\7G\2\2\u0087\u0088\7p\2\2\u0088\u0089"+
		"\7f\2\2\u0089\u008a\7D\2\2\u008a\u008b\7q\2\2\u008b\u008c\7f\2\2\u008c"+
		"\u008d\7{\2\2\u008d\20\3\2\2\2\u008e\u008f\7G\2\2\u008f\u0090\7p\2\2\u0090"+
		"\u0091\7f\2\2\u0091\u0092\7K\2\2\u0092\u0093\7h\2\2\u0093\22\3\2\2\2\u0094"+
		"\u0095\7G\2\2\u0095\u0096\7p\2\2\u0096\u0097\7f\2\2\u0097\u0098\7H\2\2"+
		"\u0098\u0099\7q\2\2\u0099\u009a\7t\2\2\u009a\24\3\2\2\2\u009b\u009c\7"+
		"G\2\2\u009c\u009d\7p\2\2\u009d\u009e\7f\2\2\u009e\u009f\7Y\2\2\u009f\u00a0"+
		"\7j\2\2\u00a0\u00a1\7k\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3\7g\2\2\u00a3"+
		"\26\3\2\2\2\u00a4\u00a5\7H\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7t\2\2\u00a7"+
		"\30\3\2\2\2\u00a8\u00a9\7H\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab\7p\2\2\u00ab"+
		"\u00ac\7e\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7q\2\2"+
		"\u00af\u00b0\7p\2\2\u00b0\32\3\2\2\2\u00b1\u00b2\7K\2\2\u00b2\u00b3\7"+
		"h\2\2\u00b3\34\3\2\2\2\u00b4\u00b5\7R\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7"+
		"\7t\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9\7o\2\2\u00b9\u00ba\7g\2\2\u00ba"+
		"\u00bb\7v\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7t\2\2\u00bd\36\3\2\2\2\u00be"+
		"\u00bf\7T\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7w\2\2"+
		"\u00c2\u00c3\7t\2\2\u00c3\u00c4\7p\2\2\u00c4 \3\2\2\2\u00c5\u00c6\7V\2"+
		"\2\u00c6\u00c7\7j\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7p\2\2\u00c9\"\3"+
		"\2\2\2\u00ca\u00cb\7X\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd\7t\2\2\u00cd"+
		"$\3\2\2\2\u00ce\u00cf\7Y\2\2\u00cf\u00d0\7j\2\2\u00d0\u00d1\7k\2\2\u00d1"+
		"\u00d2\7n\2\2\u00d2\u00d3\7g\2\2\u00d3&\3\2\2\2\u00d4\u00d5\7V\2\2\u00d5"+
		"\u00d6\7t\2\2\u00d6\u00d7\7w\2\2\u00d7\u00d8\7g\2\2\u00d8(\3\2\2\2\u00d9"+
		"\u00da\7H\2\2\u00da\u00db\7c\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7u\2\2"+
		"\u00dd\u00de\7g\2\2\u00de*\3\2\2\2\u00df\u00e0\7G\2\2\u00e0\u00e1\7p\2"+
		"\2\u00e1\u00e2\7f\2\2\u00e2\u00e3\7F\2\2\u00e3\u00e4\7q\2\2\u00e4,\3\2"+
		"\2\2\u00e5\u00e6\7?\2\2\u00e6.\3\2\2\2\u00e7\u00e8\7*\2\2\u00e8\60\3\2"+
		"\2\2\u00e9\u00ea\7+\2\2\u00ea\62\3\2\2\2\u00eb\u00ec\7]\2\2\u00ec\64\3"+
		"\2\2\2\u00ed\u00ee\7_\2\2\u00ee\66\3\2\2\2\u00ef\u00f0\7}\2\2\u00f08\3"+
		"\2\2\2\u00f1\u00f2\7\177\2\2\u00f2:\3\2\2\2\u00f3\u00f4\7<\2\2\u00f4<"+
		"\3\2\2\2\u00f5\u00f6\7\60\2\2\u00f6>\3\2\2\2\u00f7\u00f8\7.\2\2\u00f8"+
		"@\3\2\2\2\u00f9\u00fa\7=\2\2\u00faB\3\2\2\2\u00fb\u00fc\t\2\2\2\u00fc"+
		"D\3\2\2\2\u00fd\u00ff\t\3\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2"+
		"\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103"+
		"\b#\2\2\u0103F\3\2\2\2\u0104\u0105\7,\2\2\u0105\u0106\7,\2\2\u0106\u010a"+
		"\3\2\2\2\u0107\u0109\13\2\2\2\u0108\u0107\3\2\2\2\u0109\u010c\3\2\2\2"+
		"\u010a\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010d\3\2\2\2\u010c\u010a"+
		"\3\2\2\2\u010d\u010e\7,\2\2\u010e\u010f\7,\2\2\u010f\u0110\3\2\2\2\u0110"+
		"\u0111\b$\2\2\u0111H\3\2\2\2\u0112\u0113\t\4\2\2\u0113J\3\2\2\2\u0114"+
		"\u0115\t\5\2\2\u0115L\3\2\2\2\u0116\u0117\t\6\2\2\u0117N\3\2\2\2\u0118"+
		"\u0119\t\7\2\2\u0119P\3\2\2\2\u011a\u0120\t\b\2\2\u011b\u011f\5I%\2\u011c"+
		"\u011f\5K&\2\u011d\u011f\7a\2\2\u011e\u011b\3\2\2\2\u011e\u011c\3\2\2"+
		"\2\u011e\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121"+
		"\3\2\2\2\u0121R\3\2\2\2\u0122\u0120\3\2\2\2\u0123\u0127\t\t\2\2\u0124"+
		"\u0126\5K&\2\u0125\u0124\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2"+
		"\2\u0127\u0128\3\2\2\2\u0128\u0146\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b"+
		"\7\62\2\2\u012b\u012f\7z\2\2\u012c\u012d\7\62\2\2\u012d\u012f\7Z\2\2\u012e"+
		"\u012a\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0134\t\n"+
		"\2\2\u0131\u0133\5M\'\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134"+
		"\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0146\3\2\2\2\u0136\u0134\3\2"+
		"\2\2\u0137\u0138\7\62\2\2\u0138\u013c\7q\2\2\u0139\u013a\7\62\2\2\u013a"+
		"\u013c\7Q\2\2\u013b\u0137\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d\3\2"+
		"\2\2\u013d\u0141\t\13\2\2\u013e\u0140\5O(\2\u013f\u013e\3\2\2\2\u0140"+
		"\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0146\3\2"+
		"\2\2\u0143\u0141\3\2\2\2\u0144\u0146\7\62\2\2\u0145\u0123\3\2\2\2\u0145"+
		"\u012e\3\2\2\2\u0145\u013b\3\2\2\2\u0145\u0144\3\2\2\2\u0146T\3\2\2\2"+
		"\u0147\u0149\5K&\2\u0148\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u0148"+
		"\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u0150\5=\37\2\u014d"+
		"\u014f\5K&\2\u014e\u014d\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2"+
		"\2\u0150\u0151\3\2\2\2\u0151\u0157\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0155"+
		"\t\f\2\2\u0154\u0156\t\r\2\2\u0155\u0154\3\2\2\2\u0155\u0156\3\2\2\2\u0156"+
		"\u0158\3\2\2\2\u0157\u0153\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u015a\3\2"+
		"\2\2\u0159\u015b\5K&\2\u015a\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015a"+
		"\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u0176\3\2\2\2\u015e\u0160\5K&\2\u015f"+
		"\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2"+
		"\2\2\u0162\u0164\3\2\2\2\u0163\u0165\5=\37\2\u0164\u0163\3\2\2\2\u0164"+
		"\u0165\3\2\2\2\u0165\u0169\3\2\2\2\u0166\u0168\5K&\2\u0167\u0166\3\2\2"+
		"\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c"+
		"\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016e\t\f\2\2\u016d\u016f\t\r\2\2\u016e"+
		"\u016d\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0171\3\2\2\2\u0170\u0172\5K"+
		"&\2\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0171\3\2\2\2\u0173"+
		"\u0174\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0148\3\2\2\2\u0175\u015f\3\2"+
		"\2\2\u0176V\3\2\2\2\u0177\u017a\5\'\24\2\u0178\u017a\5)\25\2\u0179\u0177"+
		"\3\2\2\2\u0179\u0178\3\2\2\2\u017aX\3\2\2\2\u017b\u0180\7$\2\2\u017c\u017f"+
		"\5C\"\2\u017d\u017f\13\2\2\2\u017e\u017c\3\2\2\2\u017e\u017d\3\2\2\2\u017f"+
		"\u0182\3\2\2\2\u0180\u0181\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0183\3\2"+
		"\2\2\u0182\u0180\3\2\2\2\u0183\u0184\7$\2\2\u0184Z\3\2\2\2\u0185\u0186"+
		"\13\2\2\2\u0186\\\3\2\2\2\u0187\u0188\13\2\2\2\u0188^\3\2\2\2\u0189\u018a"+
		"\13\2\2\2\u018a`\3\2\2\2\u018b\u018c\13\2\2\2\u018cb\3\2\2\2\33\2\u0100"+
		"\u010a\u011e\u0120\u0127\u012e\u0134\u013b\u0141\u0145\u014a\u0150\u0155"+
		"\u0157\u015c\u0161\u0164\u0169\u016e\u0173\u0175\u0179\u017e\u0180\3\b"+
		"\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}