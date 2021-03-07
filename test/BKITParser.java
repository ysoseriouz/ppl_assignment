// Generated from BKIT.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, BODY=13, BREAK=14, CONTINUE=15, DO=16, ELSE=17, 
		ELSEIF=18, ENDBODY=19, ENDIF=20, ENDFOR=21, ENDWHILE=22, FOR=23, FUNCTION=24, 
		IF=25, PARAMETER=26, RETURN=27, THEN=28, VAR=29, WHILE=30, ENDDO=31, WS=32, 
		CMT=33, EQ=34, LP=35, RP=36, LS=37, RS=38, LB=39, RB=40, COLON=41, DOT=42, 
		COMMA=43, SEMI=44, RELOP=45, ID=46, INTLIT=47, FLOATLIT=48, BOOLLIT=49, 
		STRINGLIT=50, UNCLOSE_STRING=51, ILLEGAL_ESCAPE=52, UNTERMINATED_COMMENT=53, 
		ERROR_CHAR=54;
	public static final int
		RULE_arraylit = 0, RULE_litlist = 1, RULE_literal = 2, RULE_program = 3, 
		RULE_vardecl = 4, RULE_varlist = 5, RULE_variable = 6, RULE_dim = 7, RULE_init = 8, 
		RULE_assignstmt = 9, RULE_lhs = 10, RULE_ifstmt = 11, RULE_condblock = 12, 
		RULE_forstmt = 13, RULE_iterblock = 14, RULE_iterinit = 15, RULE_itercond = 16, 
		RULE_iterupdate = 17, RULE_whilestmt = 18, RULE_dowhilestmt = 19, RULE_breakstmt = 20, 
		RULE_continuestmt = 21, RULE_callstmt = 22, RULE_returnstmt = 23, RULE_stmtlist = 24, 
		RULE_stmt = 25, RULE_funcdecl = 26, RULE_paramdecl = 27, RULE_paramlist = 28, 
		RULE_param = 29, RULE_bodydecl = 30, RULE_call = 31, RULE_expr = 32, RULE_relexpr = 33, 
		RULE_operand = 34, RULE_exprlist = 35;
	private static String[] makeRuleNames() {
		return new String[] {
			"arraylit", "litlist", "literal", "program", "vardecl", "varlist", "variable", 
			"dim", "init", "assignstmt", "lhs", "ifstmt", "condblock", "forstmt", 
			"iterblock", "iterinit", "itercond", "iterupdate", "whilestmt", "dowhilestmt", 
			"breakstmt", "continuestmt", "callstmt", "returnstmt", "stmtlist", "stmt", 
			"funcdecl", "paramdecl", "paramlist", "param", "bodydecl", "call", "expr", 
			"relexpr", "operand", "exprlist"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'-'", "'-.'", "'!'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'+'", 
			"'+.'", "'&&'", "'||'", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
			"'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", 
			"'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
			"'EndDo'", null, null, "'='", "'('", "')'", "'['", "']'", "'{'", "'}'", 
			"':'", "'.'", "','", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
			"ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
			"RETURN", "THEN", "VAR", "WHILE", "ENDDO", "WS", "CMT", "EQ", "LP", "RP", 
			"LS", "RS", "LB", "RB", "COLON", "DOT", "COMMA", "SEMI", "RELOP", "ID", 
			"INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
			"UNTERMINATED_COMMENT", "ERROR_CHAR"
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
	public String getGrammarFileName() { return "BKIT.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKITParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ArraylitContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKITParser.LB, 0); }
		public LitlistContext litlist() {
			return getRuleContext(LitlistContext.class,0);
		}
		public TerminalNode RB() { return getToken(BKITParser.RB, 0); }
		public ArraylitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arraylit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterArraylit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitArraylit(this);
		}
	}

	public final ArraylitContext arraylit() throws RecognitionException {
		ArraylitContext _localctx = new ArraylitContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_arraylit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(LB);
			setState(73);
			litlist();
			setState(74);
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
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public LitlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_litlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterLitlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitLitlist(this);
		}
	}

	public final LitlistContext litlist() throws RecognitionException {
		LitlistContext _localctx = new LitlistContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_litlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			literal();
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(77);
				match(COMMA);
				setState(78);
				literal();
				}
				}
				setState(83);
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
		public TerminalNode FLOATLIT() { return getToken(BKITParser.FLOATLIT, 0); }
		public TerminalNode INTLIT() { return getToken(BKITParser.INTLIT, 0); }
		public TerminalNode BOOLLIT() { return getToken(BKITParser.BOOLLIT, 0); }
		public TerminalNode STRINGLIT() { return getToken(BKITParser.STRINGLIT, 0); }
		public ArraylitContext arraylit() {
			return getRuleContext(ArraylitContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitLiteral(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_literal);
		try {
			setState(89);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FLOATLIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				match(FLOATLIT);
				}
				break;
			case INTLIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				match(INTLIT);
				}
				break;
			case BOOLLIT:
				enterOuterAlt(_localctx, 3);
				{
				setState(86);
				match(BOOLLIT);
				}
				break;
			case STRINGLIT:
				enterOuterAlt(_localctx, 4);
				{
				setState(87);
				match(STRINGLIT);
				}
				break;
			case LB:
				enterOuterAlt(_localctx, 5);
				{
				setState(88);
				arraylit();
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
		public TerminalNode EOF() { return getToken(BKITParser.EOF, 0); }
		public List<VardeclContext> vardecl() {
			return getRuleContexts(VardeclContext.class);
		}
		public VardeclContext vardecl(int i) {
			return getRuleContext(VardeclContext.class,i);
		}
		public List<FuncdeclContext> funcdecl() {
			return getRuleContexts(FuncdeclContext.class);
		}
		public FuncdeclContext funcdecl(int i) {
			return getRuleContext(FuncdeclContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(91);
				vardecl();
				}
				}
				setState(96);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(100);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION) {
				{
				{
				setState(97);
				funcdecl();
				}
				}
				setState(102);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(103);
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

	public static class VardeclContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BKITParser.VAR, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public VarlistContext varlist() {
			return getRuleContext(VarlistContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public VardeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVardecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVardecl(this);
		}
	}

	public final VardeclContext vardecl() throws RecognitionException {
		VardeclContext _localctx = new VardeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_vardecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			match(VAR);
			setState(106);
			match(COLON);
			setState(107);
			varlist();
			setState(108);
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
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public VarlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVarlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVarlist(this);
		}
	}

	public final VarlistContext varlist() throws RecognitionException {
		VarlistContext _localctx = new VarlistContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_varlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			variable();
			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(111);
				match(COMMA);
				setState(112);
				variable();
				}
				}
				setState(117);
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
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public List<DimContext> dim() {
			return getRuleContexts(DimContext.class);
		}
		public DimContext dim(int i) {
			return getRuleContext(DimContext.class,i);
		}
		public TerminalNode EQ() { return getToken(BKITParser.EQ, 0); }
		public InitContext init() {
			return getRuleContext(InitContext.class,0);
		}
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVariable(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_variable);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(ID);
			setState(122);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LS) {
				{
				{
				setState(119);
				dim();
				}
				}
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(127);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQ) {
				{
				setState(125);
				match(EQ);
				setState(126);
				init();
				}
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
		public TerminalNode LS() { return getToken(BKITParser.LS, 0); }
		public TerminalNode INTLIT() { return getToken(BKITParser.INTLIT, 0); }
		public TerminalNode RS() { return getToken(BKITParser.RS, 0); }
		public DimContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dim; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterDim(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitDim(this);
		}
	}

	public final DimContext dim() throws RecognitionException {
		DimContext _localctx = new DimContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_dim);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(LS);
			setState(130);
			match(INTLIT);
			setState(131);
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

	public static class InitContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public InitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitInit(this);
		}
	}

	public final InitContext init() throws RecognitionException {
		InitContext _localctx = new InitContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			literal();
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

	public static class AssignstmtContext extends ParserRuleContext {
		public LhsContext lhs() {
			return getRuleContext(LhsContext.class,0);
		}
		public TerminalNode EQ() { return getToken(BKITParser.EQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public AssignstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterAssignstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitAssignstmt(this);
		}
	}

	public final AssignstmtContext assignstmt() throws RecognitionException {
		AssignstmtContext _localctx = new AssignstmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_assignstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			lhs();
			setState(136);
			match(EQ);
			setState(137);
			expr();
			setState(138);
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

	public static class LhsContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> LS() { return getTokens(BKITParser.LS); }
		public TerminalNode LS(int i) {
			return getToken(BKITParser.LS, i);
		}
		public List<TerminalNode> RS() { return getTokens(BKITParser.RS); }
		public TerminalNode RS(int i) {
			return getToken(BKITParser.RS, i);
		}
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public LhsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterLhs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitLhs(this);
		}
	}

	public final LhsContext lhs() throws RecognitionException {
		LhsContext _localctx = new LhsContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_lhs);
		int _la;
		try {
			setState(150);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				expr();
				setState(145); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(141);
					match(LS);
					setState(142);
					expr();
					setState(143);
					match(RS);
					}
					}
					setState(147); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==LS );
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(149);
				match(ID);
				}
				break;
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

	public static class IfstmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BKITParser.IF, 0); }
		public List<CondblockContext> condblock() {
			return getRuleContexts(CondblockContext.class);
		}
		public CondblockContext condblock(int i) {
			return getRuleContext(CondblockContext.class,i);
		}
		public TerminalNode ENDIF() { return getToken(BKITParser.ENDIF, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public List<TerminalNode> ELSEIF() { return getTokens(BKITParser.ELSEIF); }
		public TerminalNode ELSEIF(int i) {
			return getToken(BKITParser.ELSEIF, i);
		}
		public TerminalNode ELSE() { return getToken(BKITParser.ELSE, 0); }
		public StmtlistContext stmtlist() {
			return getRuleContext(StmtlistContext.class,0);
		}
		public IfstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterIfstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitIfstmt(this);
		}
	}

	public final IfstmtContext ifstmt() throws RecognitionException {
		IfstmtContext _localctx = new IfstmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_ifstmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(IF);
			setState(153);
			condblock();
			setState(158);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(154);
				match(ELSEIF);
				setState(155);
				condblock();
				}
				}
				setState(160);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(163);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(161);
				match(ELSE);
				setState(162);
				stmtlist();
				}
			}

			setState(165);
			match(ENDIF);
			setState(166);
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

	public static class CondblockContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode THEN() { return getToken(BKITParser.THEN, 0); }
		public StmtlistContext stmtlist() {
			return getRuleContext(StmtlistContext.class,0);
		}
		public CondblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condblock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterCondblock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitCondblock(this);
		}
	}

	public final CondblockContext condblock() throws RecognitionException {
		CondblockContext _localctx = new CondblockContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_condblock);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			expr();
			setState(169);
			match(THEN);
			setState(170);
			stmtlist();
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

	public static class ForstmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(BKITParser.FOR, 0); }
		public TerminalNode LP() { return getToken(BKITParser.LP, 0); }
		public IterblockContext iterblock() {
			return getRuleContext(IterblockContext.class,0);
		}
		public TerminalNode RP() { return getToken(BKITParser.RP, 0); }
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public StmtlistContext stmtlist() {
			return getRuleContext(StmtlistContext.class,0);
		}
		public TerminalNode ENDFOR() { return getToken(BKITParser.ENDFOR, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public ForstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterForstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitForstmt(this);
		}
	}

	public final ForstmtContext forstmt() throws RecognitionException {
		ForstmtContext _localctx = new ForstmtContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_forstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(FOR);
			setState(173);
			match(LP);
			setState(174);
			iterblock();
			setState(175);
			match(RP);
			setState(176);
			match(DO);
			setState(177);
			stmtlist();
			setState(178);
			match(ENDFOR);
			setState(179);
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

	public static class IterblockContext extends ParserRuleContext {
		public IterinitContext iterinit() {
			return getRuleContext(IterinitContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public ItercondContext itercond() {
			return getRuleContext(ItercondContext.class,0);
		}
		public IterupdateContext iterupdate() {
			return getRuleContext(IterupdateContext.class,0);
		}
		public IterblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iterblock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterIterblock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitIterblock(this);
		}
	}

	public final IterblockContext iterblock() throws RecognitionException {
		IterblockContext _localctx = new IterblockContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_iterblock);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			iterinit();
			setState(182);
			match(COMMA);
			setState(183);
			itercond();
			setState(184);
			match(COMMA);
			setState(185);
			iterupdate();
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

	public static class IterinitContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode EQ() { return getToken(BKITParser.EQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public IterinitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iterinit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterIterinit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitIterinit(this);
		}
	}

	public final IterinitContext iterinit() throws RecognitionException {
		IterinitContext _localctx = new IterinitContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_iterinit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			match(ID);
			setState(188);
			match(EQ);
			setState(189);
			expr();
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

	public static class ItercondContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ItercondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_itercond; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterItercond(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitItercond(this);
		}
	}

	public final ItercondContext itercond() throws RecognitionException {
		ItercondContext _localctx = new ItercondContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_itercond);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			expr();
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

	public static class IterupdateContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public IterupdateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iterupdate; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterIterupdate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitIterupdate(this);
		}
	}

	public final IterupdateContext iterupdate() throws RecognitionException {
		IterupdateContext _localctx = new IterupdateContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_iterupdate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			expr();
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

	public static class WhilestmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(BKITParser.WHILE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public StmtlistContext stmtlist() {
			return getRuleContext(StmtlistContext.class,0);
		}
		public TerminalNode ENDWHILE() { return getToken(BKITParser.ENDWHILE, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public WhilestmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whilestmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterWhilestmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitWhilestmt(this);
		}
	}

	public final WhilestmtContext whilestmt() throws RecognitionException {
		WhilestmtContext _localctx = new WhilestmtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_whilestmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			match(WHILE);
			setState(196);
			expr();
			setState(197);
			match(DO);
			setState(198);
			stmtlist();
			setState(199);
			match(ENDWHILE);
			setState(200);
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

	public static class DowhilestmtContext extends ParserRuleContext {
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public StmtlistContext stmtlist() {
			return getRuleContext(StmtlistContext.class,0);
		}
		public TerminalNode WHILE() { return getToken(BKITParser.WHILE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ENDDO() { return getToken(BKITParser.ENDDO, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public DowhilestmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dowhilestmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterDowhilestmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitDowhilestmt(this);
		}
	}

	public final DowhilestmtContext dowhilestmt() throws RecognitionException {
		DowhilestmtContext _localctx = new DowhilestmtContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_dowhilestmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(DO);
			setState(203);
			stmtlist();
			setState(204);
			match(WHILE);
			setState(205);
			expr();
			setState(206);
			match(ENDDO);
			setState(207);
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

	public static class BreakstmtContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(BKITParser.BREAK, 0); }
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public BreakstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterBreakstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitBreakstmt(this);
		}
	}

	public final BreakstmtContext breakstmt() throws RecognitionException {
		BreakstmtContext _localctx = new BreakstmtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_breakstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			match(BREAK);
			setState(210);
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

	public static class ContinuestmtContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(BKITParser.CONTINUE, 0); }
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public ContinuestmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continuestmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterContinuestmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitContinuestmt(this);
		}
	}

	public final ContinuestmtContext continuestmt() throws RecognitionException {
		ContinuestmtContext _localctx = new ContinuestmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_continuestmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			match(CONTINUE);
			setState(213);
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

	public static class CallstmtContext extends ParserRuleContext {
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public CallstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterCallstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitCallstmt(this);
		}
	}

	public final CallstmtContext callstmt() throws RecognitionException {
		CallstmtContext _localctx = new CallstmtContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_callstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215);
			call();
			setState(216);
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

	public static class ReturnstmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(BKITParser.RETURN, 0); }
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ReturnstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterReturnstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitReturnstmt(this);
		}
	}

	public final ReturnstmtContext returnstmt() throws RecognitionException {
		ReturnstmtContext _localctx = new ReturnstmtContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_returnstmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			match(RETURN);
			setState(220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << LP) | (1L << LB) | (1L << ID) | (1L << INTLIT) | (1L << FLOATLIT) | (1L << BOOLLIT) | (1L << STRINGLIT))) != 0)) {
				{
				setState(219);
				expr();
				}
			}

			setState(222);
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

	public static class StmtlistContext extends ParserRuleContext {
		public List<VardeclContext> vardecl() {
			return getRuleContexts(VardeclContext.class);
		}
		public VardeclContext vardecl(int i) {
			return getRuleContext(VardeclContext.class,i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public StmtlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmtlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterStmtlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitStmtlist(this);
		}
	}

	public final StmtlistContext stmtlist() throws RecognitionException {
		StmtlistContext _localctx = new StmtlistContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_stmtlist);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(227);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(224);
				vardecl();
				}
				}
				setState(229);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(233);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(230);
					stmt();
					}
					} 
				}
				setState(235);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
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

	public static class StmtContext extends ParserRuleContext {
		public AssignstmtContext assignstmt() {
			return getRuleContext(AssignstmtContext.class,0);
		}
		public IfstmtContext ifstmt() {
			return getRuleContext(IfstmtContext.class,0);
		}
		public ForstmtContext forstmt() {
			return getRuleContext(ForstmtContext.class,0);
		}
		public WhilestmtContext whilestmt() {
			return getRuleContext(WhilestmtContext.class,0);
		}
		public DowhilestmtContext dowhilestmt() {
			return getRuleContext(DowhilestmtContext.class,0);
		}
		public BreakstmtContext breakstmt() {
			return getRuleContext(BreakstmtContext.class,0);
		}
		public ContinuestmtContext continuestmt() {
			return getRuleContext(ContinuestmtContext.class,0);
		}
		public CallstmtContext callstmt() {
			return getRuleContext(CallstmtContext.class,0);
		}
		public ReturnstmtContext returnstmt() {
			return getRuleContext(ReturnstmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitStmt(this);
		}
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_stmt);
		try {
			setState(245);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(236);
				assignstmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(237);
				ifstmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(238);
				forstmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(239);
				whilestmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(240);
				dowhilestmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(241);
				breakstmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(242);
				continuestmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(243);
				callstmt();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(244);
				returnstmt();
				}
				break;
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

	public static class FuncdeclContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(BKITParser.FUNCTION, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public BodydeclContext bodydecl() {
			return getRuleContext(BodydeclContext.class,0);
		}
		public ParamdeclContext paramdecl() {
			return getRuleContext(ParamdeclContext.class,0);
		}
		public FuncdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFuncdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFuncdecl(this);
		}
	}

	public final FuncdeclContext funcdecl() throws RecognitionException {
		FuncdeclContext _localctx = new FuncdeclContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_funcdecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			match(FUNCTION);
			setState(248);
			match(COLON);
			setState(249);
			match(ID);
			setState(251);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETER) {
				{
				setState(250);
				paramdecl();
				}
			}

			setState(253);
			bodydecl();
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

	public static class ParamdeclContext extends ParserRuleContext {
		public TerminalNode PARAMETER() { return getToken(BKITParser.PARAMETER, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public ParamlistContext paramlist() {
			return getRuleContext(ParamlistContext.class,0);
		}
		public ParamdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterParamdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitParamdecl(this);
		}
	}

	public final ParamdeclContext paramdecl() throws RecognitionException {
		ParamdeclContext _localctx = new ParamdeclContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_paramdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(255);
			match(PARAMETER);
			setState(256);
			match(COLON);
			setState(257);
			paramlist();
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

	public static class ParamlistContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public ParamlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterParamlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitParamlist(this);
		}
	}

	public final ParamlistContext paramlist() throws RecognitionException {
		ParamlistContext _localctx = new ParamlistContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_paramlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(259);
			param();
			setState(264);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(260);
				match(COMMA);
				setState(261);
				param();
				}
				}
				setState(266);
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

	public static class ParamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public List<DimContext> dim() {
			return getRuleContexts(DimContext.class);
		}
		public DimContext dim(int i) {
			return getRuleContext(DimContext.class,i);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterParam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitParam(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_param);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(ID);
			setState(271);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LS) {
				{
				{
				setState(268);
				dim();
				}
				}
				setState(273);
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

	public static class BodydeclContext extends ParserRuleContext {
		public TerminalNode BODY() { return getToken(BKITParser.BODY, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public StmtlistContext stmtlist() {
			return getRuleContext(StmtlistContext.class,0);
		}
		public TerminalNode ENDBODY() { return getToken(BKITParser.ENDBODY, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public BodydeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bodydecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterBodydecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitBodydecl(this);
		}
	}

	public final BodydeclContext bodydecl() throws RecognitionException {
		BodydeclContext _localctx = new BodydeclContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_bodydecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(274);
			match(BODY);
			setState(275);
			match(COLON);
			setState(276);
			stmtlist();
			setState(277);
			match(ENDBODY);
			setState(278);
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

	public static class CallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode LP() { return getToken(BKITParser.LP, 0); }
		public TerminalNode RP() { return getToken(BKITParser.RP, 0); }
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitCall(this);
		}
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			match(ID);
			setState(281);
			match(LP);
			setState(283);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << LP) | (1L << LB) | (1L << ID) | (1L << INTLIT) | (1L << FLOATLIT) | (1L << BOOLLIT) | (1L << STRINGLIT))) != 0)) {
				{
				setState(282);
				exprlist();
				}
			}

			setState(285);
			match(RP);
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

	public static class ExprContext extends ParserRuleContext {
		public List<RelexprContext> relexpr() {
			return getRuleContexts(RelexprContext.class);
		}
		public RelexprContext relexpr(int i) {
			return getRuleContext(RelexprContext.class,i);
		}
		public TerminalNode RELOP() { return getToken(BKITParser.RELOP, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_expr);
		try {
			setState(292);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(287);
				relexpr(0);
				setState(288);
				match(RELOP);
				setState(289);
				relexpr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(291);
				relexpr(0);
				}
				break;
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

	public static class RelexprContext extends ParserRuleContext {
		public List<RelexprContext> relexpr() {
			return getRuleContexts(RelexprContext.class);
		}
		public RelexprContext relexpr(int i) {
			return getRuleContext(RelexprContext.class,i);
		}
		public OperandContext operand() {
			return getRuleContext(OperandContext.class,0);
		}
		public List<TerminalNode> LS() { return getTokens(BKITParser.LS); }
		public TerminalNode LS(int i) {
			return getToken(BKITParser.LS, i);
		}
		public List<TerminalNode> RS() { return getTokens(BKITParser.RS); }
		public TerminalNode RS(int i) {
			return getToken(BKITParser.RS, i);
		}
		public RelexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relexpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterRelexpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitRelexpr(this);
		}
	}

	public final RelexprContext relexpr() throws RecognitionException {
		return relexpr(0);
	}

	private RelexprContext relexpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		RelexprContext _localctx = new RelexprContext(_ctx, _parentState);
		RelexprContext _prevctx = _localctx;
		int _startState = 66;
		enterRecursionRule(_localctx, 66, RULE_relexpr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
				{
				setState(295);
				_la = _input.LA(1);
				if ( !(_la==T__0 || _la==T__1) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(296);
				relexpr(6);
				}
				break;
			case T__2:
				{
				setState(297);
				match(T__2);
				setState(298);
				relexpr(5);
				}
				break;
			case LP:
			case LB:
			case ID:
			case INTLIT:
			case FLOATLIT:
			case BOOLLIT:
			case STRINGLIT:
				{
				setState(299);
				operand();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(322);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(320);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
					case 1:
						{
						_localctx = new RelexprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_relexpr);
						setState(302);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(303);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << T__6) | (1L << T__7))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(304);
						relexpr(5);
						}
						break;
					case 2:
						{
						_localctx = new RelexprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_relexpr);
						setState(305);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(306);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__8) | (1L << T__9))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(307);
						relexpr(4);
						}
						break;
					case 3:
						{
						_localctx = new RelexprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_relexpr);
						setState(308);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(309);
						_la = _input.LA(1);
						if ( !(_la==T__10 || _la==T__11) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(310);
						relexpr(3);
						}
						break;
					case 4:
						{
						_localctx = new RelexprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_relexpr);
						setState(311);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(316); 
						_errHandler.sync(this);
						_alt = 1;
						do {
							switch (_alt) {
							case 1:
								{
								{
								setState(312);
								match(LS);
								setState(313);
								relexpr(0);
								setState(314);
								match(RS);
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							setState(318); 
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
						} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
						}
						break;
					}
					} 
				}
				setState(324);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class OperandContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(BKITParser.LP, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RP() { return getToken(BKITParser.RP, 0); }
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterOperand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitOperand(this);
		}
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_operand);
		try {
			setState(332);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(325);
				match(LP);
				setState(326);
				expr();
				setState(327);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(329);
				call();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(330);
				match(ID);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(331);
				literal();
				}
				break;
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

	public static class ExprlistContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public ExprlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExprlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExprlist(this);
		}
	}

	public final ExprlistContext exprlist() throws RecognitionException {
		ExprlistContext _localctx = new ExprlistContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_exprlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(334);
			expr();
			setState(339);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(335);
				match(COMMA);
				setState(336);
				expr();
				}
				}
				setState(341);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 33:
			return relexpr_sempred((RelexprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean relexpr_sempred(RelexprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 7);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38\u0159\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\3\2\3\2\3\2\3\3\3\3\3\3\7\3R\n\3\f\3"+
		"\16\3U\13\3\3\4\3\4\3\4\3\4\3\4\5\4\\\n\4\3\5\7\5_\n\5\f\5\16\5b\13\5"+
		"\3\5\7\5e\n\5\f\5\16\5h\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7"+
		"\7t\n\7\f\7\16\7w\13\7\3\b\3\b\7\b{\n\b\f\b\16\b~\13\b\3\b\3\b\5\b\u0082"+
		"\n\b\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f"+
		"\3\f\6\f\u0094\n\f\r\f\16\f\u0095\3\f\5\f\u0099\n\f\3\r\3\r\3\r\3\r\7"+
		"\r\u009f\n\r\f\r\16\r\u00a2\13\r\3\r\3\r\5\r\u00a6\n\r\3\r\3\r\3\r\3\16"+
		"\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26"+
		"\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\5\31\u00df\n\31\3\31\3\31"+
		"\3\32\7\32\u00e4\n\32\f\32\16\32\u00e7\13\32\3\32\7\32\u00ea\n\32\f\32"+
		"\16\32\u00ed\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u00f8"+
		"\n\33\3\34\3\34\3\34\3\34\5\34\u00fe\n\34\3\34\3\34\3\35\3\35\3\35\3\35"+
		"\3\36\3\36\3\36\7\36\u0109\n\36\f\36\16\36\u010c\13\36\3\37\3\37\7\37"+
		"\u0110\n\37\f\37\16\37\u0113\13\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\5!\u011e"+
		"\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u0127\n\"\3#\3#\3#\3#\3#\3#\5#\u012f"+
		"\n#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\6#\u013f\n#\r#\16#\u0140"+
		"\7#\u0143\n#\f#\16#\u0146\13#\3$\3$\3$\3$\3$\3$\3$\5$\u014f\n$\3%\3%\3"+
		"%\7%\u0154\n%\f%\16%\u0157\13%\3%\2\3D&\2\4\6\b\n\f\16\20\22\24\26\30"+
		"\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFH\2\6\3\2\3\4\3\2\6\n\4\2\3\4\13"+
		"\f\3\2\r\16\2\u015d\2J\3\2\2\2\4N\3\2\2\2\6[\3\2\2\2\b`\3\2\2\2\nk\3\2"+
		"\2\2\fp\3\2\2\2\16x\3\2\2\2\20\u0083\3\2\2\2\22\u0087\3\2\2\2\24\u0089"+
		"\3\2\2\2\26\u0098\3\2\2\2\30\u009a\3\2\2\2\32\u00aa\3\2\2\2\34\u00ae\3"+
		"\2\2\2\36\u00b7\3\2\2\2 \u00bd\3\2\2\2\"\u00c1\3\2\2\2$\u00c3\3\2\2\2"+
		"&\u00c5\3\2\2\2(\u00cc\3\2\2\2*\u00d3\3\2\2\2,\u00d6\3\2\2\2.\u00d9\3"+
		"\2\2\2\60\u00dc\3\2\2\2\62\u00e5\3\2\2\2\64\u00f7\3\2\2\2\66\u00f9\3\2"+
		"\2\28\u0101\3\2\2\2:\u0105\3\2\2\2<\u010d\3\2\2\2>\u0114\3\2\2\2@\u011a"+
		"\3\2\2\2B\u0126\3\2\2\2D\u012e\3\2\2\2F\u014e\3\2\2\2H\u0150\3\2\2\2J"+
		"K\7)\2\2KL\5\4\3\2LM\7*\2\2M\3\3\2\2\2NS\5\6\4\2OP\7-\2\2PR\5\6\4\2QO"+
		"\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\5\3\2\2\2US\3\2\2\2V\\\7\62\2"+
		"\2W\\\7\61\2\2X\\\7\63\2\2Y\\\7\64\2\2Z\\\5\2\2\2[V\3\2\2\2[W\3\2\2\2"+
		"[X\3\2\2\2[Y\3\2\2\2[Z\3\2\2\2\\\7\3\2\2\2]_\5\n\6\2^]\3\2\2\2_b\3\2\2"+
		"\2`^\3\2\2\2`a\3\2\2\2af\3\2\2\2b`\3\2\2\2ce\5\66\34\2dc\3\2\2\2eh\3\2"+
		"\2\2fd\3\2\2\2fg\3\2\2\2gi\3\2\2\2hf\3\2\2\2ij\7\2\2\3j\t\3\2\2\2kl\7"+
		"\37\2\2lm\7+\2\2mn\5\f\7\2no\7.\2\2o\13\3\2\2\2pu\5\16\b\2qr\7-\2\2rt"+
		"\5\16\b\2sq\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2v\r\3\2\2\2wu\3\2\2\2"+
		"x|\7\60\2\2y{\5\20\t\2zy\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\u0081"+
		"\3\2\2\2~|\3\2\2\2\177\u0080\7$\2\2\u0080\u0082\5\22\n\2\u0081\177\3\2"+
		"\2\2\u0081\u0082\3\2\2\2\u0082\17\3\2\2\2\u0083\u0084\7\'\2\2\u0084\u0085"+
		"\7\61\2\2\u0085\u0086\7(\2\2\u0086\21\3\2\2\2\u0087\u0088\5\6\4\2\u0088"+
		"\23\3\2\2\2\u0089\u008a\5\26\f\2\u008a\u008b\7$\2\2\u008b\u008c\5B\"\2"+
		"\u008c\u008d\7.\2\2\u008d\25\3\2\2\2\u008e\u0093\5B\"\2\u008f\u0090\7"+
		"\'\2\2\u0090\u0091\5B\"\2\u0091\u0092\7(\2\2\u0092\u0094\3\2\2\2\u0093"+
		"\u008f\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2"+
		"\2\2\u0096\u0099\3\2\2\2\u0097\u0099\7\60\2\2\u0098\u008e\3\2\2\2\u0098"+
		"\u0097\3\2\2\2\u0099\27\3\2\2\2\u009a\u009b\7\33\2\2\u009b\u00a0\5\32"+
		"\16\2\u009c\u009d\7\24\2\2\u009d\u009f\5\32\16\2\u009e\u009c\3\2\2\2\u009f"+
		"\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a5\3\2"+
		"\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4\7\23\2\2\u00a4\u00a6\5\62\32\2\u00a5"+
		"\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\7\26"+
		"\2\2\u00a8\u00a9\7,\2\2\u00a9\31\3\2\2\2\u00aa\u00ab\5B\"\2\u00ab\u00ac"+
		"\7\36\2\2\u00ac\u00ad\5\62\32\2\u00ad\33\3\2\2\2\u00ae\u00af\7\31\2\2"+
		"\u00af\u00b0\7%\2\2\u00b0\u00b1\5\36\20\2\u00b1\u00b2\7&\2\2\u00b2\u00b3"+
		"\7\22\2\2\u00b3\u00b4\5\62\32\2\u00b4\u00b5\7\27\2\2\u00b5\u00b6\7,\2"+
		"\2\u00b6\35\3\2\2\2\u00b7\u00b8\5 \21\2\u00b8\u00b9\7-\2\2\u00b9\u00ba"+
		"\5\"\22\2\u00ba\u00bb\7-\2\2\u00bb\u00bc\5$\23\2\u00bc\37\3\2\2\2\u00bd"+
		"\u00be\7\60\2\2\u00be\u00bf\7$\2\2\u00bf\u00c0\5B\"\2\u00c0!\3\2\2\2\u00c1"+
		"\u00c2\5B\"\2\u00c2#\3\2\2\2\u00c3\u00c4\5B\"\2\u00c4%\3\2\2\2\u00c5\u00c6"+
		"\7 \2\2\u00c6\u00c7\5B\"\2\u00c7\u00c8\7\22\2\2\u00c8\u00c9\5\62\32\2"+
		"\u00c9\u00ca\7\30\2\2\u00ca\u00cb\7,\2\2\u00cb\'\3\2\2\2\u00cc\u00cd\7"+
		"\22\2\2\u00cd\u00ce\5\62\32\2\u00ce\u00cf\7 \2\2\u00cf\u00d0\5B\"\2\u00d0"+
		"\u00d1\7!\2\2\u00d1\u00d2\7,\2\2\u00d2)\3\2\2\2\u00d3\u00d4\7\20\2\2\u00d4"+
		"\u00d5\7.\2\2\u00d5+\3\2\2\2\u00d6\u00d7\7\21\2\2\u00d7\u00d8\7.\2\2\u00d8"+
		"-\3\2\2\2\u00d9\u00da\5@!\2\u00da\u00db\7.\2\2\u00db/\3\2\2\2\u00dc\u00de"+
		"\7\35\2\2\u00dd\u00df\5B\"\2\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df"+
		"\u00e0\3\2\2\2\u00e0\u00e1\7.\2\2\u00e1\61\3\2\2\2\u00e2\u00e4\5\n\6\2"+
		"\u00e3\u00e2\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6"+
		"\3\2\2\2\u00e6\u00eb\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00ea\5\64\33\2"+
		"\u00e9\u00e8\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec"+
		"\3\2\2\2\u00ec\63\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f8\5\24\13\2\u00ef"+
		"\u00f8\5\30\r\2\u00f0\u00f8\5\34\17\2\u00f1\u00f8\5&\24\2\u00f2\u00f8"+
		"\5(\25\2\u00f3\u00f8\5*\26\2\u00f4\u00f8\5,\27\2\u00f5\u00f8\5.\30\2\u00f6"+
		"\u00f8\5\60\31\2\u00f7\u00ee\3\2\2\2\u00f7\u00ef\3\2\2\2\u00f7\u00f0\3"+
		"\2\2\2\u00f7\u00f1\3\2\2\2\u00f7\u00f2\3\2\2\2\u00f7\u00f3\3\2\2\2\u00f7"+
		"\u00f4\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8\65\3\2\2"+
		"\2\u00f9\u00fa\7\32\2\2\u00fa\u00fb\7+\2\2\u00fb\u00fd\7\60\2\2\u00fc"+
		"\u00fe\58\35\2\u00fd\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\3\2"+
		"\2\2\u00ff\u0100\5> \2\u0100\67\3\2\2\2\u0101\u0102\7\34\2\2\u0102\u0103"+
		"\7+\2\2\u0103\u0104\5:\36\2\u01049\3\2\2\2\u0105\u010a\5<\37\2\u0106\u0107"+
		"\7-\2\2\u0107\u0109\5<\37\2\u0108\u0106\3\2\2\2\u0109\u010c\3\2\2\2\u010a"+
		"\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b;\3\2\2\2\u010c\u010a\3\2\2\2"+
		"\u010d\u0111\7\60\2\2\u010e\u0110\5\20\t\2\u010f\u010e\3\2\2\2\u0110\u0113"+
		"\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112=\3\2\2\2\u0113"+
		"\u0111\3\2\2\2\u0114\u0115\7\17\2\2\u0115\u0116\7+\2\2\u0116\u0117\5\62"+
		"\32\2\u0117\u0118\7\25\2\2\u0118\u0119\7,\2\2\u0119?\3\2\2\2\u011a\u011b"+
		"\7\60\2\2\u011b\u011d\7%\2\2\u011c\u011e\5H%\2\u011d\u011c\3\2\2\2\u011d"+
		"\u011e\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\7&\2\2\u0120A\3\2\2\2\u0121"+
		"\u0122\5D#\2\u0122\u0123\7/\2\2\u0123\u0124\5D#\2\u0124\u0127\3\2\2\2"+
		"\u0125\u0127\5D#\2\u0126\u0121\3\2\2\2\u0126\u0125\3\2\2\2\u0127C\3\2"+
		"\2\2\u0128\u0129\b#\1\2\u0129\u012a\t\2\2\2\u012a\u012f\5D#\b\u012b\u012c"+
		"\7\5\2\2\u012c\u012f\5D#\7\u012d\u012f\5F$\2\u012e\u0128\3\2\2\2\u012e"+
		"\u012b\3\2\2\2\u012e\u012d\3\2\2\2\u012f\u0144\3\2\2\2\u0130\u0131\f\6"+
		"\2\2\u0131\u0132\t\3\2\2\u0132\u0143\5D#\7\u0133\u0134\f\5\2\2\u0134\u0135"+
		"\t\4\2\2\u0135\u0143\5D#\6\u0136\u0137\f\4\2\2\u0137\u0138\t\5\2\2\u0138"+
		"\u0143\5D#\5\u0139\u013e\f\t\2\2\u013a\u013b\7\'\2\2\u013b\u013c\5D#\2"+
		"\u013c\u013d\7(\2\2\u013d\u013f\3\2\2\2\u013e\u013a\3\2\2\2\u013f\u0140"+
		"\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0143\3\2\2\2\u0142"+
		"\u0130\3\2\2\2\u0142\u0133\3\2\2\2\u0142\u0136\3\2\2\2\u0142\u0139\3\2"+
		"\2\2\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145"+
		"E\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148\7%\2\2\u0148\u0149\5B\"\2\u0149"+
		"\u014a\7&\2\2\u014a\u014f\3\2\2\2\u014b\u014f\5@!\2\u014c\u014f\7\60\2"+
		"\2\u014d\u014f\5\6\4\2\u014e\u0147\3\2\2\2\u014e\u014b\3\2\2\2\u014e\u014c"+
		"\3\2\2\2\u014e\u014d\3\2\2\2\u014fG\3\2\2\2\u0150\u0155\5B\"\2\u0151\u0152"+
		"\7-\2\2\u0152\u0154\5B\"\2\u0153\u0151\3\2\2\2\u0154\u0157\3\2\2\2\u0155"+
		"\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156I\3\2\2\2\u0157\u0155\3\2\2\2"+
		"\34S[`fu|\u0081\u0095\u0098\u00a0\u00a5\u00de\u00e5\u00eb\u00f7\u00fd"+
		"\u010a\u0111\u011d\u0126\u012e\u0140\u0142\u0144\u014e\u0155";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}