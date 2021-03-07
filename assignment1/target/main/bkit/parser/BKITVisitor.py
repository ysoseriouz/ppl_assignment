# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#arraylit.
    def visitArraylit(self, ctx:BKITParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#litlist.
    def visitLitlist(self, ctx:BKITParser.LitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#globdecs.
    def visitGlobdecs(self, ctx:BKITParser.GlobdecsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcdecs.
    def visitFuncdecs(self, ctx:BKITParser.FuncdecsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardec.
    def visitVardec(self, ctx:BKITParser.VardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varlist.
    def visitVarlist(self, ctx:BKITParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dim.
    def visitDim(self, ctx:BKITParser.DimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#initlist.
    def visitInitlist(self, ctx:BKITParser.InitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#init.
    def visitInit(self, ctx:BKITParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign.
    def visitAssign(self, ctx:BKITParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifstmt.
    def visitIfstmt(self, ctx:BKITParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#cond_block.
    def visitCond_block(self, ctx:BKITParser.Cond_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forstmt.
    def visitForstmt(self, ctx:BKITParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#iter_block.
    def visitIter_block(self, ctx:BKITParser.Iter_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#iter_init.
    def visitIter_init(self, ctx:BKITParser.Iter_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#iter_cond.
    def visitIter_cond(self, ctx:BKITParser.Iter_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#iter_update.
    def visitIter_update(self, ctx:BKITParser.Iter_updateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#whilestmt.
    def visitWhilestmt(self, ctx:BKITParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhilestmt.
    def visitDowhilestmt(self, ctx:BKITParser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#breakstmt.
    def visitBreakstmt(self, ctx:BKITParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continuestmt.
    def visitContinuestmt(self, ctx:BKITParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callstmt.
    def visitCallstmt(self, ctx:BKITParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnstmt.
    def visitReturnstmt(self, ctx:BKITParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmtlist.
    def visitStmtlist(self, ctx:BKITParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcdec.
    def visitFuncdec(self, ctx:BKITParser.FuncdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramdec.
    def visitParamdec(self, ctx:BKITParser.ParamdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bodydec.
    def visitBodydec(self, ctx:BKITParser.BodydecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call.
    def visitCall(self, ctx:BKITParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relexpr.
    def visitRelexpr(self, ctx:BKITParser.RelexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exprlist.
    def visitExprlist(self, ctx:BKITParser.ExprlistContext):
        return self.visitChildren(ctx)



del BKITParser