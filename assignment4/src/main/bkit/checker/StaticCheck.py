"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    def __eq__(self, other):
        return type(self) == type(other)

class Prim(Type):
    __metaclass__ = ABCMeta

class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class Symbol:
    name: str
    mtype:Type

    def __str__(self):
        return f"Symbol({self.name}, {self.mtype})"

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type
    def __eq__(self, other):
        return type(other) == ArrayType and self.dimen == other.dimen and self.eletype == other.eletype

@dataclass
class MType(Type):
    intype:List[Symbol]
    restype:Type

#########################################################################################
class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([Symbol(None,FloatType())],IntType())),
Symbol("float_to_int",MType([Symbol(None,IntType())],FloatType())),
Symbol("int_of_string",MType([Symbol(None,StringType())],IntType())),
Symbol("string_of_int",MType([Symbol(None,IntType())],StringType())),
Symbol("float_of_string",MType([Symbol(None,StringType())],FloatType())),
Symbol("string_of_float",MType([Symbol(None,FloatType())],StringType())),
Symbol("bool_of_string",MType([Symbol(None,StringType())],BoolType())),
Symbol("string_of_bool",MType([Symbol(None,BoolType())],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([Symbol(None,StringType())],VoidType())),
Symbol("printStrLn",MType([Symbol(None,StringType())],VoidType()))]
        self.first_runtime = True

    ############################# Helper Function #####################################
    def get_kind(self, ast):
        return Function() if type(ast) == FuncDecl else Variable()

    def get_type(self, symbol):
        if type(symbol) == tuple:
            symbol = symbol[0]
        if type(symbol.mtype) == MType:  
            return symbol.mtype.restype
        elif type(symbol.mtype) == ArrayType:
            return symbol.mtype
        else:
            return symbol.mtype
    
    def get_symbol_by_name(self, name, c):
        for envi in c:
            for sym in envi:
                if sym.name == name:
                    return sym
        return None
        
    def infer_type_by_type(self, symbol, inferType):
        # Store type into symbol
        if type(symbol.mtype) == MType:
            symbol.mtype.restype = inferType
        elif type(symbol.mtype) == ArrayType:
            symbol.mtype.eletype = inferType
        else:
            symbol.mtype = inferType

    def infer_type_by_symbol(self, ast, leftSym, rightSym):
        if type(leftSym) == tuple or type(rightSym) == tuple or type(leftSym.mtype) == ArrayType or type(rightSym.mtype) == ArrayType:
            return self.infer_array_type(ast, leftSym, rightSym)
        leftType = self.get_type(leftSym)
        rightType = self.get_type(rightSym)

        if type(leftType) == Unknown:
            if type(rightType) == Unknown and isinstance(ast, Stmt):
                raise TypeCannotBeInferred(ast)
            self.infer_type_by_type(leftSym, rightType)
        elif type(leftType) != type(rightType):
            if type(rightType) == Unknown:
                self.infer_type_by_type(rightSym, leftType)
            elif isinstance(ast, Stmt):
                raise TypeMismatchInStatement(ast)
            elif isinstance(ast, Expr):
                raise TypeMismatchInExpression(ast)
    
    def infer_array_type(self, ast, leftSym, rightSym):
        leftIdx, rightIdx = None, None
        if type(leftSym) == tuple:
            leftIdx = leftSym[1]
            leftSym = leftSym[0]
        if type(rightSym) == tuple:
            rightIdx = rightSym[1]
            rightSym = rightSym[0]
    
        leftType = self.get_type(leftSym)
        rightType = self.get_type(rightSym)

        if leftIdx is not None:
            leftType = ArrayType(leftType.dimen[leftIdx:], leftType.eletype) \
                                if leftIdx < len(leftType.dimen) \
                                else leftType.eletype
        if rightIdx is not None:
            rightType = ArrayType(rightType.dimen[leftIdx:], rightType.eletype) \
                                if rightIdx < len(rightType.dimen) \
                                else rightType.eletype

        # Infer array type
        if type(leftType) == ArrayType and type(rightType) == ArrayType and leftType.dimen == rightType.dimen:
            if type(leftType.eletype) == Unknown:
                if type(rightType.eletype) == Unknown:
                    if isinstance(ast, Stmt):
                        raise TypeCannotBeInferred(ast)
                self.infer_type_by_type(leftSym, rightType.eletype)
            elif type(leftType.eletype) != type(rightType.eletype):
                if type(rightType.eletype) == Unknown:
                    self.infer_type_by_type(rightSym, leftType.eletype)
        elif type(leftType) == Unknown:
            if type(leftSym.mtype) == MType:
                leftSym.mtype.restype = rightType
            elif type(leftSym.mtype) == ArrayType:
                leftSym.mtype.eletype = rightType
        elif type(rightType) == Unknown:
            if type(rightSym.mtype) == MType:
                rightSym.mtype.restype = rightType
            elif type(rightSym.mtype) == ArrayType:
                rightSym.mtype.eletype = leftType

        leftType = self.get_type(leftSym)
        rightType = self.get_type(rightSym)

        if leftIdx is not None:
            leftType = ArrayType(leftType.dimen[leftIdx:], leftType.eletype) \
                                if leftIdx < len(leftType.dimen) \
                                else leftType.eletype
        if rightIdx is not None:
            rightType = ArrayType(rightType.dimen[leftIdx:], rightType.eletype) \
                                if rightIdx < len(rightType.dimen) \
                                else rightType.eletype

        if leftType != rightType:
            if isinstance(ast, Stmt):
                raise TypeMismatchInStatement(ast)
            elif isinstance(ast, Expr):
                raise TypeMismatchInExpression(ast)

    def is_inferred(self, symbol):
        # Return TRUE if fully inferred, FALSE otherwise
        if type(symbol.mtype) == Unknown:
            return False
        elif type(symbol.mtype) == MType:
            return all([self.is_inferred(param) for param in symbol.mtype.intype])
        elif type(symbol.mtype) == ArrayType and type(symbol.mtype.eletype) == Unknown:
            return False
        return True
    ##################################################################################
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        c = [c]
        [self.visit(decl, (c, self.get_kind(decl))) for decl in ast.decl]

        # Check main function exists
        check_main = ["main" == sym.name and type(sym.mtype) == MType for sym in c[-1]]
        if not any(check_main):
            raise NoEntryPoint()

        # Second run
        self.first_runtime = False
        [self.visit(decl, (c, self.get_kind(decl))) for decl in ast.decl if isinstance(decl, FuncDecl)]

    def visitVarDecl(self, ast, c):
        kind = c[1]
        c = c[0]

        # Check redeclaration
        name = ast.variable.name
        if name in [symbol.name for symbol in c[0]]:
            raise Redeclared(kind, name)

        if len(ast.varDimen) > 0:
            if ast.varInit is None:
                typ = ArrayType(ast.varDimen, Unknown())
                c[0] = [Symbol(name, typ)] + c[0]
            else:
                typ = self.visit(ast.varInit, None).mtype
                c[0] = [Symbol(name, typ)] + c[0]
        else:
            if ast.varInit is None:
                typ = Unknown()
                c[0] = [Symbol(name, typ)] + c[0]
            else:
                typ = self.visit(ast.varInit, None).mtype
                c[0] = [Symbol(name, typ)] + c[0]
        
    def visitFuncDecl(self, ast, c):
        kind = c[1]
        c = c[0]

        if self.first_runtime:
            # Traverse parameters
            new_c = [[]]
            [self.visit(param, (new_c, Parameter())) for param in ast.param]    # Special flag for parameter declaration

            # Check redeclaration
            name = ast.name.name
            if name in [symbol.name for symbol in c[0]]:
                raise Redeclared(kind, name)

            # Add FuncDecl to environment
            func_sym = Symbol(name, MType(new_c[0][::-1], Unknown()))
            c[0] = [func_sym] + c[0]
            return None

        func_sym = self.get_symbol_by_name(ast.name.name, c)
        if func_sym is None or type(func_sym.mtype) != MType:
            raise Undeclared(Function(), ast.name.name)

        # Traver body of function
        local_c = [func_sym.mtype.intype]
        [self.visit(decl, (local_c, self.get_kind(decl))) for decl in ast.body[0]]
        local_len = len(local_c[0]) - len(func_sym.mtype.intype)
        new_c = [local_c[0][:local_len]] + c
        [self.visit(stmt, (new_c, func_sym)) for stmt in ast.body[1]]

    #################### Statement Visitor ##########################
    def visitAssign(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        lhs = self.visit(ast.lhs, c)
        rhs = self.visit(ast.rhs, c)
        if lhs == False or rhs == False:
            raise TypeCannotBeInferred(ast)

        # Left hand side must not be VoidType
        self.infer_type_by_symbol(ast, lhs, rhs)
        if type(self.get_type(lhs)) == VoidType:
            raise TypeMismatchInStatement(ast)
    
    def visitIf(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        cond_syms = [self.visit(block[0], c) for block in ast.ifthenStmt]
        if any([cond == False for cond in cond_syms]):
            raise TypeCannotBeInferred(ast)
        [self.infer_type_by_symbol(ast, cond_sym, Symbol(None, BoolType())) for cond_sym in cond_syms]

        # Get all block
        blocks = [(block[1], block[2]) for block in ast.ifthenStmt]
        if ast.elseStmt is not None:
            blocks = blocks + [ast.elseStmt]
    
        # Visit body of If statement
        dup_envi = envi
        for block in blocks:
            new_c = [[]] + dup_envi
            [self.visit(decl, (new_c, self.get_kind(decl))) for decl in block[0]]
            [self.visit(stmt, (new_c, func_sym)) for stmt in block[1]]
    
    def visitFor(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        id = self.visit(ast.idx1, c)

        # Infer type in for loop
        self.infer_type_by_symbol(ast, id, Symbol(None, IntType()))

        # Check type of expressions in for loop
        expr_syms = [self.visit(expr, c) for expr in [ast.expr1, ast.expr2, ast.expr3]]
        if any([expr == False for expr in expr_syms]):
            raise TypeCannotBeInferred(ast)

        typ_syms = [Symbol(None, IntType()), Symbol(None, BoolType()), Symbol(None, IntType())]
        [self.infer_type_by_symbol(ast, expr, typ) for (expr, typ) in zip(expr_syms, typ_syms)]

        # Visit body of For statement
        new_c = [[]] + envi
        [self.visit(decl, (new_c, self.get_kind(decl))) for decl in ast.loop[0]]
        [self.visit(stmt, (new_c, func_sym)) for stmt in ast.loop[1]]
    
    def visitContinue(self, ast, c):
        func_sym = c[1]
        envi = c[0]
        return None
    
    def visitBreak(self, ast, c):
        func_sym = c[1]
        envi = c[0]
        return None
    
    def visitReturn(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        if type(func_sym.mtype.restype) == VoidType and ast.expr is not None:
            raise TypeMismatchInStatement(ast)

        # Get return type of Return Statement and infer restype
        restype_sym = self.visit(ast.expr, c) if ast.expr is not None else Symbol(None, VoidType())
        if restype_sym == False:
            raise TypeCannotBeInferred(ast)

        self.infer_type_by_symbol(ast, func_sym, restype_sym)
        if type(restype_sym) == tuple:
            restype_sym = restype_sym[0]
        if self.is_inferred(restype_sym) == False:
            raise TypeCannotBeInferred(ast)
    
    def visitDowhile(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        # Visit body of DoWhile statement with new scope
        new_c = [[]] + envi
        [self.visit(decl, (new_c, self.get_kind(decl))) for decl in ast.sl[0]]
        [self.visit(stmt, (new_c, func_sym)) for stmt in ast.sl[1]]

        # Get condition expression symbol and infer type
        expr = self.visit(ast.exp, c)
        if expr == False:
            raise TypeCannotBeInferred(ast)
        self.infer_type_by_symbol(ast, expr, Symbol(None, BoolType()))

    def visitWhile(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        # Get condition expression symbol and infer type
        expr = self.visit(ast.exp, c)
        if expr == False:
            raise TypeCannotBeInferred(ast)
        self.infer_type_by_symbol(ast, expr, Symbol(None, BoolType()))

        # Visit body of While statement
        new_c = [[]] + envi
        [self.visit(decl, (new_c, self.get_kind(decl))) for decl in ast.sl[0]]
        [self.visit(stmt, (new_c, func_sym)) for stmt in ast.sl[1]]

    def visitCallStmt(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        func_sym = self.visit(ast.method, (c, Function()))

        # Infer return type
        self.infer_type_by_symbol(ast, func_sym, Symbol(None, VoidType()))

        # Check return type and number of arguments
        if len(ast.param) != len(func_sym.mtype.intype):
            raise TypeMismatchInStatement(ast)

        # Infer parameter types and check type compatibility
        arg_syms = [self.visit(arg, c) for arg in ast.param]
        if any([arg == False for arg in arg_syms]):
            return False
        param_syms = func_sym.mtype.intype
        [self.infer_type_by_symbol(ast, arg, param) for arg, param in zip(arg_syms, param_syms)]
        
    #################### Expression Visitor ##########################
    def visitBinaryOp(self, ast, c):
        leftSym = self.visit(ast.left, c)
        rightSym = self.visit(ast.right, c)
        if leftSym == False or rightSym == False:
            return False

        if ast.op in ['-', '+', '*', '\\', '%']:
            self.infer_type_by_symbol(ast, leftSym, Symbol(None, IntType()))
            self.infer_type_by_symbol(ast, rightSym, Symbol(None, IntType()))
            return Symbol(None, IntType())        
        elif ast.op in ['-.', '+.', '*.', '\\.']:
            self.infer_type_by_symbol(ast, leftSym, Symbol(None, FloatType()))
            self.infer_type_by_symbol(ast, rightSym, Symbol(None, FloatType()))
            return Symbol(None, FloatType())        
        elif ast.op in ['&&', '||']:
            self.infer_type_by_symbol(ast, leftSym, Symbol(None, BoolType()))
            self.infer_type_by_symbol(ast, rightSym, Symbol(None, BoolType()))
            return Symbol(None, BoolType())        
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            self.infer_type_by_symbol(ast, leftSym, Symbol(None, IntType()))
            self.infer_type_by_symbol(ast, rightSym, Symbol(None, IntType()))
            return Symbol(None, BoolType())
        elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
            self.infer_type_by_symbol(ast, leftSym, Symbol(None, FloatType()))
            self.infer_type_by_symbol(ast, rightSym, Symbol(None, FloatType()))
            return Symbol(None, BoolType())
    
    def visitUnaryOp(self, ast, c):
        sym = self.visit(ast.body, c)
        if sym == False:
            return False

        if ast.op == '-':
            self.infer_type_by_symbol(ast, sym, Symbol(None, IntType()))
            return Symbol(None, IntType())
        elif ast.op == '-.':
            self.infer_type_by_symbol(ast, sym, Symbol(None, FloatType()))
            return Symbol(None, FloatType())
        elif ast.op == '!':
            self.infer_type_by_symbol(ast, sym, Symbol(None, BoolType()))
            return Symbol(None, BoolType())
    
    def visitCallExpr(self, ast, c):
        func_sym = self.visit(ast.method, (c, Function()))

        # Check return type and number of arguments
        if len(ast.param) != len(func_sym.mtype.intype):
            raise TypeMismatchInExpression(ast)

        # Infer parameter types and check type compatibility
        arg_syms = [self.visit(arg, c) for arg in ast.param]
        if any([arg == False for arg in arg_syms]):
            return False
        param_syms = func_sym.mtype.intype
        [self.infer_type_by_symbol(ast, arg, param) for arg, param in zip(arg_syms, param_syms)]
        return func_sym if self.is_inferred(func_sym) else False

    def visitId(self, ast, c):
        kind = Identifier()
        if len(c) == 2 and type(c[1]) == Function:
            kind = c[1]
            c = c[0]
        func_sym = c[1]
        envi = c[0]

        for scope in envi:
            for sym in scope:
                if sym.name == ast.name:
                    if type(kind) == Function and type(sym.mtype) != MType:
                        raise Undeclared(kind, ast.name)
                    elif type(kind) == Identifier:
                        if type(sym.mtype) == MType:
                            for param in sym.mtype.intype:
                                if param.name == ast.name:
                                    if type(kind) == Identifier:
                                        return param
                                    raise Undeclared(kind, ast.name)
                            raise Undeclared(kind, ast.name)
                    return sym
                elif sym.name == func_sym.name:
                    for param in sym.mtype.intype:
                        if param.name == ast.name:
                            if type(kind) == Identifier:
                                return param
                            raise Undeclared(kind, ast.name)
        raise Undeclared(kind, ast.name)
    
    def visitArrayCell(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        arr = self.visit(ast.arr, c)
        if arr == False:
            return False
        if arr is None:
            # Only visitId return None
            raise Undeclared(Identifier(), ast.arr.name)

        arr_type = self.get_type(arr)

        if type(arr_type) != ArrayType:
            return False
        if len(arr_type.dimen) < len(ast.idx):
            raise IndexOutOfRange(ast)

        expr_syms = [self.visit(expr, c) for expr in ast.idx]
        if any([expr == False for expr in expr_syms]):
            return False

        [self.infer_type_by_symbol(ast, expr, Symbol(None, IntType())) for expr in expr_syms]
        return (arr, len(ast.idx))

    #################### Literal Visitor ##########################
    def visitIntLiteral(self, ast, c):
        return Symbol(None, IntType())
    
    def visitFloatLiteral(self, ast, c):
        return Symbol(None, FloatType())
    
    def visitStringLiteral(self, ast, c):
        return Symbol(None, StringType())

    def visitBooleanLiteral(self, ast, c):
        return Symbol(None, BoolType())
    
    def visitArrayLiteral(self, ast, c):
        res = self.visit(ast.value[0], c)
        return Symbol(None, ArrayType([len(ast.value)] + res.mtype.dimen, res.mtype.eletype)) \
                            if type(res.mtype) == ArrayType \
                            else Symbol(None, ArrayType([len(ast.value)], res.mtype))