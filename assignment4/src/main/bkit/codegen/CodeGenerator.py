'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *   
 *   @author Nguyen Tien Thanh 1852740
 *   Principle of Programming Languages Sem201
 *
'''
from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from AST import *
from functools import reduce

##########################################################
class Kind(ABC):
    pass

class Function(Kind):
    def __str__(self):
        return "Function"

class Parameter(Kind):
    def __str__(self):
        return "Parameter"

class Variable(Kind):
    def __str__(self):
        return "Variable"

class Identifier(Kind):
    def __str__(self):
        return "Identifier"
##########################################################
class MethodEnv():
    def __init__(self, frame, sym):
        # sym: List[Symbol]
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isArrayType=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isArrayType = isArrayType

class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

class CName:
    def __init__(self,n):
        self.value = n

class Index:
    def __init__(self,n):
        self.value = n

class Type(ABC): pass
class Unknown(Type): pass
class IntType(Type): pass
class FloatType(Type): pass
class StringType(Type): pass
class BoolType(Type): pass
class VoidType(Type): pass

class ClassType(Type):
    def __init__(self,n):
        self.cname = n

class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type

class ArrayType(Type):
    def __init__(self,et,s=None):
        self.eleType = et #Type
        self.dimen = s   #List[int]
    def __eq__(self, other):
        return type(other) == ArrayType and self.dimen == other.dimen and self.eleType == other.eleType

class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("int_of_float",MType([Symbol(None,FloatType())],IntType()), CName(self.libName)),
            Symbol("float_to_int",MType([Symbol(None,IntType())],FloatType()), CName(self.libName)),
            Symbol("int_of_string",MType([Symbol(None,StringType())],IntType()), CName(self.libName)),
            Symbol("string_of_int",MType([Symbol(None,IntType())],StringType()), CName(self.libName)),
            Symbol("float_of_string",MType([Symbol(None,StringType())],FloatType()), CName(self.libName)),
            Symbol("string_of_float",MType([Symbol(None,FloatType())],StringType()), CName(self.libName)),
            Symbol("bool_of_string",MType([Symbol(None,StringType())],BoolType()), CName(self.libName)),
            Symbol("string_of_bool",MType([Symbol(None,BoolType())],StringType()), CName(self.libName)),
            Symbol("printLn",MType([],VoidType()), CName(self.libName)),
            Symbol("print",MType([Symbol(None,StringType())],VoidType()), CName(self.libName)),
            Symbol("printStrLn",MType([Symbol(None,StringType())],VoidType()), CName(self.libName)),
            Symbol("read",MType([],StringType()), CName(self.libName))
        ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        # Infer type
        sc = StaticChecker(ast, gl)
        env = sc.visit(ast, None)           # inferred referencing environment

        gl = list(map(lambda sym: Symbol(sym.name, MType(list(map(lambda x: x.mtype, sym.mtype.partype)),sym.mtype.rettype), sym.value), gl))
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, env)



class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.globalVarDecl = list()     # List[VarDecl]

    def getType(self, originType):
        if type(originType) is ArrayType:
            return self.flattenArrayType(originType)
        return originType

    def flattenArrayType(self, arrType):
        # ArrayType(Type, [Int,...]) -> # ArrayType(ArrayType(...ArrayType(Type, Int)..., Int), Int)
        typ = arrType.eleType
        for d in arrType.dimen[::-1]:
            typ = ArrayType(typ, d)
        return typ
    
    def initArray(self, sym, arrayLit, c):
        # sym: Symbol(<name>, mtype=ArrayType, <value>)
        result = list()
        if type(sym.value) is Index:
            result.append(self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, c.frame))
        else:
            result.append(self.emit.emitGETSTATIC(f"{sym.value.value}.{sym.name}", sym.mtype, c.frame))

        result += self.storeArray(arrayLit, c)
        return ''.join(result)
    
    def storeArray(self, literal, c):
        # Store array into Array pointer
        # Array Pointer is already on top of the stack
        # literal: ArrayLiteral
        if type(literal.value[0]) is ArrayLiteral:
            result = [self.emit.emitDUP(c.frame) for i in range(len(literal.value) - 1)]
            for i, lit in zip(range(len(literal.value)), literal.value):
                result.append(self.emit.emitPUSHICONST(i, c.frame))
                result.append(self.emit.emitALOAD(ArrayType(None), c.frame))
                result += self.storeArray(lit, c)
            return result
        else:
            result = [self.emit.emitDUP(c.frame) for i in range(len(literal.value) - 1)]
            for i, lit in zip(range(len(literal.value)), literal.value):
                result.append(self.emit.emitPUSHICONST(i, c.frame))
                code, typ = self.visit(lit, c)
                result.append(code)
                result.append(self.emit.emitASTORE(typ, c.frame))
            return result
    
    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        for sym in c:
            if sym.value is None:
                sym.value = CName(self.className)
        self.infer = c

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        e = MethodEnv(None, self.env)
        for decl in ast.decl:
            if type(decl) is VarDecl:
                e.sym = [self.visit(decl, e)] + e.sym
        
        # generate default constructor
        self.genInit(e)

        for decl in ast.decl:
            if type(decl) is FuncDecl:
                e.sym = [self.visit(decl, e)] + e.sym

        self.emit.emitEPILOG()
        return c
    
    def visitVarDecl(self, ast, c):
        isParam = False
        varName = ast.variable.name
        varDimen = ast.varDimen
        varInit = ast.varInit
        varSym = next(filter(lambda x: x.name == varName, self.infer), None)
        varType = None
        if varSym:
            varType = varSym.mtype
        elif varInit:
            _, varType = self.emit.getConst(varInit)
            if len(varDimen) > 0:
                varType = ArrayType(varType, varDimen)
        elif c.frame is not None:
            funcSym = next(filter(lambda x: x.name == c.frame.name, self.infer), None)
            paramSym = next(filter(lambda x: x.name == varName, funcSym.mtype.partype), None)
            varType = paramSym.mtype
            isParam = True

        if c.frame is None:
            self.globalVarDecl.append(ast)
            frame = Frame(None, None)
            # Global scope
            val = CName(self.className)

            # Variable declare
            self.emit.printout(self.emit.emitATTRIBUTE(varName, self.getType(varType), False))
        else:
            val = Index(c.frame.getNewIndex())

            # Variable declare
            self.emit.printout(self.emit.emitVAR(val.value, varName, self.getType(varType), c.frame.getStartLabel(), c.frame.getEndLabel(), c.frame))

            # Create a new array
            if type(varType) is ArrayType:
                if isParam:
                    self.emit.printout(self.emit.emitCLONEARRAY(val.value, varType.eleType, c.frame))
                else:
                    self.emit.printout(self.emit.emitARRAY(varType, c.frame))
                    self.emit.printout(self.emit.emitWRITEVAR(varName, varType, val.value, c.frame))

            if varInit:
                if type(varInit) is ArrayLiteral:
                    self.emit.printout(self.initArray(Symbol(varName,varType,val), varInit, c))
                else:
                    value, _ = self.emit.getConst(varInit)
                    self.emit.printout(self.emit.emitPUSHCONST(value, varType, c.frame))
                    self.emit.printout(self.emit.emitWRITEVAR(varName, varType, val.value, c.frame))
            
        return Symbol(varName, varType, val)
    
    def visitFuncDecl(self, ast, c):
        funcSym = next(filter(lambda x: x.name == ast.name.name, self.infer))

        paramTypes = [paramSym.mtype for paramSym in funcSym.mtype.partype]
        rettype = funcSym.mtype.rettype if type(funcSym.mtype.rettype) is not Unknown else VoidType()

        isMain = ast.name.name == "main" and len(paramTypes) == 0 and type(rettype) is VoidType
        methodname = ast.name.name
        methodtype = MType([ArrayType(StringType())],VoidType()) if isMain else MType(paramTypes, rettype)

        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname, methodtype, True, frame))
        frame.enterScope(True)
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()

        # Parameter and local variable declaration
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", methodtype.partype[0],
                frame.getStartLabel(), frame.getEndLabel(), frame))
        symlist = reduce(lambda acc, ele: [self.visit(ele, MethodEnv(frame, acc))] + acc, ast.param + ast.body[0], c.sym)

        # Body of function
        self.emit.printout(self.emit.emitLABEL(startLabel, frame))
        [self.visit(stmt, MethodEnv(frame, symlist)) for stmt in ast.body[1]]
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))

        if type(rettype) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))

        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return Symbol(methodname, methodtype, CName(self.className))

    def genInit(self, c):
        methodname,methodtype = "<init>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel, frame))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        # Initlialize global variable
        for vardecl in self.globalVarDecl:
            varSym = next(filter(lambda x: x.name == vardecl.variable.name, c.sym))
            varName = varSym.name
            varType = varSym.mtype
            val = varSym.value
            varInit = vardecl.varInit

            # Create a new array
            if type(varType) is ArrayType:
                self.emit.printout(self.emit.emitARRAY(varType, frame))
                self.emit.printout(self.emit.emitPUTSTATIC(f"{val.value}.{varName}", self.getType(varType), frame))

            # Initialize
            if varInit:
                if type(varInit) is ArrayLiteral:
                    self.emit.printout(self.initArray(varSym, varInit, MethodEnv(frame, c.sym)))
                else:
                    value, _ = self.emit.getConst(varInit)
                    self.emit.printout(self.emit.emitPUSHCONST(value, varType, frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(f"{val.value}.{varName}", self.getType(varType), frame))

        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
    
    #################### Statement Visitor ##########################
    def visitAssign(self, ast, c):
        # Assume both side are same type

        rCode, rType = self.visit(ast.rhs, Access(frame=c.frame, sym=c.sym, isLeft=False))
        lCode, lType = self.visit(ast.lhs, Access(frame=c.frame, sym=c.sym, isLeft=True))

        if type(lType) is ArrayType and type(ast.rhs) is ArrayLiteral:
            self.emit.printout(lCode + ''.join(rCode))
        elif type(lType) is not ArrayType and type(ast.lhs) is ArrayCell:
            self.emit.printout(lCode + rCode)
            self.emit.printout(self.emit.emitASTORE(lType, c.frame))
        else:
            self.emit.printout(rCode + lCode)
    
    def visitIf(self, ast, c):
        # All new label
        labels = list(map(lambda x: c.frame.getNewLabel(), ast.ifthenStmt))
        endLabel = c.frame.getNewLabel()
        hasReturnStmt = False

        for block, nextLabel in zip(ast.ifthenStmt, labels):
            self.emit.printout(self.visit(block[0], Access(c.frame, c.sym, False))[0])
            self.emit.printout(self.emit.emitIFFALSE(nextLabel, c.frame))

            symlist = reduce(lambda acc, ele: [self.visit(ele, MethodEnv(c.frame, acc))] + acc, block[1], c.sym)
            hasReturnStmt = True in [self.visit(stmt, MethodEnv(c.frame, symlist)) for stmt in block[2]]
            if not hasReturnStmt:
                self.emit.printout(self.emit.emitGOTO(endLabel, c.frame))
            self.emit.printout(self.emit.emitLABEL(nextLabel, c.frame))

        if ast.elseStmt:
            symlist = reduce(lambda acc, ele: [self.visit(ele, MethodEnv(c.frame, acc))] + acc, ast.elseStmt[0], c.sym)
            hasReturnStmt = True in [self.visit(stmt, MethodEnv(c.frame, symlist)) for stmt in ast.elseStmt[1]] and hasReturnStmt
        
        self.emit.printout(self.emit.emitLABEL(endLabel, c.frame))
        return hasReturnStmt
    
    def visitFor(self, ast, c):
        e1Code, _ = self.visit(ast.expr1, Access(c.frame, c.sym, False))
        e2Code, _ = self.visit(ast.expr2, Access(c.frame, c.sym, False))
        e3Code, _ = self.visit(ast.expr3, Access(c.frame, c.sym, False))
        idWCode, _ = self.visit(ast.idx1, Access(c.frame, c.sym, True))   # Write to ID
        idRCode, _ = self.visit(ast.idx1, Access(c.frame, c.sym, False))  # Read from ID

        # Init ID
        self.emit.printout(e1Code)
        self.emit.printout(idWCode)

        # Loop
        c.frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(c.frame.getContinueLabel(), c.frame))

        # Evaluate condition
        self.emit.printout(e2Code)
        self.emit.printout(self.emit.emitIFFALSE(c.frame.getBreakLabel(), c.frame))
        # Run statement if TRUE
        symlist = reduce(lambda acc, ele: [self.visit(ele, MethodEnv(c.frame, acc))] + acc, ast.loop[0], c.sym)
        hasReturnStmt = True in [self.visit(stmt, MethodEnv(c.frame, symlist)) for stmt in ast.loop[1]]
        # Calculate updateExpr
        self.emit.printout(idRCode)
        self.emit.printout(e3Code)
        self.emit.printout(self.emit.emitADDOP('+', IntType(), c.frame))
        self.emit.printout(idWCode)
        # Continue loop
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))
        
        self.emit.printout(self.emit.emitLABEL(c.frame.getBreakLabel(), c.frame))
        c.frame.exitLoop()
    
    def visitContinue(self, ast, c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))
    
    def visitBreak(self, ast, c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getBreakLabel(), c.frame))
    
    def visitReturn(self, ast, c):
        rettype = c.frame.returnType
        if type(rettype) is not VoidType:
            eCode, eType = self.visit(ast.expr, Access(c.frame, c.sym, False))
            if type(rettype) is FloatType and type(eType) is IntType:
                self.emit.printout(self.emit.emitI2F(c.frame))
            self.emit.printout(eCode)
        self.emit.printout(self.emit.emitRETURN(rettype, c.frame))
        return True
    
    def visitDowhile(self, ast, c):
        exprCode, _ = self.visit(ast.exp, Access(c.frame, c.sym, isLeft=False))
        
        c.frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(c.frame.getContinueLabel(), c.frame))

        symlist = reduce(lambda acc, ele: [self.visit(ele, MethodEnv(c.frame, acc))] + acc, ast.sl[0], c.sym)
        hasReturnStmt = True in [self.visit(stmt, MethodEnv(c.frame, symlist)) for stmt in ast.sl[1]]

        self.emit.printout(exprCode)
        self.emit.printout(self.emit.emitIFFALSE(c.frame.getBreakLabel(), c.frame))

        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))

        self.emit.printout(self.emit.emitLABEL(c.frame.getBreakLabel(), c.frame))
        c.frame.exitLoop()

    def visitWhile(self, ast, c):
        exprCode, _ = self.visit(ast.exp, Access(c.frame, c.sym, isLeft=False))
        
        c.frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(c.frame.getContinueLabel(), c.frame))
        self.emit.printout(exprCode)
        self.emit.printout(self.emit.emitIFFALSE(c.frame.getBreakLabel(), c.frame))
        
        symlist = reduce(lambda acc, ele: [self.visit(ele, MethodEnv(c.frame, acc))] + acc, ast.sl[0], c.sym)
        hasReturnStmt = True in [self.visit(stmt, MethodEnv(c.frame, symlist)) for stmt in ast.sl[1]]
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))

        self.emit.printout(self.emit.emitLABEL(c.frame.getBreakLabel(), c.frame))
        c.frame.exitLoop()

    def visitCallStmt(self, ast, c):
        funcSym = next(filter(lambda x: x.name == ast.method.name, c.sym), None)
        if funcSym is None:
            funcSym = next(filter(lambda x: x.name == ast.method.name, self.infer), None)
            paramTypes = [paramSym.mtype for paramSym in funcSym.mtype.partype]
            funcSym = Symbol(funcSym.name, MType(paramTypes, funcSym.mtype.rettype), funcSym.value)

        methodname = f"{funcSym.value.value}/{funcSym.name}"
        methodtype = funcSym.mtype

        result = [self.visit(param, Access(c.frame, c.sym, False))[0] for param in ast.param]
        result.append(self.emit.emitINVOKESTATIC(methodname, methodtype, c.frame))
        self.emit.printout(''.join(result))
        
    #################### Expression Visitor ##########################
    def visitBinaryOp(self, ast, c):
        if ast.op in ['&&', '||']:
            result = list()

            lCode, _ = self.visit(ast.left, Access(c.frame, c.sym, False))
            result.append(lCode)

            labelF = c.frame.getNewLabel()      # False label
            labelT = c.frame.getNewLabel()      # True label
            labelN = c.frame.getNewLabel()

            # Short-circuit evaluation
            if ast.op == '&&':
                result.append(self.emit.emitIFFALSE(labelF, c.frame))
            else:
                result.append(self.emit.emitIFTRUE(labelT, c.frame))
            
            rCode, _ = self.visit(ast.right, Access(c.frame, c.sym, False))
            result.append(lCode)
            result.append(rCode)

            # Visit both side -> not infer by short-circuit
            if ast.op == '&&':
                result.append(self.emit.emitANDOP(c.frame))
            else:
                result.append(self.emit.emitOROP(c.frame))
            result.append(self.emit.emitGOTO(labelN, c.frame))

            # Short-circuit result
            result.append(self.emit.emitLABEL(labelT, c.frame))
            result.append(self.emit.emitPUSHICONST("true", c.frame))
            result.append(self.emit.emitGOTO(labelN, c.frame))
            result.append(self.emit.emitLABEL(labelF, c.frame))
            result.append(self.emit.emitPUSHICONST("false", c.frame))

            result.append(self.emit.emitLABEL(labelN, c.frame))
            return ''.join(result), BoolType()

        lCode, lType = self.visit(ast.left, Access(c.frame, c.sym, False))
        rCode, rType = self.visit(ast.right, Access(c.frame, c.sym, False))

        typ = IntType()
        if ast.op in ['+.', '-.', '*.', '\\.', '<.', '>.', '<=.', '>=.', '=/='] or \
            (ast.op == '==' and (type(lType) is FloatType or type(rType) is FloatType)):
            if type(lType) is IntType:
                lCode += self.emit.emitI2F(c.frame)
            if type(rType) is IntType:
                rCode += self.emit.emitI2F(c.frame)
            typ = FloatType()
        
        if ast.op in ['+', '-']:
            return lCode + rCode + self.emit.emitADDOP(ast.op, typ, c.frame), IntType()
        elif ast.op in ['+.', '-.']:
            return lCode + rCode + self.emit.emitADDOP(ast.op[0], typ, c.frame), FloatType()
        elif ast.op in ['*', '\\']:
            return lCode + rCode + self.emit.emitMULOP(ast.op, typ, c.frame), IntType()
        elif ast.op in ['*.', '\\.']:
            return lCode + rCode + self.emit.emitMULOP(ast.op[0], typ, c.frame), FloatType()
        elif ast.op == '%':
            return lCode + rCode + self.emit.emitMOD(c.frame), IntType()
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            return lCode + rCode + self.emit.emitREOP(ast.op, typ, c.frame), BoolType()
        elif ast.op in ['<.', '>.', '<=.', '>=.']:
            return lCode + rCode + self.emit.emitREOP(ast.op[:-1], typ, c.frame), BoolType()
        elif ast.op == '=/=':
            return lCode + rCode + self.emit.emitREOP('!=', typ, c.frame), BoolType()
    
    def visitUnaryOp(self, ast, c):
        eCode, eType = self.visit(ast.body, Access(c.frame, c.sym, False))
        if ast.op == '-':
            return eCode + self.emit.emitNEGOP(IntType(), c.frame), IntType()
        elif ast.op == '-.':
            if type(eType) is IntType:
                eCode += self.emit.emitI2F(c.frame)
            return eCode + self.emit.emitNEGOP(FloatType(), c.frame), FloatType()
        elif ast.op == '!':
            return eCode + self.emit.emitNOT(BoolType(), c.frame), BoolType()
    
    def visitCallExpr(self, ast, c):
        funcSym = next(filter(lambda x: x.name == ast.method.name, c.sym), None)
        if funcSym is None:
            funcSym = next(filter(lambda x: x.name == ast.method.name, self.infer), None)
            paramTypes = [paramSym.mtype for paramSym in funcSym.mtype.partype]
            funcSym = Symbol(funcSym.name, MType(paramTypes, funcSym.mtype.rettype), funcSym.value)
    
        methodname = f"{funcSym.value.value}/{funcSym.name}"
        methodtype = funcSym.mtype

        result = [self.visit(param, Access(c.frame, c.sym, False))[0] for param in ast.param]
        result.append(self.emit.emitINVOKESTATIC(methodname, methodtype, c.frame))
        return ''.join(result), methodtype.rettype

    def visitId(self, ast, c):
        sym = next(filter(lambda x: x.name == ast.name, c.sym))
        if type(sym.value) is Index:
            if c.isLeft:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, c.frame), sym.mtype
            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, c.frame), sym.mtype
        else:
            name = f"{sym.value.value}.{sym.name}"
            if c.isLeft:
                return self.emit.emitPUTSTATIC(name, sym.mtype, c.frame), sym.mtype
            return self.emit.emitGETSTATIC(name, sym.mtype, c.frame), sym.mtype
    
    def visitArrayCell(self, ast, c):
        result = list()

        arrCode, arrType = self.visit(ast.arr, Access(c.frame, c.sym, False))
        indexCodes = [self.visit(indexExpr, Access(c.frame, c.sym, False))[0] for indexExpr in ast.idx]

        typ = self.getType(arrType)
        result.append(arrCode)
        for indexCode in indexCodes[:-1]:
            result.append(indexCode)
            result.append(self.emit.emitALOAD(typ.eleType, c.frame))
            typ = typ.eleType
        
        if type(typ.eleType) is not ArrayType and c.isLeft:
            result.append(indexCodes[-1])
        else:
            result.append(indexCodes[-1])
            result.append(self.emit.emitALOAD(typ.eleType, c.frame))

        return ''.join(result), typ.eleType

    #################### Literal Visitor ##########################
    def visitIntLiteral(self, ast, c):
        return self.emit.emitPUSHICONST(ast.value, c.frame), IntType()
    
    def visitFloatLiteral(self, ast, c):
        return self.emit.emitPUSHFCONST(str(ast.value), c.frame), FloatType()
    
    def visitStringLiteral(self, ast, c):
        return self.emit.emitPUSHCONST(ast.value, StringType(), c.frame), StringType()

    def visitBooleanLiteral(self, ast, c):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), c.frame), BoolType()
    
    def visitArrayLiteral(self, ast, c):
        return self.storeArray(ast, c), ArrayType(None)


################################# Static Check Visitor #############################################
class StaticChecker(BaseVisitor):
    def __init__(self,ast,envi):
        self.ast = ast
        self.global_envi = envi
        self.first_runtime = True

    ############################# Helper Function #####################################
    def get_kind(self, ast):
        return Function() if type(ast) == FuncDecl else Variable()

    def get_type(self, symbol):
        if type(symbol) == tuple:
            symbol = symbol[0]
        if type(symbol.mtype) == MType:  
            return symbol.mtype.rettype
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
            symbol.mtype.rettype = inferType
        elif type(symbol.mtype) == ArrayType:
            symbol.mtype.eleType = inferType
        else:
            symbol.mtype = inferType

    def infer_type_by_symbol(self, ast, leftSym, rightSym):
        if type(leftSym) == tuple or type(rightSym) == tuple or type(leftSym.mtype) == ArrayType or type(rightSym.mtype) == ArrayType:
            return self.infer_array_type(ast, leftSym, rightSym)
        leftType = self.get_type(leftSym)
        rightType = self.get_type(rightSym)

        if type(leftType) == Unknown:
            if type(rightType) == Unknown and isinstance(ast, Stmt):
                return None
            self.infer_type_by_type(leftSym, rightType)
        elif type(leftType) != type(rightType):
            if type(rightType) == Unknown:
                self.infer_type_by_type(rightSym, leftType)
    
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
            leftType = ArrayType(leftType.eleType, leftType.dimen[leftIdx:]) \
                                if leftIdx < len(leftType.dimen) \
                                else leftType.eleType
        if rightIdx is not None:
            rightType = ArrayType(rightType.eleType, rightType.dimen[leftIdx:]) \
                                if rightIdx < len(rightType.dimen) \
                                else rightType.eleType

        # Infer array type
        if type(leftType) == ArrayType and type(rightType) == ArrayType and leftType.dimen == rightType.dimen:
            if type(leftType.eleType) is Unknown:
                if type(rightType.eleType) is Unknown and isinstance(ast, Stmt):
                    return None
                self.infer_type_by_type(leftSym, rightType.eleType)
            elif type(leftType.eleType) != type(rightType.eleType):
                if type(rightType.eleType) == Unknown:
                    self.infer_type_by_type(rightSym, leftType.eleType)
        elif type(leftType) == Unknown:
            if type(leftSym.mtype) == MType:
                leftSym.mtype.rettype = rightType
            elif type(leftSym.mtype) == ArrayType:
                leftSym.mtype.eleType = rightType
        elif type(rightType) == Unknown:
            if type(rightSym.mtype) == MType:
                rightSym.mtype.rettype = rightType
            elif type(rightSym.mtype) == ArrayType:
                rightSym.mtype.eleType = leftType

        leftType = self.get_type(leftSym)
        rightType = self.get_type(rightSym)


        if leftIdx is not None:
            leftType = ArrayType(leftType.eleType, leftType.dimen[leftIdx:]) \
                                if leftIdx < len(leftType.dimen) \
                                else leftType.eleType
        if rightIdx is not None:
            rightType = ArrayType(rightType.eleType, rightType.dimen[leftIdx:]) \
                                if rightIdx < len(rightType.dimen) \
                                else rightType.eleType

    def is_inferred(self, symbol):
        # Return TRUE if fully inferred, FALSE otherwise
        if type(symbol.mtype) == Unknown:
            return False
        elif type(symbol.mtype) == MType:
            return all([self.is_inferred(param) for param in symbol.mtype.partype])
        elif type(symbol.mtype) == ArrayType and type(symbol.mtype.eleType) == Unknown:
            return False
        return True
    ##################################################################################
    def visitProgram(self,ast, c):
        c = [self.global_envi]
        [self.visit(decl, (c, self.get_kind(decl))) for decl in ast.decl]

        # Second run
        self.first_runtime = False
        [self.visit(decl, (c, self.get_kind(decl))) for decl in ast.decl if isinstance(decl, FuncDecl)]
        return c[0]

    def visitVarDecl(self, ast, c):
        kind = c[1]
        c = c[0]

        name = ast.variable.name
        if len(ast.varDimen) > 0:
            if ast.varInit is None:
                typ = ArrayType(Unknown(), ast.varDimen)
                c[0] = [Symbol(ast.variable.name, typ)] + c[0]
            else:
                typ = self.visit(ast.varInit, None).mtype
                c[0] = [Symbol(ast.variable.name, typ)] + c[0]
        else:
            if ast.varInit is None:
                typ = Unknown()
                c[0] = [Symbol(ast.variable.name, typ)] + c[0]
            else:
                typ = self.visit(ast.varInit, None).mtype
                c[0] = [Symbol(ast.variable.name, typ)] + c[0]
        
    def visitFuncDecl(self, ast, c):
        kind = c[1]
        c = c[0]

        if self.first_runtime:
            # Traverse parameters
            new_c = [[]]
            [self.visit(param, (new_c, Parameter())) for param in ast.param]    # Special flag for parameter declaration

            # Add FuncDecl to environment
            func_sym = Symbol(ast.name.name, MType(new_c[0][::-1], Unknown()))
            c[0] = [func_sym] + c[0]
            return None

        func_sym = self.get_symbol_by_name(ast.name.name, c)

        # Traver body of function
        local_c = [func_sym.mtype.partype]
        [self.visit(decl, (local_c, self.get_kind(decl))) for decl in ast.body[0]]
        local_len = len(local_c[0]) - len(func_sym.mtype.partype)
        new_c = [local_c[0][:local_len]] + c
        [self.visit(stmt, (new_c, func_sym)) for stmt in ast.body[1]]

    #################### Statement Visitor ##########################
    def visitAssign(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        lhs = self.visit(ast.lhs, c)
        rhs = self.visit(ast.rhs, c)

        # Left hand side must not be VoidType
        self.infer_type_by_symbol(ast, lhs, rhs)
    
    def visitIf(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        cond_syms = [self.visit(block[0], c) for block in ast.ifthenStmt]
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

        # Get return type of Return Statement and infer rettype
        rettype_sym = self.visit(ast.expr, c) if ast.expr is not None else Symbol(None, VoidType())
        self.infer_type_by_symbol(ast, func_sym, rettype_sym)
    
    def visitDowhile(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        # Visit body of DoWhile statement with new scope
        new_c = [[]] + envi
        [self.visit(decl, (new_c, self.get_kind(decl))) for decl in ast.sl[0]]
        [self.visit(stmt, (new_c, func_sym)) for stmt in ast.sl[1]]

        # Get condition expression symbol and infer type
        expr = self.visit(ast.exp, c)
        self.infer_type_by_symbol(ast, expr, Symbol(None, BoolType()))

    def visitWhile(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        # Get condition expression symbol and infer type
        expr = self.visit(ast.exp, c)
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

        # Infer parameter types and check type compatibility
        arg_syms = [self.visit(arg, c) for arg in ast.param]
        param_syms = func_sym.mtype.partype
        [self.infer_type_by_symbol(ast, arg, param) for arg, param in zip(arg_syms, param_syms)]
        
    #################### Expression Visitor ##########################
    def visitBinaryOp(self, ast, c):
        leftSym = self.visit(ast.left, c)
        rightSym = self.visit(ast.right, c)

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

        # Infer parameter types and check type compatibility
        arg_syms = [self.visit(arg, c) for arg in ast.param]
        param_syms = func_sym.mtype.partype
        [self.infer_type_by_symbol(ast, arg, param) for arg, param in zip(arg_syms, param_syms)]
        return func_sym

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
                        return None
                    elif type(kind) == Identifier:
                        if type(sym.mtype) == MType:
                            for param in sym.mtype.partype:
                                if param.name == ast.name:
                                    if type(kind) == Identifier:
                                        return param
                                    return None
                            return None
                    return sym
                elif sym.name == func_sym.name:
                    for param in sym.mtype.partype:
                        if param.name == ast.name:
                            if type(kind) == Identifier:
                                return param
                            return None
        return None
    
    def visitArrayCell(self, ast, c):
        func_sym = c[1]
        envi = c[0]

        arr = self.visit(ast.arr, c)
        arr_type = self.get_type(arr)

        if len(arr_type.dimen) < len(ast.idx):
            raise IndexOutOfRange(ast)

        expr_syms = [self.visit(expr, c) for expr in ast.idx]
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
        return Symbol(None, ArrayType(res.mtype.eleType, [len(ast.value)] + res.mtype.dimen)) \
                            if type(res.mtype) == ArrayType \
                            else Symbol(None, ArrayType(res.mtype, [len(ast.value)]))