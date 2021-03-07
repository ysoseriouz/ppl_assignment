import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    ############################ Test global declaration part #############################
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_valid_global_declaration_with_initialization(self):
        input = \
r"""
Var: x = 1;
"""
        expect = Program([VarDecl(Id('x'), [], IntLiteral(1))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))
    
    def test_full_valid_program_inline(self):
        input = \
r"""
Var: m, n[10]; Function: fact Parameter: n Body: If n == 0 Then Return 1; Else Return n * fact (n-1); EndIf. EndBody.
"""
        expect = Program([
            VarDecl(Id('m'),[],None),
            VarDecl(Id('n'),[10],None),
            FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],(
                [],
                [
                    If(
                        [
                            (
                                BinaryOp(
                                    '==',
                                    Id('n'),
                                    IntLiteral(0)
                                ),
                                [],
                                [Return(IntLiteral(1))]
                            )
                        ],
                        (
                            [],
                            [
                                Return(
                                    BinaryOp(
                                        '*',
                                        Id('n'),
                                        CallExpr(
                                            Id('fact'),
                                            [BinaryOp('-',Id('n'),IntLiteral(1))]
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_valid_global_declaration_with_array_initialization(self):
        input = \
r"""
Var: a[2][2] = {{1, 2}, {3, 4}};
"""
        expect = Program([
            VarDecl(Id('a'),[2,2],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]), ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_valid_global_declaration_with_different_literal_types_in_array(self):
        input = \
r"""
Var: b[2][2] = {{True, 2}, {2.8, "gg"}};
"""
        expect = Program([
            VarDecl(Id('b'),[2,2],ArrayLiteral([ArrayLiteral([BooleanLiteral(True),IntLiteral(2)]), ArrayLiteral([FloatLiteral(2.8),StringLiteral("gg")])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_valid_normal_global_declaration(self):
        input = \
r"""
Var: x, y, z[2][4];
"""
        expect = Program([
            VarDecl(Id('x'),[],None),
            VarDecl(Id('y'),[],None),
            VarDecl(Id('z'),[2, 4],None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_valid_global_declaration_with_function_call_initialization(self):
        input = \
r"""
Function: main
Body:
    Var: a;
    a = id();
EndBody.
"""
        expect = Program([
            FuncDecl(Id('main'),[],(
                [VarDecl(Id('a'),[],None)],
                [Assign(Id('a'),CallExpr(Id('id'),[]))]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))
    
    def test_multiple_variable_declarations(self):
        input = r"""Var: x; Var: y; Var: z[4]=5;"""
        expect = Program([
            VarDecl(Id('x'),[],None),
            VarDecl(Id('y'),[],None),
            VarDecl(Id('z'),[4],IntLiteral(5))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))
    
    def test_empty_array_declaration(self):
        input = \
r"""
Var: a, b[1], c = 0;
Var: arr[2] = {};
"""
        expect = Program([
            VarDecl(Id('a'),[],None),
            VarDecl(Id('b'),[1],None),
            VarDecl(Id('c'),[],IntLiteral(0)),
            VarDecl(Id('arr'),[2],ArrayLiteral([]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))
    
    def test_complex_array_declaration(self):
        input = \
r"""
Var: a[0x1][0o7][56] = {"True", True}, literal, array;
"""
        expect = Program([
            VarDecl(Id('a'),[1,7,56],ArrayLiteral([StringLiteral('True'),BooleanLiteral(True)])),
            VarDecl(Id('literal'),[],None),VarDecl(Id('array'),[],None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_hex_integer(self):
        input = \
r"""
Var: a = 0xF;
"""
        expect = Program([
            VarDecl(Id('a'),[],IntLiteral(0xF)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))
    
    def test_octal_integer(self):
        input = \
r"""
Var: a = 0o1234;
"""
        expect = Program([
            VarDecl(Id('a'),[],IntLiteral(0o1234)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))
    
    def test_float_number_1(self):
        input = \
r"""
Var: a = 0.123;
"""
        expect = Program([
            VarDecl(Id('a'),[],FloatLiteral(0.123)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))
    
    def test_float_number_2(self):
        input = \
r"""
Var: a = 12.0e3;
"""
        expect = Program([
            VarDecl(Id('a'),[],FloatLiteral(12.0e3)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_float_number_3(self):
        input = \
r"""
Var: a = 12.e5;
"""
        expect = Program([
            VarDecl(Id('a'),[],FloatLiteral(12.e5)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))
    
    def test_float_number_4(self):
        input = \
r"""
Var: a = 12000.;
"""
        expect = Program([
            VarDecl(Id('a'),[],FloatLiteral(12000.)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))
    
    def test_float_number_5(self):
        input = \
r"""
Var: a = 12000e-1;
"""
        expect = Program([
            VarDecl(Id('a'),[],FloatLiteral(12000e-1)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))
    
    def test_float_number_6(self):
        input = \
r"""
Var: a = 12000E-1;
"""
        expect = Program([
            VarDecl(Id('a'),[],FloatLiteral(12000E-1)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))
    
    def test_float_number_7(self):
        input = \
r"""
Var: a = 120.00E+2;
"""
        expect = Program([
            VarDecl(Id('a'),[],FloatLiteral(120.00E+2)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))
    
    def test_string_declaration_1(self):
        input = \
r"""
Var: a = "This is a string containing tab \t";
"""
        expect = Program([
            VarDecl(Id('a'),[],StringLiteral("This is a string containing tab \\t")),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))
    
    def test_string_declaration_2(self):
        input = \
"""
Var: a = "\t8\t";
"""
        expect = Program([
            VarDecl(Id('a'),[],StringLiteral("\t8\t")),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))
    
    def test_string_declaration_3(self):
        input = \
r"""
Var: a = "He asked me: '"Where is John?'"";
"""
        expect = Program([
            VarDecl(Id('a'),[],StringLiteral("He asked me: '\"Where is John?'\"")),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))
    
    def test_dimension(self):
        input = \
r"""
Function: main
Body:
    Return a[3][0][-4];
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),
                [],
                (
                    [],
                    [Return(
                        ArrayCell(
                            Id('a'),
                            [
                                IntLiteral(3),
                                IntLiteral(0),
                                UnaryOp('-',IntLiteral(4))
                            ]
                        )
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    ############################ Test function declaration part ###########################
    def test_comment_inside_function(self):
        input = \
r"""
Function: main
Body:
    a = ** comment goes here **  6*6;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            BinaryOp('*',IntLiteral(6),IntLiteral(6)))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_valid_normal_function_declaration(self):
        input = \
r"""
Function: test 
Body: 
    If n > 10 Then 
        Return 5; 
    Else 
        Return True; 
    EndIf.
EndBody
.
"""
        expect = Program([
            FuncDecl(Id('test'),[],(
                [],
                [
                    If(
                        [
                            (BinaryOp('>',Id('n'),IntLiteral(10)),[],[Return(IntLiteral(5))])
                        ],
                        ([],[Return(BooleanLiteral(True))])
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_many_function_declarations(self):
        input = \
r"""
Function: test1 
Parameter: n 
Body: 
    If n > 10 Then 
        Return 5; 
    Else Return True; 
    EndIf. 
EndBody. 

Function: test2 
Parameter: n 
Body: 
    If n > 10 Then Return 5; 
    Else Return True; 
    EndIf. 
EndBody.
"""
        expect = Program([
            FuncDecl(Id('test1'),[VarDecl(Id('n'),[],None)],(
                [],
                [
                    If(
                        [
                            (BinaryOp('>',Id('n'),IntLiteral(10)),[],[Return(IntLiteral(5))])
                        ],
                        ([],[Return(BooleanLiteral(True))])
                    )
                ]
            )),
            FuncDecl(Id('test2'),[VarDecl(Id('n'),[],None)],(
                [],
                [
                    If(
                        [
                            (BinaryOp('>',Id('n'),IntLiteral(10)),[],[Return(IntLiteral(5))])
                        ],
                        ([],[Return(BooleanLiteral(True))])
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_valid_empty_program(self):
        input = \
r"""
** @Author: Nguyen Tien Thanh - 1852740 **
** This should be
 * an empty
 * program
**
"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_valid_function_with_empty_body(self):
        input = \
r"""
Function: foo 
Body: 
EndBody.
"""
        expect = Program([
            FuncDecl(Id('foo'),[],([],[]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    ############################ Test expression #############################
    def test_variable_declaration(self):
        input = \
r"""
Function: test 
Body: 
    Var: x,y,z;
EndBody.
"""
        expect = Program([
            FuncDecl(Id('test'),[],(
                [
                    VarDecl(Id('x'),[],None),
                    VarDecl(Id('y'),[],None),
                    VarDecl(Id('z'),[],None)
                ],[]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_variable_declaration_with_array_initialization(self):
        input = \
r"""
Function: test 
Body: 
    Var: a;
    a = {1, 2.0};
EndBody.
"""
        expect = Program([
            FuncDecl(Id('test'),[],(
                [
                    VarDecl(Id('a'),[],None),
                ],[
                    Assign(Id('a'),ArrayLiteral([IntLiteral(1),FloatLiteral(2.0)]))
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_relational_expression(self):
        input = \
r"""
Function: test
Body: 
    Var: a, b, c;
    a = a > b; 
    b = a >= c; 
EndBody.
"""
        expect = Program([
            FuncDecl(Id('test'),[],(
                [
                    VarDecl(Id('a'),[],None),
                    VarDecl(Id('b'),[],None),
                    VarDecl(Id('c'),[],None),
                ],[
                    Assign(Id('a'),BinaryOp('>',Id('a'),Id('b'))),
                    Assign(Id('b'),BinaryOp('>=',Id('a'),Id('c'))),
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_complicated_expression(self):
        input = \
r"""
Function: test
Body: 
    Var: a;
    a = a >= b || c +. d + -e;
EndBody.
"""
        expect = Program([
            FuncDecl(Id('test'),[],(
                [
                    VarDecl(Id('a'),[],None)
                ],[
                    Assign(
                        Id('a'),
                        BinaryOp(
                            '>=',
                            Id('a'),
                            BinaryOp(
                                '||',
                                Id('b'),
                                BinaryOp(
                                    '+',
                                    BinaryOp('+.',Id('c'),Id('d')),
                                    UnaryOp('-',Id('e'))
                                )
                            )
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))
    
    def test_a_weird_mix_expression(self):
        input = \
r"""
Function: test
Body: 
    Var: x;
    x = -{1, 2, 3};
EndBody.
"""
        expect = Program([
            FuncDecl(Id('test'),[],(
                [
                    VarDecl(Id('x'),[],None)
                ],[
                    Assign(
                        Id('x'),
                        UnaryOp(
                            '-',
                            ArrayLiteral([
                                IntLiteral(1),
                                IntLiteral(2),
                                IntLiteral(3)
                            ])
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))
    
    def test_another_weird_mix_expression(self):
        input = \
r"""
Function: test
Body: 
    Var: x;
    x = -True;
EndBody.
"""
        expect = Program([
            FuncDecl(Id('test'),[],(
                [
                    VarDecl(Id('x'),[],None)
                ],[
                    Assign(
                        Id('x'),
                        UnaryOp(
                            '-',
                            BooleanLiteral(True)
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))
    
    def test_negative_arithmetic_expression(self):
        input = \
r"""
Function: test
Body: 
    Var: x;
    x = -12.6;
EndBody.
"""
        expect = Program([
            FuncDecl(Id('test'),[],(
                [
                    VarDecl(Id('x'),[],None)
                ],[
                    Assign(
                        Id('x'),
                        UnaryOp(
                            '-',
                            FloatLiteral(12.6)
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_not_operator(self):
        input = \
r"""
Function: test
Body: 
    Var: x;
    x = !True;
EndBody.
"""
        expect = Program([
            FuncDecl(Id('test'),[],(
                [
                    VarDecl(Id('x'),[],None)
                ],[
                    Assign(
                        Id('x'),
                        UnaryOp(
                            '!',
                            BooleanLiteral(True)
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))
    
    def test_function_call_expression(self):
        input = \
r"""
Function: test
Body: 
    Var: a, b, c;
    a = test();
    b = para(x, y);
EndBody.
"""
        expect = Program([
            FuncDecl(Id('test'),[],(
                [
                    VarDecl(Id('a'),[],None),
                    VarDecl(Id('b'),[],None),
                    VarDecl(Id('c'),[],None),
                ],[
                    Assign(
                        Id('a'),
                        CallExpr(
                            Id('test'),
                            []
                        )
                    ),
                    Assign(
                        Id('b'),
                        CallExpr(
                            Id('para'),
                            [
                                Id('x'),
                                Id('y')
                            ]
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))
    
    def test_operation_with_array_literal(self):
        input = \
r"""
Function: main
Body:
    Var: a;
    a = {1, 2, 3} - {1, 2, 3};
EndBody.
"""
        expect = Program([
            FuncDecl(Id('main'),[],(
                [
                    VarDecl(Id('a'),[],None),
                ],[
                    Assign(
                        Id('a'),
                        BinaryOp(
                            '-',
                            ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),
                            ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_operation_with_string_literal(self):
        input = \
r"""
Function: main
Body:
    Var: a;
    a = "Hello" \ "ello";
EndBody.
"""
        expect = Program([
            FuncDecl(Id('main'),[],(
                [
                    VarDecl(Id('a'),[],None),
                ],[
                    Assign(
                        Id('a'),
                        BinaryOp(
                            '\\',
                            StringLiteral("Hello"),
                            StringLiteral("ello")
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_operation_with_two_different_literal_types_1(self):
        input = \
r"""
Function: main
Body:
    Var: a;
    a = 1 % True;
EndBody.
"""
        expect = Program([
            FuncDecl(Id('main'),[],(
                [
                    VarDecl(Id('a'),[],None),
                ],[
                    Assign(
                        Id('a'),
                        BinaryOp(
                            '%',
                            IntLiteral(1),
                            BooleanLiteral(True)
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_operation_with_two_different_literal_types_2(self):
        input = \
r"""
Function: main
Body:
    Var: a;
    a = a && "Hello world!";
EndBody.
"""
        expect = Program([
            FuncDecl(Id('main'),[],(
                [
                    VarDecl(Id('a'),[],None),
                ],[
                    Assign(
                        Id('a'),
                        BinaryOp(
                            '&&',
                            Id('a'),
                            StringLiteral("Hello world!")
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_index_operator(self):
        input = \
r"""
Function: main
Body:
    a[3 + foo(2)] = a[b[2][3]] - 4;
EndBody.
"""
        expect = Program([
            FuncDecl(Id('main'),[],(
                [],[
                    Assign(
                        ArrayCell(
                            Id('a'),
                            [
                                BinaryOp(
                                    '+',
                                    IntLiteral(3),
                                    CallExpr(Id('foo'),[IntLiteral(2)])
                                )
                            ]
                        ),
                        BinaryOp(
                            '-',
                            ArrayCell(
                                Id('a'),
                                [ArrayCell(
                                    Id('b'),
                                    [IntLiteral(2),IntLiteral(3)]
                                )]
                            ),
                            IntLiteral(4)
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))
    
    def test_logical_expression_inside_function(self):
        input = \
r"""
Function: test
Body: 
    n = a || b || c; 
EndBody.
"""
        expect = Program([
            FuncDecl(Id('test'),[],(
                [],[
                    Assign(
                        Id('n'),
                        BinaryOp(
                            '||',
                            BinaryOp(
                                '||',
                                Id('a'),
                                Id('b')
                            ),
                            Id('c')
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))
    
    ############################ Test statement #############################
    def test_while_loop_statement(self):
        input = \
r"""
Function: foo 
Parameter: a, c 
Body: 
    While i <= 4 Do 
        print(i); 
    EndWhile. 
    Return a + c; 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [
                    VarDecl(Id('a'),[],None),
                    VarDecl(Id('c'),[],None)
                ],
                (
                    [],
                    [
                        While(
                            BinaryOp('<=',Id('i'),IntLiteral(4)),(
                                [],[
                                    CallStmt(Id('print'),[Id('i')])
                                ]
                            )
                        ),
                        Return(BinaryOp('+',Id('a'),Id('c')))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))
    
    def test_weird_while_statement(self):
        input = \
r"""
Function: main
Body:
    While True Do
    While False Do
    While "True" Do
    
    EndWhile.
    EndWhile.
    EndWhile.
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        While(
                            BooleanLiteral(True),
                            (
                                [],
                                [
                                    While(
                                        BooleanLiteral(False),
                                        (
                                            [],
                                            [
                                                While(
                                                    StringLiteral('True'),
                                                    ([],[])
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_do_while_statement(self):
        input = \
r"""
Function: foo 
Parameter: a, c 
Body: 
    Do 
        print(i); 
    While i <= 4
    EndDo.
    Return a + c; 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [
                    VarDecl(Id('a'),[],None),
                    VarDecl(Id('c'),[],None)
                ],
                (
                    [],
                    [
                        Dowhile(
                            (
                                [],
                                [
                                    CallStmt(Id('print'),[Id('i')])
                                ]
                            ),
                            BinaryOp(
                                '<=',
                                Id('i'),
                                IntLiteral(4)
                            )
                        ),
                        Return(BinaryOp('+',Id('a'),Id('c')))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_break_statement(self):
        input = \
r"""
Function: foo 
Parameter: a, c 
Body: 
    Do 
        print(i); 
        If i >= 99 Then Break; 
        EndIf. 
    While i <= 4
    EndDo. 
    Return a + c; 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [
                    VarDecl(Id('a'),[],None),
                    VarDecl(Id('c'),[],None)
                ],
                (
                    [],
                    [
                        Dowhile(
                            (
                                [],
                                [
                                    CallStmt(Id('print'),[Id('i')]),
                                    If(
                                        [(
                                            BinaryOp(
                                                '>=',
                                                Id('i'),
                                                IntLiteral(99)
                                            ),
                                            [],
                                            [Break()]
                                        )],
                                        ([],[])
                                    )
                                ]
                            ),
                            BinaryOp(
                                '<=',
                                Id('i'),
                                IntLiteral(4)
                            )
                        ),
                        Return(BinaryOp('+',Id('a'),Id('c')))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_continue_statement(self):
        input = \
r"""
Function: foo 
Parameter: a, c 
Body: 
    Do 
        print(i); 
        If i >= 99 Then Continue; 
        EndIf.
    While (i <= 4)
    EndDo. 
    Return a + c; 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [
                    VarDecl(Id('a'),[],None),
                    VarDecl(Id('c'),[],None)
                ],
                (
                    [],
                    [
                        Dowhile(
                            (
                                [],
                                [
                                    CallStmt(Id('print'),[Id('i')]),
                                    If(
                                        [(
                                            BinaryOp(
                                                '>=',
                                                Id('i'),
                                                IntLiteral(99)
                                            ),
                                            [],
                                            [Continue()]
                                        )],
                                        ([],[])
                                    )
                                ]
                            ),
                            BinaryOp(
                                '<=',
                                Id('i'),
                                IntLiteral(4)
                            )
                        ),
                        Return(BinaryOp('+',Id('a'),Id('c')))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_if_statement(self):
        input = \
r"""
Var: m, n[10]; 
Function: fact 
Parameter: n 
Body: 
    If n + 1 Then 
        Return 1; 
    ElseIf n 
        Then Return "abc"; 
    Else 
        Return True; 
    EndIf. 
EndBody.
"""
        expect = Program([
            VarDecl(Id('m'),[],None),
            VarDecl(Id('n'),[10],None),
            FuncDecl(
                Id('fact'),
                [
                    VarDecl(Id('n'),[],None)
                ],
                (
                    [],
                    [
                        If(
                            [
                                (
                                    BinaryOp('+',Id('n'),IntLiteral(1)),
                                    [],
                                    [Return(IntLiteral(1))]
                                ),(
                                    Id('n'),
                                    [],
                                    [Return(StringLiteral("abc"))]
                                )
                            ],
                            ([],[Return(BooleanLiteral(True))])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))
    
    def test_for_loop_statement(self):
        input = \
r"""
Function: foo 
Parameter: a, c 
Body: 
    For (i = 1, i <= 4, 1) Do 
        print(i);
    EndFor. 
    Return a + c; 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [
                    VarDecl(Id('a'),[],None),
                    VarDecl(Id('c'),[],None)
                ],
                (
                    [],
                    [
                        For(
                            Id('i'),
                            IntLiteral(1),
                            BinaryOp('<=',Id('i'),IntLiteral(4)),
                            IntLiteral(1),
                            (
                                [],
                                [
                                    CallStmt(Id('print'),[Id('i')])
                                ]
                            )
                        ),
                        Return(BinaryOp('+',Id('a'),Id('c')))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))
    
    def test_complex_for_loop_1(self):
        input = \
r"""
Function: main
Body:
    For(i = i == 0, f % 4, c) Do
        e[2][3][4] = t[6][7][8];
    EndFor.
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        For(
                            Id('i'),
                            BinaryOp(
                                '==',
                                Id('i'),
                                IntLiteral(0)
                            ),
                            BinaryOp(
                                '%',
                                Id('f'),
                                IntLiteral(4)
                            ),
                            Id('c'),
                            (
                                [],
                                [
                                    Assign(
                                        ArrayCell(
                                            Id('e'),
                                            [
                                                IntLiteral(2),
                                                IntLiteral(3),
                                                IntLiteral(4)
                                            ]
                                        ),
                                        ArrayCell(
                                            Id('t'),
                                            [
                                                IntLiteral(6),
                                                IntLiteral(7),
                                                IntLiteral(8)
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))
    
    def test_complex_for_loop_2(self):
        input = \
r"""
Function: main
Body:
    For (i = foo()[1], i < foo(2,{1,2,3},4), {{3}}) Do
    EndFor.
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        For(
                            Id('i'),
                            ArrayCell(
                                CallExpr(Id('foo'),[]),
                                [IntLiteral(1)]
                            ),
                            BinaryOp(
                                '<',
                                Id('i'),
                                CallExpr(
                                    Id('foo'),
                                    [
                                        IntLiteral(2),
                                        ArrayLiteral(
                                            [
                                                IntLiteral(1),
                                                IntLiteral(2),
                                                IntLiteral(3)
                                            ]
                                        ),
                                        IntLiteral(4)
                                    ]
                                )
                            ),
                            ArrayLiteral([ArrayLiteral([IntLiteral(3)])]),
                            ([],[])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))
    
    def test_weird_for_loops(self):
        input = \
r"""
Function: main
Body:
    Var: i;
    For(i=0,i<10,1) Do
    Var: i;
    For(i=0,i<10,1) Do
    Var: i;
    For(i=0,i<10,1) Do

    EndFor.
    EndFor.
    EndFor.
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [
                        VarDecl(Id('i'),[],None)
                    ],
                    [
                        For(
                            Id('i'),
                            IntLiteral(0),
                            BinaryOp('<',Id('i'),IntLiteral(10)),
                            IntLiteral(1),
                            (
                                [
                                    VarDecl(Id('i'),[],None)
                                ],
                                [
                                    For(
                                        Id('i'),
                                        IntLiteral(0),
                                        BinaryOp(
                                            '<',
                                            Id('i'),
                                            IntLiteral(10)
                                        ),
                                        IntLiteral(1),
                                        (
                                            [
                                                VarDecl(Id('i'),[],None)
                                            ],
                                            [
                                                For(
                                                    Id('i'),
                                                    IntLiteral(0),
                                                    BinaryOp(
                                                        '<',
                                                        Id('i'),
                                                        IntLiteral(10)
                                                    ),
                                                    IntLiteral(1),
                                                    ([],[])
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_function_call_as_iter_condition(self):
        input = \
r"""
Function: foo 
Parameter: a, c 
Body: 
    Do 
        print(i); 
    While (foo()) 
    EndDo. 
    Return a + c;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [
                    VarDecl(Id('a'),[],None),
                    VarDecl(Id('c'),[],None)
                ],
                (
                    [],
                    [
                        Dowhile(
                            (
                                [],
                                [CallStmt(Id('print'),[Id('i')])]
                            ),
                            CallExpr(Id('foo'),[])
                        ),
                        Return(BinaryOp('+',Id('a'),Id('c')))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))
    
    def test_function_call_many_arguments_1(self):
        input = \
r"""
Function: main
Body: 
    foo(2, 3e-4, "rt", True);
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),
                [],
                (
                    [],
                    [
                        CallStmt(
                            Id('foo'),
                            [
                                IntLiteral(2),
                                FloatLiteral(3e-4),
                                StringLiteral("rt"),
                                BooleanLiteral(True)
                            ]
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))
    
    def test_function_call_many_arguments_2(self):
        input = \
r"""
Function: main
Body:
    foo(!r, 5+6, 7&&6%4==1);
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        CallStmt(
                            Id('foo'),
                            [
                                UnaryOp(
                                    '!',
                                    Id('r')
                                ),
                                BinaryOp(
                                    '+',
                                    IntLiteral(5),
                                    IntLiteral(6)
                                ),
                                BinaryOp(
                                    '==',
                                    BinaryOp(
                                        '&&',
                                        IntLiteral(7),
                                        BinaryOp(
                                            '%',
                                            IntLiteral(6),
                                            IntLiteral(4)
                                        )
                                    ),
                                    IntLiteral(1)
                                )
                            ]
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_nested_function_call(self):
        input = \
r"""
Function: fc 
Body: 
    foo(test(f(a, b, c))); 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('fc'),[],
                (
                    [],
                    [
                        CallStmt(
                            Id('foo'),
                            [CallExpr(Id('test'),[CallExpr(Id('f'),[Id('a'),Id('b'),Id('c')])])]
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))
    
    def test_return_none_statement(self):
        input = \
r"""
Function: main
Body: 
    Return;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [Return(None)]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))
    
    def test_complex_return_statement_1(self):
        input = \
r"""
Function: main
Body:
    Return {1,2,3}[x];
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Return(
                            ArrayCell(
                                ArrayLiteral(
                                    [
                                        IntLiteral(1),
                                        IntLiteral(2),
                                        IntLiteral(3)
                                    ]
                                ),
                                [Id('x')]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))
    
    def test_complex_return_statement_2(self):
        input = \
r"""
Function: main
Body:
    Return {2,4,5,6}[2];
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Return(
                            ArrayCell(
                                ArrayLiteral(
                                    [
                                        IntLiteral(2),
                                        IntLiteral(4),
                                        IntLiteral(5),
                                        IntLiteral(6)
                                    ]
                                ),
                                [IntLiteral(2)]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))
    
    def test_complex_return_statement_3(self):
        input = \
r"""
Function: main
Parameter: a[2][4], b[2]
Body:
    Return a[x][y] == b[4];
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),
                [
                    VarDecl(Id('a'),[2,4],None),
                    VarDecl(Id('b'),[2],None)
                ],
                (
                    [],
                    [
                        Return(
                            BinaryOp(
                                '==',
                                ArrayCell(
                                    Id('a'),
                                    [
                                        Id('x'),
                                        Id('y')
                                    ]
                                ),
                                ArrayCell(
                                    Id('b'),
                                    [IntLiteral(4)]
                                )
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))
    
    def test_complex_assignment_statement_1(self):
        input = \
r"""
Function: main
Body:
    ((--w[2])[3][8])[7][9] = a;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Assign(
                            ArrayCell(
                                ArrayCell(
                                    UnaryOp(
                                        '-',
                                        UnaryOp(
                                            '-',
                                            ArrayCell(
                                                Id('w'),
                                                [IntLiteral(2)]
                                            )
                                        )
                                    ),
                                    [
                                        IntLiteral(3),
                                        IntLiteral(8)
                                    ]
                                ),
                                [
                                    IntLiteral(7),
                                    IntLiteral(9)
                                ]
                            ),
                            Id('a')
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))
    
    def test_complex_assignment_statement_2(self):
        input = \
r"""
Function: main
Body:
    5[4][3][2] = b[4];
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Assign(
                            ArrayCell(
                                IntLiteral(5),
                                [
                                    IntLiteral(4),
                                    IntLiteral(3),
                                    IntLiteral(2)
                                ]
                            ),
                            ArrayCell(
                                Id('b'),
                                [IntLiteral(4)]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))
    
    def test_complex_assignment_statement_3(self):
        input = \
r"""
Function: main
Body:
    foo()[3] = a;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Assign(
                            ArrayCell(
                                CallExpr(
                                    Id('foo'),
                                    []
                                ),
                                [IntLiteral(3)]
                            ),
                            Id('a')
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))
    
    def test_complex_assignment_statement_4(self):
        input = \
r"""
Function: main
Body:
    foo()[a<b] = 0;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Assign(
                            ArrayCell(
                                CallExpr(
                                    Id('foo'),
                                    []
                                ),
                                [BinaryOp('<',Id('a'),Id('b'))]
                            ),
                            IntLiteral(0)
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))
    
    def test_complex_assignment_statement_5(self):
        input = \
r"""
Function: main
Body:
    a =foo(a[1+2][a*func()])[a < b];
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            ArrayCell(
                                CallExpr(
                                    Id('foo'),
                                    [
                                        ArrayCell(
                                            Id('a'),
                                            [
                                                BinaryOp(
                                                    '+',
                                                    IntLiteral(1),
                                                    IntLiteral(2)
                                                ),
                                                BinaryOp(
                                                    '*',
                                                    Id('a'),
                                                    CallExpr(
                                                        Id('func'),
                                                        []
                                                    )
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                [
                                    BinaryOp(
                                        '<',
                                        Id('a'),
                                        Id('b')
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    ################################ Test Mix ####################################
    def test_complex_function_1(self):
        input = \
r"""
Function: addsub 
Body: 
    s = a - b && c; 
    b[u] = u; 
    a = k + u[j]; 
    EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('addsub'),[],
                (
                    [],
                    [
                        Assign(
                            Id('s'),
                            BinaryOp(
                                '&&',
                                BinaryOp(
                                    '-',
                                    Id('a'),
                                    Id('b')
                                ),
                                Id('c')
                            )
                        ),
                        Assign(
                            ArrayCell(
                                Id('b'),
                                [Id('u')]
                            ),
                            Id('u')
                        ),
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '+',
                                Id('k'),
                                ArrayCell(
                                    Id('u'),
                                    [Id('j')]
                                )
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_relational_operator_less(self):
        input = \
r"""
Function: less 
Body: 
    a = (a <= b) <. c;
    a = (a < b) <=. c; 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('less'),[],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '<.',
                                BinaryOp(
                                    '<=',
                                    Id('a'),
                                    Id('b')
                                ),
                                Id('c')
                            )
                        ),
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '<=.',
                                BinaryOp(
                                    '<',
                                    Id('a'),
                                    Id('b')
                                ),
                                Id('c')
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_relational_operator_greater(self):
        input = \
r"""
Function: greater
Body: 
    Var: a;
    a = (a >= b) >. c; 
    a = (a > b) >=. c;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('greater'),[],
                (
                    [VarDecl(Id('a'),[],None)],
                    [
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '>.',
                                BinaryOp(
                                    '>=',
                                    Id('a'),
                                    Id('b')
                                ),
                                Id('c')
                            )
                        ),
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '>=.',
                                BinaryOp(
                                    '>',
                                    Id('a'),
                                    Id('b')
                                ),
                                Id('c')
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))
    
    def test_relational_operator_equal(self):
        input = \
r"""
Function: equal 
Body:
    a = (a == b) == b + c; 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('equal'),[],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '==',
                                BinaryOp(
                                    '==',
                                    Id('a'),
                                    Id('b')
                                ),
                                BinaryOp(
                                    '+',
                                    Id('b'),
                                    Id('c')
                                )
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_logical_operator_or(self):
        input = \
r"""
Function: or 
Body: 
    a = a || b || b;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('or'),[],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '||',
                                BinaryOp(
                                    '||',
                                    Id('a'),
                                    Id('b')
                                ),
                                Id('b')
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_logical_operator_and(self):
        input = \
r"""
Function: and 
Body: 
    a = a && b && b; 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('and'),[],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '&&',
                                BinaryOp(
                                    '&&',
                                    Id('a'),
                                    Id('b')
                                ),
                                Id('b')
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))


    def test_unary_operator(self):
        input = \
r"""
Function: unary
Body: 
    a = !b; b = -c; 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('unary'),[],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            UnaryOp(
                                '!',
                                Id('b')
                            )
                        ),
                        Assign(
                            Id('b'),
                            UnaryOp(
                                '-',
                                Id('c')
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))
    
    def test_mix_operators(self):
        input = \
r"""
Function: mix 
Body: 
    a = (a * b \ c % d  + f - h > b || c && m) == (v || a != a);
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('mix'),[],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '==',
                                BinaryOp(
                                    '>',
                                    BinaryOp(
                                        '-',
                                        BinaryOp(
                                            '+',
                                            BinaryOp(
                                                '%',
                                                BinaryOp(
                                                    '\\',
                                                    BinaryOp(
                                                        '*',
                                                        Id('a'),
                                                        Id('b')
                                                    ),
                                                    Id('c')
                                                ),
                                                Id('d')
                                            ),
                                            Id('f')
                                        ),
                                        Id('h')
                                    ),
                                    BinaryOp(
                                        '&&',
                                        BinaryOp(
                                            '||',
                                            Id('b'),
                                            Id('c')
                                        ),
                                        Id('m')
                                    )
                                ),
                                BinaryOp(
                                    '!=',
                                    BinaryOp(
                                        '||',
                                        Id('v'),
                                        Id('a')
                                    ),
                                    Id('a')
                                )
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_mix_statements_1(self):
        input = \
r"""
Function: stmtmix 
Body: 
    Break; 
    Continue; 
    For(i = 1, i < 3, 1) Do
        Var: v;
        v = v + 1; 
    EndFor. 
    Return 1; 

    Do
        Var: x = {5, {1}};
        x = x*x; 
    While (True) 
    EndDo. 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('stmtmix'),[],
                (
                    [],
                    [
                        Break(),
                        Continue(),
                        For(
                            Id('i'),
                            IntLiteral(1),
                            BinaryOp('<',Id('i'),IntLiteral(3)),
                            IntLiteral(1),
                            (
                                [VarDecl(Id('v'),[],None)],
                                [Assign(Id('v'),BinaryOp('+',Id('v'),IntLiteral(1)))]
                            )
                        ),
                        Return(IntLiteral(1)),
                        Dowhile(
                            (
                                [
                                    VarDecl(
                                        Id('x'),
                                        [],
                                        ArrayLiteral([
                                            IntLiteral(5),
                                            ArrayLiteral([
                                                IntLiteral(1)
                                            ])
                                        ])
                                    )
                                ],
                                [
                                    Assign(
                                        Id('x'),
                                        BinaryOp('*',Id('x'),Id('x'))
                                    )
                                ]
                            ),
                            BooleanLiteral(True)
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_mix_statements_2(self):
        input = \
r"""
Function: stmtmix 
Body: 
    While (False) Do 
        Return "abc"; 
    EndWhile. 
    foo(); 
    print(n); 
    If (foo()) Then Break; 
    EndIf. 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('stmtmix'),[],
                (
                    [],
                    [
                        While(
                            BooleanLiteral(False),
                            (
                                [],
                                [Return(StringLiteral("abc"))]
                            )
                        ),
                        CallStmt(
                            Id('foo'),
                            []
                        ),
                        CallStmt(
                            Id('print'),
                            [Id('n')]
                        ),
                        If(
                            [
                                (
                                    CallExpr(Id('foo'),[]),
                                    [],
                                    [Break()]
                                )
                            ],
                            ([],[])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))
    
    def test_mix_operations_1(self):
        input = \
r"""
Function: main
Body:
    Return 5 * a > b + 5 * 0 && 67;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Return(
                            BinaryOp(
                                '>',
                                BinaryOp(
                                    '*',
                                    IntLiteral(5),
                                    Id('a')
                                ),
                                BinaryOp(
                                    '&&',
                                    BinaryOp(
                                        '+',
                                        Id('b'),
                                        BinaryOp(
                                            '*',
                                            IntLiteral(5),
                                            IntLiteral(0)
                                        )
                                    ),
                                    IntLiteral(67)
                                )
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))
    
    def test_mix_operations_2(self):
        input = \
r"""
Function: main
Body:
    Return !a + t % e;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Return(
                            BinaryOp(
                                '+',
                                UnaryOp(
                                    '!',
                                    Id('a')
                                ),
                                BinaryOp(
                                    '%',
                                    Id('t'),
                                    Id('e')
                                )
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_many_minus_operation(self):
        input = \
r"""
Function: main
Body:
    Return -----a;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Return(
                            UnaryOp(
                                '-',
                                UnaryOp(
                                    '-',
                                    UnaryOp(
                                        '-',
                                        UnaryOp(
                                            '-',
                                            UnaryOp(
                                                '-',
                                                Id('a')
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))
    
    def test_index_operator_with_call_expression(self):
        input = \
r"""
Function: main
Body:
    Return foo()[1][3];
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Return(
                            ArrayCell(
                                CallExpr(Id('foo'),[]),
                                [
                                    IntLiteral(1),
                                    IntLiteral(3)
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))
    
    def test_index_operator_with_string_literal(self):
        input = \
r"""
Function: main
Body:
    Return "True"[1 == 4][3];
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Return(
                            ArrayCell(
                                StringLiteral("True"),
                                [
                                    BinaryOp('==',IntLiteral(1),IntLiteral(4)),
                                    IntLiteral(3)
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))
    
    def test_very_complex_operations(self):
        input = \
r"""
Function: main
Body:
    Return 6 + !a[foo()][-a && 6];
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        Return(
                            BinaryOp(
                                '+',
                                IntLiteral(6),
                                UnaryOp(
                                    '!',
                                    ArrayCell(
                                        Id('a'),
                                        [
                                            CallExpr(Id('foo'),[]),
                                            BinaryOp('&&',UnaryOp('-',Id('a')),
                                            IntLiteral(6))
                                        ]
                                    )
                                )
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    ################################## Test complete program #########################

    def test_valid_complete_program_1(self):
        input = \
r"""
Var: a, b = 100;
Var: c = True;
Function: test 
    Parameter: x,y=1,z[5]
    Body: 
        t = factor(x, y, z);
        Return t; 
    EndBody.
"""
        expect = Program([
            VarDecl(Id('a'),[],None),
            VarDecl(Id('b'),[],IntLiteral(100)),
            VarDecl(Id('c'),[],BooleanLiteral(True)),
            FuncDecl(
                Id('test'),
                [
                    VarDecl(Id('x'),[],None),
                    VarDecl(Id('y'),[],IntLiteral(1)),
                    VarDecl(Id('z'),[5],None),
                ],
                (
                    [],
                    [
                        Assign(
                            Id('t'),
                            CallExpr(
                                Id('factor'),
                                [
                                    Id('x'),
                                    Id('y'),
                                    Id('z')
                                ]
                            )
                        ),
                        Return(
                            Id('t')
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_valid_complete_program_2(self):
        input = \
r"""
Var: a, b, c; 
Function: f 
Body: 
    Return random(); 
EndBody. 

Function: main 
Body: 
    print(f());
EndBody.
"""
        expect = Program([
            VarDecl(Id('a'),[],None),
            VarDecl(Id('b'),[],None),
            VarDecl(Id('c'),[],None),
            FuncDecl(
                Id('f'),[],
                (
                    [],
                    [
                        Return(
                            CallExpr(
                                Id('random'),
                                []
                            )
                        )
                    ]
                )
            ),
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        CallStmt(
                            Id('print'),
                            [
                                CallExpr(
                                    Id('f'),
                                    []
                                )
                            ]
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_valid_complete_program_3(self):
        input = \
r"""
Var: a, b; 
Function: test 
Parameter: x, y 
Body: 
    a = "Hi"; 
EndBody. 

Function: foo 
Parameter: a, c 
Body: 
    For (i = 1, i <= 4, 1) Do 
        print(i); 
    EndFor. 
    x = x % y;
    y = y * z; 
    z = z && x; 
    Return a + c; 
EndBody.
"""
        expect = Program([
            VarDecl(Id('a'),[],None),
            VarDecl(Id('b'),[],None),
            FuncDecl(
                Id('test'),
                [
                    VarDecl(Id('x'),[],None),
                    VarDecl(Id('y'),[],None)
                ],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            StringLiteral("Hi")
                        )
                    ]
                )
            ),
            FuncDecl(
                Id('foo'),
                [
                    VarDecl(Id('a'),[],None),
                    VarDecl(Id('c'),[],None)
                ],
                (
                    [],
                    [
                        For(
                            Id('i'),
                            IntLiteral(1),
                            BinaryOp('<=',Id('i'),IntLiteral(4)),
                            IntLiteral(1),
                            (
                                [],
                                [CallStmt(Id('print'),[Id('i')])]
                            )
                        ),
                        Assign(
                            Id('x'),
                            BinaryOp(
                                '%',
                                Id('x'),
                                Id('y')
                            )
                        ),
                        Assign(
                            Id('y'),
                            BinaryOp(
                                '*',
                                Id('y'),
                                Id('z')
                            )
                        ),
                        Assign(
                            Id('z'),
                            BinaryOp(
                                '&&',
                                Id('z'),
                                Id('x')
                            )
                        ),
                        Return(BinaryOp('+',Id('a'),Id('c')))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_valid_complete_program_4(self):
        input = \
r"""
Function: test 
Parameter: suite 
Body: 
    import(pprint); 
    import(stringIO); 
    stream = stringIO(); 
    runner = unittest(textTestRunner(stream==stream));
    result = runner(run(suite));
    print("Tests run", result(testsRun)); 
    print("Errors ", result(errors));
EndBody. 
"""
        expect = Program([
            FuncDecl(
                Id('test'),
                [
                    VarDecl(Id('suite'),[],None)
                ],
                (
                    [],
                    [
                        CallStmt(
                            Id('import'),
                            [Id('pprint')]
                        ),
                        CallStmt(
                            Id('import'),
                            [Id('stringIO')]
                        ),
                        Assign(
                            Id('stream'),
                            CallExpr(
                                Id('stringIO'),
                                []
                            )
                        ),
                        Assign(
                            Id('runner'),
                            CallExpr(
                                Id('unittest'),
                                [
                                    CallExpr(
                                        Id('textTestRunner'),
                                        [BinaryOp('==',Id('stream'),Id('stream'))]
                                    )
                                ]
                            )
                        ),
                        Assign(
                            Id('result'),
                            CallExpr(
                                Id('runner'),
                                [
                                    CallExpr(
                                        Id('run'),
                                        [Id('suite')]
                                    )
                                ]
                            )
                        ),
                        CallStmt(
                            Id('print'),
                            [
                                StringLiteral("Tests run"),
                                CallExpr(
                                    Id('result'),
                                    [Id('testsRun')]
                                )
                            ]
                        ),
                        CallStmt(
                            Id('print'),
                            [
                                StringLiteral("Errors "),
                                CallExpr(
                                    Id('result'),
                                    [Id('errors')]
                                )
                            ]
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))
    
    def test_valid_complete_program_5(self):
        input = \
r"""
Function: fibo
Parameter: x
Body:
    If (x == 1) || (x == 0) Then 
        Return 1;
    Else
        Return fibo(x-1) + fibo(x-2);
    EndIf.
EndBody.

Function: main
Body:
    fibo(3);
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('fibo'),
                [
                    VarDecl(Id('x'),[],None)
                ],
                (
                    [],
                    [
                        If(
                            [
                                (
                                    BinaryOp(
                                        '||',
                                        BinaryOp(
                                            '==',
                                            Id('x'),
                                            IntLiteral(1)
                                        ),
                                        BinaryOp(
                                            '==',
                                            Id('x'),
                                            IntLiteral(0)
                                        )
                                    ),
                                    [],
                                    [
                                        Return(
                                            IntLiteral(1)
                                        )
                                    ]
                                )
                            ],
                            (
                                [],
                                [
                                    Return(
                                        BinaryOp(
                                            '+',
                                            CallExpr(
                                                Id('fibo'),
                                                [
                                                    BinaryOp(
                                                        '-',
                                                        Id('x'),
                                                        IntLiteral(1)
                                                    )
                                                ]
                                            ),
                                            CallExpr(
                                                Id('fibo'),
                                                [
                                                    BinaryOp(
                                                        '-',
                                                        Id('x'),
                                                        IntLiteral(2)
                                                    )
                                                ]
                                            )
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            ),
            FuncDecl(
                Id('main'),[],
                (
                    [],
                    [
                        CallStmt(
                            Id('fibo'),
                            [IntLiteral(3)]
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_valid_while_statement_with_empty_body(self):
        input = \
r"""
Function: foo 
Body: 
    While (True) Do 
    EndWhile. 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('foo'),[],
                (
                    [],
                    [
                        While(
                            BooleanLiteral(True),
                            ([],[])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_valid_for_statement_with_empty_body(self):
        input = \
r"""
Function: foo 
Body: 
    For(i=1, i<2, 1) Do 
    EndFor. 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('foo'),[],
                (
                    [],
                    [
                        For(
                            Id('i'),
                            IntLiteral(1),
                            BinaryOp('<',Id('i'),IntLiteral(2)),
                            IntLiteral(1),
                            ([],[])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_valid_do_while_statement_with_empty_body(self):
        input = \
r"""
Function: foo 
Body: 
    Do  
    While (True) 
    EndDo. 
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('foo'),[],
                (
                    [],
                    [
                        Dowhile(
                            ([],[]),
                            BooleanLiteral(True)
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))
    
    ################################# Test useful program ###############################

    def test_palindrome_string(self):
        input = \
r"""
Function: isPalindrome
Parameter: str
Body:
    Var: len, i;
    len = length(str);
    For(i = 0, i < length \ 2, 1) Do
        If str[i] =/= str[length - i - 1] Then
            Return False;
        EndIf.
    EndFor.
    Return True;
EndBody.

Function: length
Parameter: str
Body:
    Var: i = 0;
    While str[i] == null Do
        i = i + 1;
    EndWhile.
    Return i;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('isPalindrome'),
                [
                    VarDecl(Id('str'),[],None)
                ],
                (
                    [
                        VarDecl(Id('len'),[],None),
                        VarDecl(Id('i'),[],None)
                    ],
                    [
                        Assign(
                            Id('len'),
                            CallExpr(
                                Id('length'),
                                [Id('str')]
                            )
                        ),
                        For(
                            Id('i'),
                            IntLiteral(0),
                            BinaryOp('<',Id('i'),BinaryOp('\\',Id('length'),IntLiteral(2))),
                            IntLiteral(1),
                            (
                                [],
                                [
                                    If(
                                        [
                                            (
                                                BinaryOp(
                                                    '=/=',
                                                    ArrayCell(Id('str'),[Id('i')]),
                                                    ArrayCell(
                                                        Id('str'),
                                                        [
                                                            BinaryOp(
                                                                '-',
                                                                BinaryOp(
                                                                    '-',
                                                                    Id('length'),
                                                                    Id('i')
                                                                ),
                                                                IntLiteral(1)
                                                            )
                                                        ]
                                                    )
                                                ),
                                                [],
                                                [Return(BooleanLiteral(False))]
                                            )
                                        ],
                                        ([],[])
                                    )
                                ]
                            )
                        ),
                        Return(BooleanLiteral(True))
                    ]
                )
            ),
            FuncDecl(
                Id('length'),
                [
                    VarDecl(Id('str'),[],None)
                ],
                (
                    [
                        VarDecl(Id('i'),[],IntLiteral(0))
                    ],
                    [
                        While(
                            BinaryOp(
                                '==',
                                ArrayCell(Id('str'),[Id('i')]),
                                Id('null')
                            ),
                            (
                                [],
                                [
                                    Assign(
                                        Id('i'),
                                        BinaryOp(
                                            '+',
                                            Id('i'),
                                            IntLiteral(1)
                                        )
                                    )
                                ]
                            )
                        ),
                        Return(Id('i'))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))
    
    def test_prime_number_program_iteration(self):
        input = \
r"""
Function: isPrime
Parameter: n
Body:
    Var: i;
    If n <= 1 Then Return False; EndIf.

    For(i = 2, i <= n \ 2, 1) Do
        If n % i == 0 Then
            Return False;
        EndIf.
    EndFor.
    Return True;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('isPrime'),
                [
                    VarDecl(Id('n'),[],None)
                ],
                (
                    [
                        VarDecl(Id('i'),[],None)
                    ],
                    [
                        If(
                            [
                                (
                                    BinaryOp('<=',Id('n'),IntLiteral(1)),
                                    [],
                                    [Return(BooleanLiteral(False))]
                                )
                            ],
                            ([],[])
                        ),
                        For(
                            Id('i'),
                            IntLiteral(2),
                            BinaryOp('<=',Id('i'),BinaryOp('\\',Id('n'),IntLiteral(2))),
                            IntLiteral(1),
                            (
                                [],
                                [
                                    If(
                                        [(
                                            BinaryOp('==',BinaryOp('%',Id('n'),Id('i')),IntLiteral(0)),
                                            [],
                                            [Return(BooleanLiteral(False))]
                                        )],
                                        ([],[])
                                    )
                                ]
                            )
                        ),
                        Return(BooleanLiteral(True))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_prime_number_program_recursion(self):
        input = \
r"""
Function: isPrime
Parameter: n, i=2         ** Default: i = 2 **
Body:
    If n == 2 Then
        Return True;
    ElseIf n < 2 Then
        Return False;
    EndIf.
    
    If n % i == 0 Then
        Return False;
    EndIf.
    
    If i * i > n Then
        Return True;
    EndIf.

    Return isPrime(n, i + 1);
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('isPrime'),
                [
                    VarDecl(Id('n'),[],None),
                    VarDecl(Id('i'),[],IntLiteral(2))
                ],
                (
                    [],
                    [
                        If(
                            [
                                (
                                    BinaryOp('==',Id('n'),IntLiteral(2)),
                                    [],
                                    [Return(BooleanLiteral(True))]
                                ),
                                (
                                    BinaryOp('<',Id('n'),IntLiteral(2)),
                                    [],
                                    [Return(BooleanLiteral(False))]
                                )
                            ],
                            ([],[])
                        ),
                        If(
                            [
                                (
                                    BinaryOp('==',BinaryOp('%',Id('n'),Id('i')),IntLiteral(0)),
                                    [],
                                    [Return(BooleanLiteral(False))]
                                )
                            ],
                            ([],[])
                        ),
                        If(
                            [
                                (
                                    BinaryOp('>',BinaryOp('*',Id('i'),Id('i')),Id('n')),
                                    [],
                                    [Return(BooleanLiteral(True))]
                                )
                            ],
                            ([],[])
                        ),
                        Return(
                            CallExpr(
                                Id('isPrime'),
                                [
                                    Id('n'),
                                    BinaryOp(
                                        '+',
                                        Id('i'),
                                        IntLiteral(1)
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))
    
    def test_factorial_recursion(self):
        input = \
r"""
Function: factorial
Parameter: n
Body:
    If n <= 1 Then
        Return 1;
    Else
        Return n * factorial(n - 1);
    EndIf.
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('factorial'),
                [
                    VarDecl(Id('n'),[],None)
                ],
                (
                    [],
                    [
                        If(
                            [(
                                BinaryOp('<=',Id('n'),IntLiteral(1)),
                                [],
                                [Return(IntLiteral(1))]
                            )],
                            (
                                [],
                                [Return(
                                    BinaryOp(
                                        '*',
                                        Id('n'),
                                        CallExpr(
                                            Id('factorial'),
                                            [BinaryOp('-',Id('n'),IntLiteral(1))]
                                        )
                                    )
                                )]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_factorial_iteration(self):
        input = \
r"""
Function: factorial
Parameter: n
Body:
    Var: i;
    Var: fact = 1;

    If n <= 1 Then
        Return 1;
    EndIf.
    
    For (i = 1, i <= n, 1) Do
        fact = fact * i;
    EndFor.
    Return fact;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('factorial'),
                [
                    VarDecl(Id('n'),[],None)
                ],
                (
                    [
                        VarDecl(Id('i'),[],None),
                        VarDecl(Id('fact'),[],IntLiteral(1))
                    ],
                    [
                        If(
                            [(
                                BinaryOp('<=',Id('n'),IntLiteral(1)),
                                [],
                                [Return(IntLiteral(1))]
                            )],
                            ([],[])
                        ),
                        For(
                            Id('i'),
                            IntLiteral(1),
                            BinaryOp('<=',Id('i'),Id('n')),
                            IntLiteral(1),
                            (
                                [],
                                [Assign(Id('fact'),BinaryOp('*',Id('fact'),Id('i')))]
                            )
                        ),
                        Return(Id('fact'))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))
    
    def test_fizzbuzz_program(self):
        input = \
r"""
Function: fizz_buzz
Body:
    Var: i;
    For (i = 1, i <= 100, 1) Do
        If i % 15 == 0 Then
            printLn("FizzBuzz\t");
        ElseIf i % 3 == 0 Then
            printLn("Fizz\t");
        ElseIf i % 5 == 0 Then
            printLn("Buzz\t");
        Else
            printLn(string_of_int(i) + "\t");
        EndIf.
    EndFor.
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('fizz_buzz'),[],
                (
                    [
                        VarDecl(Id('i'),[],None)
                    ],
                    [
                        For(
                            Id('i'),
                            IntLiteral(1),
                            BinaryOp('<=',Id('i'),IntLiteral(100)),
                            IntLiteral(1),
                            (
                                [],
                                [
                                    If(
                                        [
                                            (
                                                BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(15)),IntLiteral(0)),
                                                [],
                                                [
                                                    CallStmt(
                                                        Id('printLn'),
                                                        [StringLiteral("FizzBuzz\\t")]
                                                    )
                                                ]
                                            ),
                                            (
                                                BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(3)),IntLiteral(0)),
                                                [],
                                                [
                                                    CallStmt(
                                                        Id('printLn'),
                                                        [StringLiteral("Fizz\\t")]
                                                    )
                                                ]
                                            ),
                                            (
                                                BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(5)),IntLiteral(0)),
                                                [],
                                                [
                                                    CallStmt(
                                                        Id('printLn'),
                                                        [StringLiteral("Buzz\\t")]
                                                    )
                                                ]
                                            )
                                        ],
                                        (
                                            [],
                                            [CallStmt(
                                                Id('printLn'),
                                                [
                                                    BinaryOp(
                                                        '+',
                                                        CallExpr(
                                                            Id('string_of_int'),
                                                            [Id('i')]
                                                        ),
                                                        StringLiteral("\\t")
                                                    )
                                                ]
                                            )]
                                        )
                                    )
                                ]
                            )
                        ),
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_blackjack_program(self):
        input = \
r"""
Function: blackjack
Parameter: a, b
Body:
    Var: sum;
    sum = a + b;
    If sum > 21 Then
        If a == 11 Then
            sum = 1 + b;
        ElseIf b == 11 Then
            sum = 1 + a;
        Else
            sum = 0;
        EndIf.
    EndIf.
    Return sum;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('blackjack'),
                [
                    VarDecl(Id('a'),[],None),
                    VarDecl(Id('b'),[],None)
                ],
                (
                    [
                        VarDecl(Id('sum'),[],None)
                    ],
                    [
                        Assign(
                            Id('sum'),
                            BinaryOp('+',Id('a'),Id('b'))
                        ),
                        If(
                            [(
                                BinaryOp('>',Id('sum'),IntLiteral(21)),
                                [],
                                [
                                    If(
                                        [
                                            (
                                                BinaryOp('==',Id('a'),IntLiteral(11)),
                                                [],
                                                [Assign(Id('sum'),BinaryOp('+',IntLiteral(1),Id('b')))]
                                            ),
                                            (
                                                BinaryOp('==',Id('b'),IntLiteral(11)),
                                                [],
                                                [Assign(Id('sum'),BinaryOp('+',IntLiteral(1),Id('a')))]
                                            )
                                        ],
                                        (
                                            [],
                                            [Assign(Id('sum'),IntLiteral(0))]
                                        )
                                    )
                                ]
                            )],
                            ([],[])
                        ),
                        Return(Id('sum'))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))
    
    def test_search_array(self):
        input = \
r"""
Function: search
Parameter: target, arr, size
Body:
    Var: idx;
    For (idx = 0, idx < size, 1) Do
        If arr[idx] == target Then
            Return idx;
        EndIf.
    EndFor.
    Return -1;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('search'),
                [
                    VarDecl(Id('target'),[],None),
                    VarDecl(Id('arr'),[],None),
                    VarDecl(Id('size'),[],None)
                ],
                (
                    [
                        VarDecl(Id('idx'),[],None)
                    ],
                    [
                        For(
                            Id('idx'),
                            IntLiteral(0),
                            BinaryOp('<',Id('idx'),Id('size')),
                            IntLiteral(1),
                            (
                                [],
                                [
                                    If(
                                        [(
                                            BinaryOp(
                                                '==',
                                                ArrayCell(Id('arr'),[Id('idx')]),
                                                Id('target')
                                            ),
                                            [],
                                            [Return(Id('idx'))]
                                        )],
                                        ([],[])
                                    )
                                ]
                            )
                        ),
                        Return(UnaryOp('-',IntLiteral(1)))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))
    
    def test_gcd_program(self):
        input = \
r"""
Function: gcd
Parameter: a, b
Body:
    While a =/= b Do
        If a > b Then
            a = a - b;
        Else
            b = b - a;
        EndIf.
    EndWhile.
    Return a;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('gcd'),
                [
                    VarDecl(Id('a'),[],None),
                    VarDecl(Id('b'),[],None)
                ],
                (
                    [],
                    [
                        While(
                            BinaryOp('=/=',Id('a'),Id('b')),
                            (
                                [],
                                [
                                    If(
                                        [(
                                            BinaryOp('>',Id('a'),Id('b')),
                                            [],
                                            [Assign(Id('a'),BinaryOp('-',Id('a'),Id('b')))]
                                        )],
                                        (
                                            [],
                                            [Assign(Id('b'),BinaryOp('-',Id('b'),Id('a')))]
                                        )
                                    )
                                ]
                            )
                        ),
                        Return(Id('a'))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))
    
    def test_binary_search_program(self):
        input = \
r"""
Function: binarySearch
Parameter: arr, leftIdx, rightIdx, target
Body:
    ** Assume array is sorted **
    Var: mid;
    If rightIdx >= leftIdx Then
        mid = leftIdx + (rightIdx - leftIdx) \ 2;

        ** If found target **
        If arr[mid] == target Then
            Return mid;
        EndIf.

        ** Target is at left branch **
        If arr[mid] > target Then
            Return binarySearch(arr, 1, mid - 1, target);
        EndIf.

         ** Target is at right branch **
        Return binarySearch(arr, mid + 1, rightIdx, target);
    EndIf.
    Return -1;
EndBody.
"""
        expect = Program([
            FuncDecl(
                Id('binarySearch'),
                [
                    VarDecl(Id('arr'),[],None),
                    VarDecl(Id('leftIdx'),[],None),
                    VarDecl(Id('rightIdx'),[],None),
                    VarDecl(Id('target'),[],None)
                ],
                (
                    [
                        VarDecl(Id('mid'),[],None)
                    ],
                    [
                        If(
                            [(
                                BinaryOp('>=',Id('rightIdx'),Id('leftIdx')),
                                [],
                                [
                                    Assign(
                                        Id('mid'),
                                        BinaryOp(
                                            '+',
                                            Id('leftIdx'),
                                            BinaryOp(
                                                '\\',
                                                BinaryOp('-',Id('rightIdx'),Id('leftIdx')),
                                                IntLiteral(2)
                                            )
                                        )
                                    ),
                                    If(
                                        [(
                                            BinaryOp('==',ArrayCell(Id('arr'),[Id('mid')]),Id('target')),
                                            [],
                                            [Return(Id('mid'))]
                                        )],
                                        ([],[])
                                    ),
                                    If(
                                        [(
                                            BinaryOp('>',ArrayCell(Id('arr'),[Id('mid')]),Id('target')),
                                            [],
                                            [Return(
                                                CallExpr(
                                                    Id('binarySearch'),
                                                    [
                                                        Id('arr'),
                                                        IntLiteral(1),
                                                        BinaryOp('-',Id('mid'),IntLiteral(1)),
                                                        Id('target')
                                                    ]
                                                )
                                            )]
                                        )],
                                        ([],[])
                                    ),
                                    Return(
                                        CallExpr(
                                            Id('binarySearch'),
                                            [
                                                Id('arr'),
                                                BinaryOp('+',Id('mid'),IntLiteral(1)),
                                                Id('rightIdx'),
                                                Id('target')
                                            ]
                                        )
                                    )
                                ]
                            )],
                            ([],[])
                        ),
                        Return(UnaryOp('-',IntLiteral(1)))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_something(self):
        input = \
r"""
Function: main
Body:
    Function: g
    Body:
    EndBody.

    Function: f
    Body:
    EndBody.
EndBody.
"""
        expect = Program(
            [
                FuncDecl(
                    Id('main'),
                    [],
                    (
                        [
                            FuncDecl(Id('g'),[],([],[])),
                            FuncDecl(Id('f'),[],([],[]))
                        ],
                        []
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))

 
   