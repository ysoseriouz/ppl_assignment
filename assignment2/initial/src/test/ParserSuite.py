import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    ############################ Test global declaration part #############################
    def test_valid_global_declaration_with_initialization(self):
        input = \
r"""
Var: x = 1;
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,200))
    
    def test_full_valid_program_inline(self):
        input = \
r"""
Var: m, n[10]; Function: fact Parameter: n Body: If n == 0 Then Return 1; Else Return n * fact (n-1); EndIf. EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_valid_global_declaration_with_array_initialization(self):
        input = \
r"""
Var: a[2][2] = {{1, 2}, {3, 4}};
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_valid_global_declaration_with_different_literal_types_in_array(self):
        input = \
r"""
Var: b[2][2] = {{True, 2}, {2.8, 4}};
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_invalid_multi_declaration(self):
        input = \
r"""
Var: a, b[1], c = 2, 1;
"""
        expect = "Error on line 2 col 21: 1"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_valid_normal_global_declaration(self):
        input = \
r"""
Var: x, y, z[2][4];
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_valid_global_declaration_with_function_call_initialization(self):
        input = \
r"""
Function: main
Body:
    Var: a;
    a = id();
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))
    
    def test_invalid_global_declaration_without_semicolon(self):
        input = \
r"""
Var: a, b[1], c = 2,1
"""
        expect = "Error on line 2 col 20: 1"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_invalid_global_declaration_with_two_semicolons(self):
        input = \
r"""
Var: a[2][3] = {{1,2,3,4}, {1,2,3,4}};;
"""
        expect = "Error on line 2 col 38: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_invalid_global_declaration_without_colon(self):
        input = \
r"""
Var a, b, c = True, True, 1;
"""
        expect = "Error on line 2 col 4: a"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_invalid_global_declaration_with_lowercase_var_keyword(self):
        """Global declaration"""
        input = \
r"""
var: a, b[1][2] = {1, 2, 3}, True;
"""
        expect = "Error on line 2 col 0: var"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_invalid_global_declaration(self):
        input = \
r"""
Var: a 1;
"""
        expect = "Error on line 2 col 7: 1"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_invalid_global_declaration_without_var_keyword(self):
        input = \
r"""
int a = 1;
"""
        expect = "Error on line 2 col 0: int"
        self.assertTrue(TestParser.checkParser(input, expect, 212))
    
    def test_multiple_variable_declarations(self):
        input = r"""Var: x; Var: y; Var: z;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_invalid_dimension_in_composite_variable(self):
        input = r"""Var: x[True];"""
        expect = "Error on line 1 col 7: True"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_invalid_global_declaration_after_function_declaration(self):
        input = \
r"""
Function: main
Body:
    print("Hello World");
EndBody.
Var: a = 1;
"""
        expect = "Error on line 6 col 0: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    ############################ Test function declaration part ###########################
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_invalid_function_with_vardec_stmt_after_other_stmt(self):
        input = \
r"""
Function: test
Body: 
    If n > 10 Then 
        Return 5; 
    Else Return True; 
    Var: n; 
    EndIf. 
EndBody.
"""
        expect = "Error on line 7 col 4: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_invalid_function_without_ending_dot(self):
        input = \
r"""
Function: test 
Parameter: n 
Body: 
    If n > 10 Then
        Return 5; 
    Else Return True; 
    EndIf. 
EndBody
"""
        expect = "Error on line 10 col 0: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_invalid_function_without_endbody(self):
        input = \
r"""
Function: main 
Body: 
    n = n + 1;
"""
        expect = "Error on line 5 col 0: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_function_end_with_two_dots(self):
        input = r"""Function: foo Body: EndBody.."""
        expect = "Error on line 1 col 28: ."
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_not_allow_function_inside_function(self):
        input = \
r"""
Function: foo 
Body: 
    Function: test 
    Body: 
    EndBody. 
EndBody.
"""
        expect = "Error on line 4 col 4: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_valid_empty_program(self):
        input = \
r"""
** @Author: Nguyen Tien Thanh - 1852740 **
** This should be
 * an empty
 * program
**
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_invalid_function_without_body(self):
        input = \
r"""
Function: test
"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_valid_function_with_empty_body(self):
        input = \
r"""
Function: foo 
Body: 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))
    
    def test_valid_function_declaration_weird_inline(self):
        input = r"""Function: test Parameter: n Body: If n>10 Then Return 5; ElseReturnTrue;EndIf.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    ############################ Test expression #############################
    def test_variable_declaration(self):
        input = \
r"""
Function: test 
Body: 
    Var: x,y,z;
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_variable_declaration_with_array_initialization(self):
        input = \
