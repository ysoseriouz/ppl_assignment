// Generated from BKIT.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BKITParser}.
 */
public interface BKITListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BKITParser#arraylit}.
	 * @param ctx the parse tree
	 */
	void enterArraylit(BKITParser.ArraylitContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#arraylit}.
	 * @param ctx the parse tree
	 */
	void exitArraylit(BKITParser.ArraylitContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#litlist}.
	 * @param ctx the parse tree
	 */
	void enterLitlist(BKITParser.LitlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#litlist}.
	 * @param ctx the parse tree
	 */
	void exitLitlist(BKITParser.LitlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(BKITParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(BKITParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(BKITParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(BKITParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#vardecl}.
	 * @param ctx the parse tree
	 */
	void enterVardecl(BKITParser.VardeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#vardecl}.
	 * @param ctx the parse tree
	 */
	void exitVardecl(BKITParser.VardeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#varlist}.
	 * @param ctx the parse tree
	 */
	void enterVarlist(BKITParser.VarlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#varlist}.
	 * @param ctx the parse tree
	 */
	void exitVarlist(BKITParser.VarlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(BKITParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(BKITParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#dim}.
	 * @param ctx the parse tree
	 */
	void enterDim(BKITParser.DimContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#dim}.
	 * @param ctx the parse tree
	 */
	void exitDim(BKITParser.DimContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#init}.
	 * @param ctx the parse tree
	 */
	void enterInit(BKITParser.InitContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#init}.
	 * @param ctx the parse tree
	 */
	void exitInit(BKITParser.InitContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#assignstmt}.
	 * @param ctx the parse tree
	 */
	void enterAssignstmt(BKITParser.AssignstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#assignstmt}.
	 * @param ctx the parse tree
	 */
	void exitAssignstmt(BKITParser.AssignstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#lhs}.
	 * @param ctx the parse tree
	 */
	void enterLhs(BKITParser.LhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#lhs}.
	 * @param ctx the parse tree
	 */
	void exitLhs(BKITParser.LhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#ifstmt}.
	 * @param ctx the parse tree
	 */
	void enterIfstmt(BKITParser.IfstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#ifstmt}.
	 * @param ctx the parse tree
	 */
	void exitIfstmt(BKITParser.IfstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#condblock}.
	 * @param ctx the parse tree
	 */
	void enterCondblock(BKITParser.CondblockContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#condblock}.
	 * @param ctx the parse tree
	 */
	void exitCondblock(BKITParser.CondblockContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#forstmt}.
	 * @param ctx the parse tree
	 */
	void enterForstmt(BKITParser.ForstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#forstmt}.
	 * @param ctx the parse tree
	 */
	void exitForstmt(BKITParser.ForstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#iterblock}.
	 * @param ctx the parse tree
	 */
	void enterIterblock(BKITParser.IterblockContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#iterblock}.
	 * @param ctx the parse tree
	 */
	void exitIterblock(BKITParser.IterblockContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#iterinit}.
	 * @param ctx the parse tree
	 */
	void enterIterinit(BKITParser.IterinitContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#iterinit}.
	 * @param ctx the parse tree
	 */
	void exitIterinit(BKITParser.IterinitContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#itercond}.
	 * @param ctx the parse tree
	 */
	void enterItercond(BKITParser.ItercondContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#itercond}.
	 * @param ctx the parse tree
	 */
	void exitItercond(BKITParser.ItercondContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#iterupdate}.
	 * @param ctx the parse tree
	 */
	void enterIterupdate(BKITParser.IterupdateContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#iterupdate}.
	 * @param ctx the parse tree
	 */
	void exitIterupdate(BKITParser.IterupdateContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#whilestmt}.
	 * @param ctx the parse tree
	 */
	void enterWhilestmt(BKITParser.WhilestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#whilestmt}.
	 * @param ctx the parse tree
	 */
	void exitWhilestmt(BKITParser.WhilestmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#dowhilestmt}.
	 * @param ctx the parse tree
	 */
	void enterDowhilestmt(BKITParser.DowhilestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#dowhilestmt}.
	 * @param ctx the parse tree
	 */
	void exitDowhilestmt(BKITParser.DowhilestmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#breakstmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakstmt(BKITParser.BreakstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#breakstmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakstmt(BKITParser.BreakstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#continuestmt}.
	 * @param ctx the parse tree
	 */
	void enterContinuestmt(BKITParser.ContinuestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#continuestmt}.
	 * @param ctx the parse tree
	 */
	void exitContinuestmt(BKITParser.ContinuestmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#callstmt}.
	 * @param ctx the parse tree
	 */
	void enterCallstmt(BKITParser.CallstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#callstmt}.
	 * @param ctx the parse tree
	 */
	void exitCallstmt(BKITParser.CallstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#returnstmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnstmt(BKITParser.ReturnstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#returnstmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnstmt(BKITParser.ReturnstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#stmtlist}.
	 * @param ctx the parse tree
	 */
	void enterStmtlist(BKITParser.StmtlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#stmtlist}.
	 * @param ctx the parse tree
	 */
	void exitStmtlist(BKITParser.StmtlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(BKITParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(BKITParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#funcdecl}.
	 * @param ctx the parse tree
	 */
	void enterFuncdecl(BKITParser.FuncdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#funcdecl}.
	 * @param ctx the parse tree
	 */
	void exitFuncdecl(BKITParser.FuncdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#paramdecl}.
	 * @param ctx the parse tree
	 */
	void enterParamdecl(BKITParser.ParamdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#paramdecl}.
	 * @param ctx the parse tree
	 */
	void exitParamdecl(BKITParser.ParamdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#paramlist}.
	 * @param ctx the parse tree
	 */
	void enterParamlist(BKITParser.ParamlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#paramlist}.
	 * @param ctx the parse tree
	 */
	void exitParamlist(BKITParser.ParamlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(BKITParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(BKITParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#bodydecl}.
	 * @param ctx the parse tree
	 */
	void enterBodydecl(BKITParser.BodydeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#bodydecl}.
	 * @param ctx the parse tree
	 */
	void exitBodydecl(BKITParser.BodydeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#call}.
	 * @param ctx the parse tree
	 */
	void enterCall(BKITParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#call}.
	 * @param ctx the parse tree
	 */
	void exitCall(BKITParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(BKITParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(BKITParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#relexpr}.
	 * @param ctx the parse tree
	 */
	void enterRelexpr(BKITParser.RelexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#relexpr}.
	 * @param ctx the parse tree
	 */
	void exitRelexpr(BKITParser.RelexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#operand}.
	 * @param ctx the parse tree
	 */
	void enterOperand(BKITParser.OperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#operand}.
	 * @param ctx the parse tree
	 */
	void exitOperand(BKITParser.OperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exprlist}.
	 * @param ctx the parse tree
	 */
	void enterExprlist(BKITParser.ExprlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exprlist}.
	 * @param ctx the parse tree
	 */
	void exitExprlist(BKITParser.ExprlistContext ctx);
}