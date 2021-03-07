from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce

class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        vardecl_list = reduce(lambda acc, ele: acc + ele.accept(self),
                            ctx.vardecl(), [])
        funcdecl_list = list(map(lambda x: x.accept(self), ctx.funcdecl()))
        return Program(vardecl_list + funcdecl_list)

    #################### VarDecl Visitor ##########################
    def visitVardecl(self, ctx:BKITParser.VardeclContext):
        """Return a list of VarDecl objects"""
        return ctx.varlist().accept(self)

    def visitVarlist(self, ctx:BKITParser.VarlistContext):
        return list(map(lambda x: x.accept(self), ctx.variable()))
    
    def visitVariable(self, ctx:BKITParser.VariableContext):
        variable = Id(ctx.ID().getText())
        varDimen = list(map(lambda x: x.accept(self), ctx.dim()))
        varInit = ctx.init().accept(self) if ctx.init() else None
        return VarDecl(variable, varDimen, varInit)
    
    def visitDim(self, ctx:BKITParser.DimContext):
        if ctx.INTLIT():
            if ctx.INTLIT().getText()[:2] in ['0x', '0X']:
                # Base 16
                return int(ctx.INTLIT().getText(), 16)
            elif ctx.INTLIT().getText()[:2] in ['0o', '0O']:
                # Base 8
                return int(ctx.INTLIT().getText(), 8)
            else:
                return int(ctx.INTLIT().getText())
        return None
    
    def visitInit(self, ctx:BKITParser.InitContext):
        return ctx.literal().accept(self)
    
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        if ctx.INTLIT():
            if ctx.INTLIT().getText()[:2] in ['0x', '0X']:
                # Base 16
                return IntLiteral(int(ctx.INTLIT().getText(), 16))
            elif ctx.INTLIT().getText()[:2] in ['0o', '0O']:
                # Base 8
                return IntLiteral(int(ctx.INTLIT().getText(), 8))
            else:
                return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText() == 'True')
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        else:
            return ArrayLiteral(ctx.arraylit().accept(self))
    
    def visitArraylit(self, ctx:BKITParser.ArraylitContext):
        return ctx.litlist().accept(self) if ctx.litlist() else []
    
    def visitLitlist(self, ctx:BKITParser.LitlistContext):
        return list(map(lambda x: x.accept(self), ctx.literal()))
        
    #################### FuncDecl Visitor ##########################
    def visitFuncdecl(self, ctx:BKITParser.FuncdeclContext):
        name = Id(ctx.ID().getText())
        param = ctx.paramdecl().accept(self) if ctx.paramdecl() else []
        body = ctx.bodydecl().accept(self)
        return FuncDecl(name, param, body)
    
    def visitParamdecl(self, ctx:BKITParser.ParamdeclContext):
        return ctx.varlist().accept(self)
    
    def visitBodydecl(self, ctx:BKITParser.BodydeclContext):
        return ctx.stmtlist().accept(self)
    
    def visitStmtlist(self, ctx:BKITParser.StmtlistContext):
        vardecl_list = reduce(lambda acc, ele: acc + ele.accept(self),
                        ctx.vardecl(), [])
        stmt_list = list(map(lambda x: x.accept(self), ctx.stmt()))
        return (vardecl_list, stmt_list)
    
    #################### Statement Visitor ########################## 
    def visitStmt(self, ctx:BKITParser.StmtContext):
        if ctx.assignstmt():
            return ctx.assignstmt().accept(self)
        elif ctx.ifstmt():
            return ctx.ifstmt().accept(self)
        elif ctx.forstmt():
            return ctx.forstmt().accept(self)
        elif ctx.whilestmt():
            return ctx.whilestmt().accept(self)
        elif ctx.dowhilestmt():
            return ctx.dowhilestmt().accept(self)
        elif ctx.breakstmt():
            return ctx.breakstmt().accept(self)
        elif ctx.continuestmt():
            return ctx.continuestmt().accept(self)
        elif ctx.callstmt():
            return ctx.callstmt().accept(self)
        else:
            return ctx.returnstmt().accept(self)
    
    def visitAssignstmt(self, ctx:BKITParser.AssignstmtContext):
        return Assign(ctx.expr(0).accept(self), ctx.expr(1).accept(self))
        
    def visitIfstmt(self, ctx:BKITParser.IfstmtContext):
        ifthenStmt = list(map(lambda x: x.accept(self), ctx.condblock()))
        elseStmt = ctx.stmtlist().accept(self) if ctx.stmtlist() else ([],[])
        return If(ifthenStmt, elseStmt)
    
    def visitCondblock(self, ctx:BKITParser.CondblockContext):
        expr = ctx.expr().accept(self)
        vardecl_list, stmt_list = ctx.stmtlist().accept(self)
        return (expr, vardecl_list, stmt_list)

    def visitForstmt(self, ctx:BKITParser.ForstmtContext):
        idx1, expr1, expr2, expr3 = ctx.iterblock().accept(self)
        loop = ctx.stmtlist().accept(self)
        return For(idx1, expr1, expr2, expr3, loop)
    
    def visitIterblock(self, ctx:BKITParser.IterblockContext):
        idx1, expr1 = ctx.iterinit().accept(self)
        expr2 = ctx.itercond().accept(self)
        expr3 = ctx.iterupdate().accept(self)
        return (idx1, expr1, expr2, expr3)
    
    def visitIterinit(self, ctx:BKITParser.IterinitContext):
        return (Id(ctx.ID().getText()), ctx.expr().accept(self))
    
    def visitItercond(self, ctx:BKITParser.ItercondContext):
        return ctx.expr().accept(self)
    
    def visitIterupdate(self, ctx:BKITParser.IterupdateContext):
        return ctx.expr().accept(self)
    
    def visitWhilestmt(self, ctx:BKITParser.WhilestmtContext):
        return While(ctx.expr().accept(self), ctx.stmtlist().accept(self))

    def visitDowhilestmt(self, ctx:BKITParser.DowhilestmtContext):
        return Dowhile(ctx.stmtlist().accept(self), ctx.expr().accept(self))
    
    def visitBreakstmt(self, ctx:BKITParser.BreakstmtContext):
        return Break()
    
    def visitContinuestmt(self, ctx:BKITParser.ContinuestmtContext):
        return Continue()
    
    def visitCallstmt(self, ctx:BKITParser.CallstmtContext):
        method, param = ctx.call().accept(self)
        return CallStmt(method, param)
    
    def visitReturnstmt(self, ctx:BKITParser.ReturnstmtContext):
        return Return(ctx.expr().accept(self)) if ctx.expr() else Return(None)
    
    #################### Expression Visitor ########################## 
    def visitCall(self, ctx:BKITParser.CallContext):
        expr_list = ctx.exprlist().accept(self) if ctx.exprlist() else []
        return (Id(ctx.ID().getText()), expr_list)
    
    def visitExprlist(self, ctx:BKITParser.ExprlistContext):
        return list(map(lambda x: x.accept(self), ctx.expr()))

    def visitExpr(self, ctx:BKITParser.ExprContext):
        if ctx.getChildCount() == 1:
            return ctx.relexpr(0).accept(self)
        return BinaryOp(ctx.RELOP().getText(),
                        ctx.relexpr(0).accept(self),
                        ctx.relexpr(1).accept(self))
    
    def visitRelexpr(self, ctx:BKITParser.RelexprContext):
        if ctx.getChildCount() == 1:
            return ctx.operand().accept(self)
        elif ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), 
                            ctx.relexpr(0).accept(self))
        elif ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(),
                            ctx.relexpr(0).accept(self),
                            ctx.relexpr(1).accept(self))
        else:
            return ArrayCell(ctx.relexpr(0).accept(self),
                             list(map(lambda x: x.accept(self), ctx.expr()))) 
    
    def visitOperand(self, ctx:BKITParser.OperandContext):
        if ctx.getChildCount() == 3:
            return ctx.expr().accept(self)

        if ctx.call():
            method, param = ctx.call().accept(self)
            return CallExpr(method, param)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return ctx.literal().accept(self)