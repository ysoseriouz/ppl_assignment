from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
     #program : all_declarations EOF ;
    def visitProgram(self, ctx:BKITParser.ProgramContext):
         
         return Program(ctx.all_declarations().accept(self))
      
    # all_declarations: variable_declarations function_declarations;
    def visitAll_declarations(self, ctx:BKITParser.All_declarationsContext):
         return ctx.variable_declarations().accept(self)+ctx.function_declarations().accept(self)

    # variable_declarations: variable_decl variable_decls| ;
    def visitVariable_declarations(self, ctx:BKITParser.Variable_declarationsContext):
          if ctx.getChildCount()==0:
             return []
          else:
             return ctx.variable_decl().accept(self)+ctx.variable_decls().accept(self)

    # variable_decls: variable_decl variable_decls | ;
    def visitVariable_decls(self, ctx:BKITParser.Variable_declsContext):
        if ctx.getChildCount()==0:
             return []
        else:
             return ctx.variable_decl().accept(self)+ctx.variable_decls().accept(self)
    # variable_decl: VAR COLON variableList SEMI ;
    def visitVariable_decl(self, ctx:BKITParser.Variable_declContext):
        return ctx.variableList().accept(self)

    # variableList:variable variable_list;
    def visitVariableList(self, ctx:BKITParser.VariableListContext):
        return [ctx.variable().accept(self)]+ctx.variable_list().accept(self)

    # variable_list: COMMA variable variable_list| ;
    def visitVariable_list(self, ctx:BKITParser.Variable_listContext):
        if ctx.getChildCount()==0:
             return []
        else:
             return [ctx.variable().accept(self)]+ctx.variable_list().accept(self)

    # variable: ID (dimension_list|)|initial;
    def visitVariable(self, ctx:BKITParser.VariableContext):
        #variable=Id(ctx.ID().getText())
        varDimen=ctx.dimension_list().accept(self) if ctx.dimension_list() else []
        if ctx.ID() or ctx.getChildCount()==2:
            return VarDecl(Id(ctx.ID().getText()),varDimen,None)
        return ctx.initial().accept(self)

    # initial:ID (dimension_list|) ASS literal;
    def visitInitial(self, ctx:BKITParser.InitialContext):
        #variable=Id(ctx.ID().getText())
        varDimen=ctx.dimension_list().accept(self) if ctx.dimension_list() else []
        varInit =ctx.literal().accept(self)
        return VarDecl(Id(ctx.ID().getText()),varDimen,varInit)

    #dimension_list: dimension dimensions;
    def visitDimension_list(self, ctx:BKITParser.Dimension_listContext):
        return [ctx.dimension().accept(self)]+ctx.dimensions().accept(self)

    #dimensions: dimension dimensions|;
    def visitDimensions(self, ctx:BKITParser.DimensionsContext):
        if ctx.getChildCount()==0:
            return []
        return [ctx.dimension().accept(self)]+ctx.dimensions().accept(self) 

    #dimension: LSB INTLIT RSB;
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        return int(ctx.INTLIT().getText()

    #function_declarations: functionList;
    def visitFunction_declarations(self, ctx:BKITParser.Function_declarationsContext):
        return ctx.functionList().accept(self)
    
    # functionList:function functions|;
    def visitFunctionList(self, ctx:BKITParser.FunctionListContext):
        if ctx.getChildCount()==0:
            return []
        return [ctx.function().accept(self)]+ctx.functions().accept(self)

    # functions: function functions|;
    def visitFunctions(self, ctx:BKITParser.FunctionsContext):
        if ctx.getChildCount()==0:
            return []
        return [ctx.function().accept(self)]+ctx.functions().accept(self)

    # function: FUNCTION COLON ID parameters body;
    def visitFunction(self, ctx:BKITParser.FunctionContext):
        name=Id(ctx.ID().getText())
        param=ctx.parameters().accept(self)
        body=ctx.body().accept(self)
        return FuncDecl(name,param,body)

    # parameters: PARAMETER COLON parameterlist|;
    def visitParameters(self, ctx:BKITParser.ParametersContext):
        if ctx.getChildCount()==0:
            return []
        return ctx.parameterlist().accept(self)
            
    # parameterlist: parameter paralist;
    def visitParameterlist(self, ctx:BKITParser.ParameterlistContext):
        return [ctx.parameter().accept(self)]+ctx.paralist().accept(self)

    # paralist: COMMA parameter paralist|;
    def visitParalist(self, ctx:BKITParser.ParalistContext):
        if ctx.getChildCount()==0:
            return []
        return [ctx.parameter().accept(self)]+ctx.paralist().accept(self)

    #parameter: ID (dimension_list|);
    def visitParameter(self, ctx:BKITParser.ParameterContext):
        varDimen=ctx.dimension_list().accept(self) if ctx.dimension_list() else []
        return VarDecl(Id(ctx.ID().getText()),varDimen,None)
    # body: BODY COLON variable_declarations many_statements ENDBODY DOT;
    def visitBody(self, ctx:BKITParser.BodyContext):
        return (ctx.variable_declarations().accept(self),ctx.many_statements().accept(self))

    # many_statements: statement statements|;
    def visitMany_statements(self, ctx:BKITParser.Many_statementsContext):
        if ctx.getChildCount()==0:
            return []
        return [ctx.statement().accept(self)]+ctx.statements().accept(self)

    # statements: statement statements|;
    def visitStatements(self, ctx:BKITParser.StatementsContext):
        if ctx.getChildCount()==0:
            return []
        return [ctx.statement().accept(self)]+ctx.statements().accept(self)

    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)

    # assign_statement:ID ASS expression SEMI |index_expr ASS expression SEMI;
    def visitAssign_statement(self, ctx:BKITParser.Assign_statementContext):
        lhs=Id(ctx.ID().getText()) if ctx.ID() else ctx.index_expr().accept(self)
        rhs=ctx.expression().accept(self)
        return Assign(lhs,rhs)
        
    # if_statement:only_if_statement elseif_statement elsestatement ENDIF DOT;
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        ifstmt = ctx.only_if_statement().accept(self)
        elseifstmts = ctx.elseif_statement().accept(self)
        elsestmt = ctx.elsestatement().accept(self)
        return If([ifstmt] + elseifstmts, elsestmt)

    # only_if_statement: IF expression THEN variable_declarations many_statements;
    def visitOnly_if_statement(self, ctx:BKITParser.Only_if_statementContext):
        return (ctx.expression().accept(self),ctx.variable_declarations().accept(self),ctx.many_statements().accept(self))
    # elseif_statement: elseif elseifs|;
    def visitElseif_statement(self, ctx:BKITParser.Elseif_statementContext):
        if ctx.getChildCount()==0:
            return []
        return [ctx.elseif().accept(self)]+ctx.elseifs().accept(self)

    # elseifs: elseif elseifs|;
    def visitElseifs(self, ctx:BKITParser.ElseifsContext):
        if ctx.getChildCount()==0:
            return []
        return [ctx.elseif().accept(self)]+ctx.elseifs().accept(self)

    # elseif: ELSEIF expression THEN variable_declarations many_statements;
    def visitElseif(self, ctx:BKITParser.ElseifContext):
        return (ctx.expression().accept(self),ctx.variable_declarations().accept(self),ctx.many_statements().accept(self))

    # elsestatement: ELSE variable_declarations many_statements|;
    def visitElsestatement(self, ctx:BKITParser.ElsestatementContext):
        if ctx.getChildCount()==0:
            return ([],[])
        return (ctx.variable_declarations().accept(self),ctx.many_statements().accept(self))
   
    # for_statement: FOR LB ID ASS expression COMMA expression COMMA expression RB DO variable_declarations many_statements ENDFOR DOT;
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        idx1=Id(ctx.ID().getText())
        expr1=ctx.expression(0).accept(self)
        expr2=ctx.expression(1).accept(self)
        expr3=ctx.expression(2).accept(self)
        loop=(ctx.variable_declarations().accept(self),ctx.many_statements().accept(self))
        return For(idx1,expr1,expr2,expr3,loop)

    # while_statement: WHILE expression DO variable_declarations many_statements ENDWHILE DOT;
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        exp=ctx.expression().accept(self)
        sl=(ctx.variable_declarations().accept(self),ctx.many_statements().accept(self))
        return While(exp,sl)

    # dowhile_statement: DO variable_declarations many_statements WHILE expression ENDDO DOT;
    def visitDowhile_statement(self, ctx:BKITParser.Dowhile_statementContext):
        sl=(ctx.variable_declarations().accept(self),ctx.many_statements().accept(self))
        exp=ctx.expression().accept(self)
        return Dowhile(sl,exp)

    # break_statement: BREAK SEMI;
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return Break()

    # continue_statement:CONTINUE SEMI;
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return Continue()


    # call_statement:ID LB argument_list RB SEMI ;.
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        method=Id(ctx.ID().getText())
        param=ctx.argument_list().accept(self)
        return CallStmt(method,param)

    # return_statement:RETURN (expression|) SEMI;
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return Return(ctx.expression().accept(self)) if ctx.expression() else Return()

    # argument_list: argument arguments|;
    def visitArgument_list(self, ctx:BKITParser.Argument_listContext):
        if ctx.getChildCount()==0:
            return []
        return [ctx.argument().accept(self)]+ctx.arguments().accept(self)

    # arguments: COMMA argument arguments|;
    def visitArguments(self, ctx:BKITParser.ArgumentsContext):
        if ctx.getChildCount()==0:
            return []
        return [ctx.argument().accept(self)]+ctx.arguments().accept(self)

    # argument: expression;
    def visitArgument(self, ctx:BKITParser.ArgumentContext):
        return ctx.expression().accept(self)

    # operands: literal|ID|LB expression RB;
    def visitOperands(self, ctx:BKITParser.OperandsContext):
        if ctx.literal():
            return ctx.literal().accept(self)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        return ctx.expression().accept(self)

    # literal:INTLIT|FLOATLIT|STRINGLIT|BOOLIT|array_lit;
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        elif ctx.BOOLIT():
            if ctx.TRUE():
                 return BooleanLiteral(bool(ctx.TRUE().getText()))
            else:
                 return BooleanLiteral(bool(ctx.FALSE().getText()))
        return ctx.array_lit().accept(self)

    # array_lit: LP literal_list RP;
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        return ArrayLiteral(ctx.literal_list().accept(self))

    # literal_list:literal literals;
    def visitLiteral_list(self, ctx:BKITParser.Literal_listContext):
        return [ctx.literal().accept(self)]+ctx.literals().accept(self)

    # literals: COMMA literal literals|;
    def visitLiterals(self, ctx:BKITParser.LiteralsContext):
        if ctx.getChildCount()==0:
            return []
        return [ctx.literal().accept(self)]+ctx.literals().accept(self)