r"""
Function: test 
Body: 
    Var: a = {1, 2}; 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_complicated_expression(self):
        input = \
r"""
Function: test
Body: 
    Var: a;
    a = a >= b || c +. d + -e;
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_invalid_variable_declaration(self):
        input = \
r"""
Function: test
Body: 
    Var: a;
    a = a || b = a*a || b*b - c;
EndBody.
"""
        expect = "Error on line 5 col 15: ="
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_invalid_operator(self):
        input = \
r"""
Function: test
Body: 
    Var: a;
    a = a * b * c %. d;
EndBody.
"""
        expect = "Error on line 5 col 19: ."
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_array_missing_closing_bracket(self):
        input = \
r"""
Function: test
Body: 
    Var: a;
    a = {{1, 2}, {3, 4};
EndBody.
"""
        expect = "Error on line 5 col 23: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 233))
    
    def test_a_weird_mix_expression(self):
        input = \
r"""
Function: test
Body: 
    Var: x;
    x = -{1, 2, 3};
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))
    
    def test_another_weird_mix_expression(self):
        input = \
r"""
Function: test
Body: 
    Var: x;
    x = -True;
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))
    
    def test_negative_arithmetic_expression(self):
        input = \
r"""
Function: test
Body: 
    Var: x;
    x = -12.6;
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_not_operator(self):
        input = \
r"""
Function: test
Body: 
    Var: x;
    x = !True;
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))
    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))
    
    def test_operation_with_array_literal(self):
        input = \
r"""
Function: main
Body:
    Var: a;
    a = {1, 2, 3} - {1, 2, 3};
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_operation_with_string_literal(self):
        input = \
r"""
Function: main
Body:
    Var: a;
    a = "Hello" \ "ello";
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_operation_with_two_different_literal_types_1(self):
        input = \
r"""
Function: main
Body:
    Var: a;
    a = 1 % True;
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_operation_with_two_different_literal_types_2(self):
        input = \
r"""
Function: main
Body:
    Var: a;
    a = a && "Hello world!";
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_index_operator(self):
        input = \
r"""
Function: main
Body:
    a[3 + foo(2)] = a[b[2][3]] - 4;
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))
    
    def test_logical_expression_inside_function(self):
        input = \
r"""
Function: test
Body: 
    n = a || b || c; 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))
    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))
    
    def test_for_loop_statement(self):
        input = \
r"""
Var: a, b; 
Function: test 
Body: 
    a = "Hi"; 
EndBody. 

Function: foo 
Parameter: a, c 
Body: 
    For (i = 1, i <= 4, 1) Do 
        print(i);
    EndFor. 
    Return a + c; 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_for_statement_with_invalid_iter_condition(self):
        input = \
r"""
Var: a, b;
Function: foo 
Body: 
    For (i = 1, i <= 4, i = i + 1) Do
        print(i); 
    EndFor. 
EndBody."""
        expect = "Error on line 5 col 26: ="
        self.assertTrue(TestParser.checkParser(input, expect, 251))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_nested_function_call(self):
        input = \
r"""
Function: fc 
Body: 
    foo(test(f(a, b, c))); 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    ################################ Test Mix ####################################
    def test_invalid_statement_as_parameter(self):
        input = \
r"""
Function: foo 
Parameter: a, Break 
Body: 
EndBody.
"""
        expect = "Error on line 3 col 14: Break"
        self.assertTrue(TestParser.checkParser(input, expect, 254))
    
    def test_invalid_function_parameter_assigned_expression(self):
        input = \
r"""
Function: foo 
Parameter: n = {a, b, c, 1}, d, a[5]
Body: 
EndBody.
"""
        expect = "Error on line 3 col 13: ="
        self.assertTrue(TestParser.checkParser(input, expect, 255))
    
    def test_invalid_function_call_as_parameter(self):
        input = \
r"""
Function: foo 
Parameter: a, f() 
Body: 
EndBody.
"""
        expect = "Error on line 3 col 15: ("
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_invalid_assignment_with_reserved_keyword_break(self):
        input = r"""Var: x = Break;"""
        expect = "Error on line 1 col 9: Break"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_invalid_assignment_with_reserved_keyword_return(self):
        input = r"""Var: x = Return;"""
        expect = "Error on line 1 col 9: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 258))
    
    def test_composite_declaration_with_invalid_function_call_as_dimension(self):
        input = r"""Var: x[f()][a()] = n;"""
        expect = "Error on line 1 col 7: f"
        self.assertTrue(TestParser.checkParser(input, expect, 259))
    
    def test_composite_declaration_with_invalid_string_as_dimension(self):
        input = r"""Var: x["abc"];"""
        expect = "Error on line 1 col 7: abc"
        self.assertTrue(TestParser.checkParser(input, expect, 260))
    
    def test_composite_declaration_with_invalid_dimension_in_general(self):
        """Test index of array"""
        input = """Var: x[a[1]];"""
        expect = "Error on line 1 col 7: a"
        self.assertTrue(TestParser.checkParser(input, expect, 261))
    
    def test_statement_outside_function(self):
        input = \
