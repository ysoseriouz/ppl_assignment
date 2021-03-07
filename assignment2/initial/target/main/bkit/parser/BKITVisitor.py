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


    # Visit a parse tree produced by BKITParser#vardecl.
    def visitVardecl(self, ctx:BKITParser.VardeclContext):
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


    # Visit a parse tree produced by BKITParser#init.
    def visitInit(self, ctx:BKITParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignstmt.
    def visitAssignstmt(self, ctx:BKITParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifstmt.
    def visitIfstmt(self, ctx:BKITParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#condblock.
    def visitCondblock(self, ctx:BKITParser.CondblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forstmt.
    def visitForstmt(self, ctx:BKITParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#iterblock.
    def visitIterblock(self, ctx:BKITParser.IterblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#iterinit.
    def visitIterinit(self, ctx:BKITParser.IterinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#itercond.
    def visitItercond(self, ctx:BKITParser.ItercondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#iterupdate.
    def visitIterupdate(self, ctx:BKITParser.IterupdateContext):
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


    # Visit a parse tree produced by BKITParser#funcdecl.
    def visitFuncdecl(self, ctx:BKITParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramdecl.
    def visitParamdecl(self, ctx:BKITParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bodydecl.
    def visitBodydecl(self, ctx:BKITParser.BodydeclContext):
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