#      expression:expression1 (EQUAL|NOTEQUAL|SMALLER|LARGER|SMALLEROREQUAL|LARGEROREQUAL|DIFFER|
#      SMALLERFLOAT|LARGERFLOAT|LOREQUALFLOAT|SOREQUALFLOAT) expression1|expression1;
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        if ctx.getChildCount()==1:
            return ctx.expression1(0).accept(self)
        return BinaryOp(ctx.getChild(1).getText(),ctx.expression1(0).accept(self),ctx.expression1(1))


    # expression1: expression1 (AND|OR) expression2|expression2;
    def visitExpression1(self, ctx:BKITParser.Expression1Context):
        if ctx.getChildCount()==1:
            return ctx.expression2().accept(self)
        return BinaryOp(ctx.getChild(1).getText(),ctx.expression1().accept(self),ctx.expression2().accept(self))

    # expression2: expression2(ADD|ADDFLOAT|SUB|SUBFLOAT) expression3|expression3;
    def visitExpression2(self, ctx:BKITParser.Expression2Context):
        if ctx.getChildCount()==1:
            return ctx.expression3().accept(self)
        return BinaryOp(ctx.getChild(1).getText(),ctx.expression2().accept(self),ctx.expression3().accept(self))
        

    # expression3: expression3(MUL|MULFLOAT|DIV|DIVFLOAT|MOD) expression4|expression4;
    def visitExpression3(self, ctx:BKITParser.Expression3Context):
        if ctx.getChildCount()==1:
            return ctx.expression4().accept(self)
        return BinaryOp(ctx.getChild(1).getText(),ctx.expression3().accept(self),ctx.expression4().accept(self))


    # expression4: (NOT) expression4|expression5;
    def visitExpression4(self, ctx:BKITParser.Expression4Context):
        if ctx.getChildCount()==1:
            return ctx.expression5().accept(self)
        return UnaryOp(ctx.getChild(0).getText(),ctx.expression4().accept(self))

    # expression5: (SUB|SUBFLOAT) expression5|index_expr;
    def visitExpression5(self, ctx:BKITParser.Expression5Context):
        if ctx.getChildCount()==1:
            return ctx.index_expr().accept(self)
        return UnaryOp(ctx.getChild(0).getText(),ctx.expression5().accept(self))

    # index_expr: index_expr index_operator|function_call;
    def visitIndex_expr(self, ctx:BKITParser.Index_exprContext):
        if ctx.getChildCount()==1:
            return ctx.function_call().accept(self)
        return ArrayCell(ctx.index_expr().accept(self),ctx.index_operator().accept(self))

    # index_operator: LSB expression RSB|LSB expression RSB index_operator;
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        if ctx.getChildCount()==3:
            return [ctx.expression().accept(self)]
        return [ctx.expression().accept(self)] + ctx.index_operator().accept(self)

    # function_call: ID LB argument_list RB|operands;
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        if ctx.getChildCount()==1:
            return ctx.operands().accept(self)
        return CallExpr(Id(ctx.ID().getText()),ctx.argument_list().accept(self))

   

    