r"""
Var: a; 
Function: test 
Body: 
EndBody.
test();
"""
        expect = "Error on line 6 col 0: test"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_relational_operator_less(self):
        input = \
r"""
Function: less 
Body: 
    a = (a <= b) <. c;
    a = (a < b) <=. c; 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))
    
    def test_relational_operator_equal(self):
        input = \
r"""
Function: equal 
Body:
    a = (a == b) == b + c; 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_logical_operator_or(self):
        input = \
r"""
Function: or 
Body: 
    a = a || b || b;
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_logical_operator_and(self):
        input = \
r"""
Function: and 
Body: 
    a = a && b && b; 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_unary_operator(self):
        input = \
r"""
Function: unary
Body: 
    a = !b; b = -c; 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))
    
    def test_mix_operators(self):
        input = \
r"""
Function: mix 
Body: 
    a = (a * b \ c % d  + f - h > b || c && m) == (v || a != a);
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_expression_as_invalid_identifier(self):
        input = """Var: x == 1 =  n;"""
        expect = "Error on line 1 col 7: =="
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_mix_statements_1(self):
        input = \
r"""
Function: stmtmix 
Body: 
    Break; 
    Continue; 
    For(i = 1, i < 3, 1) Do 
        v = v + 1; 
    EndFor. 
    Return 1; 

    Do 
        x = x*x; 
    While (True) 
    EndDo. 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))
    
    ################################## Test complete program #########################

    def test_valid_complete_program_1(self):
        input = \
r"""
Var: a, b = 100;
Var: c = True;
Function: test 
    Parameter: x,y,z
    Body: 
        t = factor(x, y, z);
        Return t; 
    EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))
    
    ################################# Test error function again ############################

    def test_invalid_function_with_missing_parameter(self):
        input = \
r"""
Function: test 
Parameter: 
Body: 
    While(1) Do 
    EndWhile. 
EndBody.
"""
        expect = "Error on line 4 col 0: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_invalid_function_without_name(self):
        input = \
r"""
Function:
Body: 
EndBody.
"""
        expect = "Error on line 3 col 0: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_valid_while_statement_with_empty_body(self):
        input = \
r"""
Function: foo 
Body: 
    While (True) Do 
    EndWhile. 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_valid_for_statement_with_empty_body(self):
        input = \
r"""
Function: foo 
Body: 
    For(i=1, i<2, 1) Do 
    EndFor. 
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))
    
    def test_syntax_error_function_keyword(self):
        input = \
r"""
function: foo 
Body: 
    printLn("Hello);
EndBody.
"""
        expect = "Error on line 2 col 0: function"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_syntax_error_endbody_keyword(self):
        input = \
r"""
Function: foo 
Body:
    Var: x = 8;
endbody.
"""
        expect = "Error on line 5 col 7: ."
        self.assertTrue(TestParser.checkParser(input, expect, 284))
    
    def test_body_missing_function_header(self):
        input = \
r"""
Body:
    Var: a;
    a[3 + foo(2)] = a[b[2][3] + 4;
endbody.
"""
        expect = "Error on line 2 col 0: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 285))
    
    def test_syntax_error_index_operator(self):
        input = \
r"""
Function: foo 
Body:
    Var: a;
    a[3 + foo(2)] = a[b[2][3] + 4;
EndBody.
"""
        expect = "Error on line 5 col 21: ["
        self.assertTrue(TestParser.checkParser(input, expect, 286))
    
    def test_syntax_error_function_call(self):
        input = \
r"""
Function: foo 
Body:
    main;
EndBody.
"""
        expect = "Error on line 4 col 8: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 287))
    
    def test_invalid_ambiguous_nested_if_statement(self):
        input = \
r"""
Function: foo 
Body:
    Var: i = 0, j = 0;
    If i == 1 Then
        If j =/= 0 Then
            Return True;
        Else
            print("Hello");
    EndIf.
EndBody.
"""
        expect = "Error on line 11 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_for_loop_without_initExpr_condition(self):
        input = \
r"""
Function: foo 
Body:
    Var: i = 0;
    For(i, i < 20, 2) Do
        writeLn(i);
    EndFor.
EndBody.
"""
        expect = "Error on line 5 col 9: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 289))
    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))
    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_prime_number_program_recursion(self):
        input = \
r"""
Function: isPrime
Parameter: n, i         ** Default: i = 2 **
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))
    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))
    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))
    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))
    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))
    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))
