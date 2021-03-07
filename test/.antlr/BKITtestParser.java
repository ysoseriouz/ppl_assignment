// Generated from /media/thanhnguyen2612/01D3670DD5838B40/Tien Thanh/HK201/Programming Languages/tutorial2/src/main/bkit/parser/test/BKITtest.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITtestParser extends Parser {
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
	public static final int
		RULE_array = 0, RULE_litlist = 1, RULE_literal = 2, RULE_program = 3, 
		RULE_globdecs = 4, RULE_funcdecs = 5, RULE_vardec = 6, RULE_varlist = 7, 
		RULE_variable = 8, RULE_dim = 9, RULE_initlist = 10, RULE_initvalue = 11, 
		RULE_funcdec = 12, RULE_paramdec = 13, RULE_bodydec = 14, RULE_stmtlist = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"array", "litlist", "literal", "program", "globdecs", "funcdecs", "vardec", 
			"varlist", "variable", "dim", "initlist", "initvalue", "funcdec", "paramdec", 
			"bodydec", "stmtlist"
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

	@Override
	public String getGrammarFileName() { return "BKITtest.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKITtestParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ArrayContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKITtestParser.LB, 0); }
		public LitlistContext litlist() {
			return getRuleContext(LitlistContext.class,0);
		}
		public TerminalNode RB() { return getToken(BKITtestParser.RB, 0); }
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_array);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(LB);
			setState(33);
			litlist();
			setState(34);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LitlistContext extends ParserRuleContext {
		public List<LiteralContext> literal() {
			return getRuleContexts(LiteralContext.class);
		}
		public LiteralContext literal(int i) {
			return getRuleContext(LiteralContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITtestParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITtestParser.COMMA, i);
		}
		public LitlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_litlist; }
	}

	public final LitlistContext litlist() throws RecognitionException {
		LitlistContext _localctx = new LitlistContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_litlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			literal();
			setState(41);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(37);
				match(COMMA);
				setState(38);
				literal();
				}
				}
				setState(43);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BKITtestParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(BKITtestParser.FLOAT, 0); }
		public TerminalNode BOOL() { return getToken(BKITtestParser.BOOL, 0); }
		public TerminalNode STRING() { return getToken(BKITtestParser.STRING, 0); }
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_literal);
		try {
			setState(49);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(44);
				match(INT);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(45);
				match(FLOAT);
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 3);
				{
				setState(46);
				match(BOOL);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(47);
				match(STRING);
				}
				break;
			case LB:
				enterOuterAlt(_localctx, 5);
				{
				setState(48);
				array();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProgramContext extends ParserRuleContext {
		public GlobdecsContext globdecs() {
			return getRuleContext(GlobdecsContext.class,0);
		}
		public TerminalNode EOF() { return getToken(BKITtestParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			globdecs();
			setState(52);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GlobdecsContext extends ParserRuleContext {
		public List<VardecContext> vardec() {
			return getRuleContexts(VardecContext.class);
		}
		public VardecContext vardec(int i) {
			return getRuleContext(VardecContext.class,i);
		}
		public GlobdecsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_globdecs; }
	}

	public final GlobdecsContext globdecs() throws RecognitionException {
		GlobdecsContext _localctx = new GlobdecsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_globdecs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(54);
				vardec();
				}
				}
				setState(59);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncdecsContext extends ParserRuleContext {
		public List<FuncdecContext> funcdec() {
			return getRuleContexts(FuncdecContext.class);
		}
		public FuncdecContext funcdec(int i) {
			return getRuleContext(FuncdecContext.class,i);
		}
		public FuncdecsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcdecs; }
	}

	public final FuncdecsContext funcdecs() throws RecognitionException {
		FuncdecsContext _localctx = new FuncdecsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_funcdecs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION) {
				{
				{
				setState(60);
				funcdec();
				}
				}
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VardecContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BKITtestParser.VAR, 0); }
		public TerminalNode COLON() { return getToken(BKITtestParser.COLON, 0); }
		public VarlistContext varlist() {
			return getRuleContext(VarlistContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITtestParser.SEMI, 0); }
		public TerminalNode EQ() { return getToken(BKITtestParser.EQ, 0); }
		public InitlistContext initlist() {
			return getRuleContext(InitlistContext.class,0);
		}
		public VardecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardec; }
	}

	public final VardecContext vardec() throws RecognitionException {
		VardecContext _localctx = new VardecContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_vardec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(VAR);
			setState(67);
			match(COLON);
			setState(68);
			varlist();
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQ) {
				{
				setState(69);
				match(EQ);
				setState(70);
				initlist();
				}
			}

			setState(73);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarlistContext extends ParserRuleContext {
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITtestParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITtestParser.COMMA, i);
		}
		public VarlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varlist; }
	}

	public final VarlistContext varlist() throws RecognitionException {
		VarlistContext _localctx = new VarlistContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_varlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			variable();
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(76);
				match(COMMA);
				setState(77);
				variable();
				}
				}
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITtestParser.ID, 0); }
		public List<DimContext> dim() {
			return getRuleContexts(DimContext.class);
		}
		public DimContext dim(int i) {
			return getRuleContext(DimContext.class,i);
		}
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_variable);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(ID);
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LS) {
				{
				{
				setState(84);
				dim();
				}
				}
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DimContext extends ParserRuleContext {
		public TerminalNode LS() { return getToken(BKITtestParser.LS, 0); }
		public TerminalNode INT() { return getToken(BKITtestParser.INT, 0); }
		public TerminalNode RS() { return getToken(BKITtestParser.RS, 0); }
		public DimContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dim; }
	}

	public final DimContext dim() throws RecognitionException {
		DimContext _localctx = new DimContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_dim);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(LS);
			setState(91);
			match(INT);
			setState(92);
			match(RS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitlistContext extends ParserRuleContext {
		public List<InitvalueContext> initvalue() {
			return getRuleContexts(InitvalueContext.class);
		}
		public InitvalueContext initvalue(int i) {
			return getRuleContext(InitvalueContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITtestParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITtestParser.COMMA, i);
		}
		public InitlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initlist; }
	}

	public final InitlistContext initlist() throws RecognitionException {
		InitlistContext _localctx = new InitlistContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_initlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			initvalue();
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(95);
				match(COMMA);
				setState(96);
				initvalue();
				}
				}
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitvalueContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode ID() { return getToken(BKITtestParser.ID, 0); }
		public InitvalueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initvalue; }
	}

	public final InitvalueContext initvalue() throws RecognitionException {
		InitvalueContext _localctx = new InitvalueContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_initvalue);
		try {
			setState(104);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LB:
			case INT:
			case FLOAT:
			case BOOL:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(102);
				literal();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(103);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncdecContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(BKITtestParser.FUNCTION, 0); }
		public TerminalNode COLON() { return getToken(BKITtestParser.COLON, 0); }
		public TerminalNode ID() { return getToken(BKITtestParser.ID, 0); }
		public BodydecContext bodydec() {
			return getRuleContext(BodydecContext.class,0);
		}
		public ParamdecContext paramdec() {
			return getRuleContext(ParamdecContext.class,0);
		}
		public FuncdecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcdec; }
	}

	public final FuncdecContext funcdec() throws RecognitionException {
		FuncdecContext _localctx = new FuncdecContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_funcdec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(FUNCTION);
			setState(107);
			match(COLON);
			setState(108);
			match(ID);
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETER) {
				{
				setState(109);
				paramdec();
				}
			}

			setState(112);
			bodydec();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamdecContext extends ParserRuleContext {
		public TerminalNode PARAMETER() { return getToken(BKITtestParser.PARAMETER, 0); }
		public TerminalNode COLON() { return getToken(BKITtestParser.COLON, 0); }
		public VarlistContext varlist() {
			return getRuleContext(VarlistContext.class,0);
		}
		public ParamdecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramdec; }
	}

	public final ParamdecContext paramdec() throws RecognitionException {
		ParamdecContext _localctx = new ParamdecContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_paramdec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(PARAMETER);
			setState(115);
			match(COLON);
			setState(116);
			varlist();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BodydecContext extends ParserRuleContext {
		public TerminalNode BODY() { return getToken(BKITtestParser.BODY, 0); }
		public TerminalNode COLON() { return getToken(BKITtestParser.COLON, 0); }
		public TerminalNode ENDBODY() { return getToken(BKITtestParser.ENDBODY, 0); }
		public TerminalNode DOT() { return getToken(BKITtestParser.DOT, 0); }
		public StmtlistContext stmtlist() {
			return getRuleContext(StmtlistContext.class,0);
		}
		public BodydecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bodydec; }
	}

	public final BodydecContext bodydec() throws RecognitionException {
		BodydecContext _localctx = new BodydecContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_bodydec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(BODY);
			setState(119);
			match(COLON);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(120);
				stmtlist();
				}
			}

			setState(123);
			match(ENDBODY);
			setState(124);
			match(DOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtlistContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITtestParser.ID, 0); }
		public TerminalNode EQ() { return getToken(BKITtestParser.EQ, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITtestParser.SEMI, 0); }
		public StmtlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmtlist; }
	}

	public final StmtlistContext stmtlist() throws RecognitionException {
		StmtlistContext _localctx = new StmtlistContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_stmtlist);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(ID);
			setState(127);
			match(EQ);
			setState(128);
			literal();
			setState(129);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3.\u0086\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3"+
		"\2\3\2\3\3\3\3\3\3\7\3*\n\3\f\3\16\3-\13\3\3\4\3\4\3\4\3\4\3\4\5\4\64"+
		"\n\4\3\5\3\5\3\5\3\6\7\6:\n\6\f\6\16\6=\13\6\3\7\7\7@\n\7\f\7\16\7C\13"+
		"\7\3\b\3\b\3\b\3\b\3\b\5\bJ\n\b\3\b\3\b\3\t\3\t\3\t\7\tQ\n\t\f\t\16\t"+
		"T\13\t\3\n\3\n\7\nX\n\n\f\n\16\n[\13\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f"+
		"\7\fd\n\f\f\f\16\fg\13\f\3\r\3\r\5\rk\n\r\3\16\3\16\3\16\3\16\5\16q\n"+
		"\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\5\20|\n\20\3\20\3\20"+
		"\3\20\3\21\3\21\3\21\3\21\3\21\3\21\2\2\22\2\4\6\b\n\f\16\20\22\24\26"+
		"\30\32\34\36 \2\2\2\u0083\2\"\3\2\2\2\4&\3\2\2\2\6\63\3\2\2\2\b\65\3\2"+
		"\2\2\n;\3\2\2\2\fA\3\2\2\2\16D\3\2\2\2\20M\3\2\2\2\22U\3\2\2\2\24\\\3"+
		"\2\2\2\26`\3\2\2\2\30j\3\2\2\2\32l\3\2\2\2\34t\3\2\2\2\36x\3\2\2\2 \u0080"+
		"\3\2\2\2\"#\7\35\2\2#$\5\4\3\2$%\7\36\2\2%\3\3\2\2\2&+\5\6\4\2\'(\7!\2"+
		"\2(*\5\6\4\2)\'\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\5\3\2\2\2-+\3\2"+
		"\2\2.\64\7\'\2\2/\64\7(\2\2\60\64\7)\2\2\61\64\7*\2\2\62\64\5\2\2\2\63"+
		".\3\2\2\2\63/\3\2\2\2\63\60\3\2\2\2\63\61\3\2\2\2\63\62\3\2\2\2\64\7\3"+
		"\2\2\2\65\66\5\n\6\2\66\67\7\2\2\3\67\t\3\2\2\28:\5\16\b\298\3\2\2\2:"+
		"=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<\13\3\2\2\2=;\3\2\2\2>@\5\32\16\2?>\3\2"+
		"\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\r\3\2\2\2CA\3\2\2\2DE\7\23\2\2EF\7"+
		"\37\2\2FI\5\20\t\2GH\7\30\2\2HJ\5\26\f\2IG\3\2\2\2IJ\3\2\2\2JK\3\2\2\2"+
		"KL\7\"\2\2L\17\3\2\2\2MR\5\22\n\2NO\7!\2\2OQ\5\22\n\2PN\3\2\2\2QT\3\2"+
		"\2\2RP\3\2\2\2RS\3\2\2\2S\21\3\2\2\2TR\3\2\2\2UY\7&\2\2VX\5\24\13\2WV"+
		"\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\23\3\2\2\2[Y\3\2\2\2\\]\7\33\2"+
		"\2]^\7\'\2\2^_\7\34\2\2_\25\3\2\2\2`e\5\30\r\2ab\7!\2\2bd\5\30\r\2ca\3"+
		"\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\27\3\2\2\2ge\3\2\2\2hk\5\6\4\2i"+
		"k\7&\2\2jh\3\2\2\2ji\3\2\2\2k\31\3\2\2\2lm\7\16\2\2mn\7\37\2\2np\7&\2"+
		"\2oq\5\34\17\2po\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\5\36\20\2s\33\3\2\2\2t"+
		"u\7\20\2\2uv\7\37\2\2vw\5\20\t\2w\35\3\2\2\2xy\7\3\2\2y{\7\37\2\2z|\5"+
		" \21\2{z\3\2\2\2{|\3\2\2\2|}\3\2\2\2}~\7\t\2\2~\177\7 \2\2\177\37\3\2"+
		"\2\2\u0080\u0081\7&\2\2\u0081\u0082\7\30\2\2\u0082\u0083\5\6\4\2\u0083"+
		"\u0084\7\"\2\2\u0084!\3\2\2\2\r+\63;AIRYejp{";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}