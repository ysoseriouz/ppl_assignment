import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    ############################### Test empty program ################################
    def test_empty_program(self):
        input = r""" "" """
        expect = """,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 101))

    def test_only_whitespace_program(self):
        input = r""" " " """
        expect = """ ,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 102))

    def test_empty_program_with_newline(self):
        input = "   \n    \n"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 103))

    def test_empty_program_with_tab(self):
        input = "\t\t\t\t\t\t   \t\t\t"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 104))

    def test_skip_space_and_only_extract_defined_tokens(self):
        input = "Var: \n x;"
        expect = "Var,:,x,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 105))

    ############################### Test string ################################
    def test_string_with_formfeed(self):
        input = """ "\f" """
        expect = """\f,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 106))

    def test_string_with_backspace(self):
        input = """ "\b" """
        expect = """\b,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 107))

    def test_unclosed_string(self):
        input = """ "\n" """
        expect = """Unclosed String: \n"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 108))

    def test_unclosed_string_1(self):
        input = """ "\n\t\\\b\r\f" """
        expect = """Unclosed String: \n"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 109))

    def test_legal_string(self):
        input = """ "00" """
        expect = """00,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 110))

    def test_string_with_illegal_escape(self):
        input = r""" "This is a string \0" """
        expect = r"""Illegal Escape In String: This is a string \0"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 111))

    def test_string_with_legal_escape(self):
        input = r""" "\t8\t" """
        expect = r"""\t8\t,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 112))

    def test_string_with_comment_syntax_inside(self):
        input = r""" "123 ** comment **" """
        expect = r"""123 ** comment **,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 113))

    def test_normal_string(self):
        input = r""" "ErrorToken" """
        expect = r"""ErrorToken,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 114))

    def test_string_with_triple_quotes_escape(self):
        input = r""" "He asked me: '"Where is John?'"" """
        expect = r"""He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 115))

    def test_very_long_normal_string(self):
        input = """ "this is a very very very very very very very very very very long string" """
        expect = """this is a very very very very very very very very very very long string,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 116))

    def test_another_very_long_normal_string_with_special_keywords_inside(self):
        input = """ "int float string if else return for do while true false" """
        expect = """int float string if else return for do while true false,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 117))

    def test_normal_string_with_minus_sign(self):
        input = """ "float-of-string" """
        expect = """float-of-string,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 118))

    def test_unclosed_string_result_from_two_double_end_quotes(self):
        input = """ "Unclosed String: \"" """
        expect = """Unclosed String: ,Unclosed String:  """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 119))

    def test_four_double_quotes_result_in_two_empty_strings(self):
        input = """ "\"\"" """
        expect = """,,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 120))

    def test_string_with_lots_of_space(self):
        input = """ "                  " """
        expect = """                  ,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 121))

    def test_valid_backslash_escape_string(self):
        input = """ "Hello \\\\t" """
        expect = """Hello \\\\t,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 122))

    def test_string_with_tab_escape(self):
        input = """ "This is a string containing tab \\t" """
        expect = """This is a string containing tab \\t,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))

    def test_string_with_special_symbols_inside(self):
        input = """ "()[]:.,;{}" """
        expect = """()[]:.,;{},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))

    def test_string_special_quote_inside(self):
        input = """ "`" """
        expect = """`,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))

    #################################### Test literal ##############################
    def test_zero_tokens_as_intlit(self):
        input = """00"""
        expect = """0,0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))

    def test_intlit_tokens(self):
        input = """00 0123"""
        expect = """0,0,0,123,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))

    def test_octal_intlit(self):
        input = """0O77"""
        expect = """0O77,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

    def test_another_form_octal_intlit(self):
        input = """0o77"""
        expect = """0o77,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))

    def test_negative_hex_intlit_1(self):
        input = """-0X1234"""
        expect = """-,0X1234,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 130))

    def test_negative_hex_intlit_2(self):
        input = """-0x1234"""
        expect = """-,0x1234,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))

    def test_floatlit_with_dot_and_e(self):
        input = """10.e3"""
        expect = """10.e3,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 132))

    def test_floatlit_with_e_only(self):
        input = """10e3"""
        expect = """10e3,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 133))

    def test_floatlit_in_different_form_with_e(self):
        input = """0.01E-10"""
        expect = """0.01E-10,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))

    def test_floatlit_with_invalid_exponent_part(self):
        input = """.1e"""
        expect = """.1,e,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 135))

    def test_floatlit_with_valid_format(self):
        input = """1.23E-121"""
        expect = """1.23E-121,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 136))

    def test_invalid_space_in_floatlit(self):
        input = """123 E - 123"""
        expect = """123,Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 137))

    def test_many_floatlit(self):
        input = """.1 .2 .3"""
        expect = """.1,.2,.3,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 138))

    def test_valid_negative_floatlit(self):
        input = """- 123E-1"""
        expect = """-,123E-1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 139))

    def test_misunderstand_identifier(self):
        input = """0a"""
        expect = """0,a,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 140))

    def test_valid_negative_decimal_intlit(self):
        input = """-2637"""
        expect = """-,2637,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 141))

    ################################### Test keyword ######################################
    def test_two_adjacent_keywords(self):
        input = """EndWhileFor"""
        expect = """EndWhile,For,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 142))

    def test_body_keyword(self):
        input = """Body EndBody"""
        expect = """Body,EndBody,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 143))

    def test_continue_keyword(self):
        input = """Continue"""
        expect = """Continue,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 144))

    def test_break_keyword(self):
        input = """Break;"""
        expect = """Break,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 145))

    def test_if_keyword(self):
        input = """If"""
        expect = """If,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))

    def test_else_if_keyword(self):
        input = """ElseIf"""
        expect = """ElseIf,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))

    def test_invalid_else_if_keyword(self):
        input = """Elseif"""
        expect = """Else,if,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

    def test_else_keyword(self):
        input = """Else"""
        expect = """Else,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))

    def test_return_keyword(self):
        input = """Return"""
        expect = """Return,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))

    def test_for_keyword(self):
        input = """For"""
        expect = """For,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))

    def test_do_keyword(self):
        input = """Do"""
        expect = """Do,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))

    def test_while_keyword(self):
        input = """While"""
        expect = """While,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))

    def test_true_keyword(self):
        input = """True"""
        expect = """True,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))

    def test_false_keyword(self):
        input = """False"""
        expect = """False,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))

    def test_then_keyword(self):
        input = """Then;"""
        expect = """Then,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))

    def test_function_keyword(self):
        input = """Function: hello"""
        expect = """Function,:,hello,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))

    def test_parameter_keyword(self):
        input = """Parameter: n"""
        expect = """Parameter,:,n,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))

    def test_relational_keyword_symbols(self):
        input = """== != < <= >= > =/= <. >. <=. >=."""
        expect = """==,!=,<,<=,>=,>,=/=,<.,>.,<=.,>=.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 159))
    
    ################################### Test identifier ######################################
    def test_valid_identifier(self):
        input = """abc"""
        expect = """abc,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))
        
    def test_identifier_start_with_underscore(self):
        input = """_id"""
        expect = """Error Token _"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

    def test_valid_identifier_with_underscore_inside(self):
        input = """id_"""
        expect = """id_,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))

    def test_another_valid_identifier_with_lots_of_underscore_inside(self):
        input = """abc123_123abc__"""
        expect = """abc123_123abc__,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))
    
    def test_invalid_identifier_begin_upper_case(self):
        input = """Abc"""
        expect = """Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))

    def test_invalid_identifier_begin_with_number(self):
        input = """1abc"""
        expect = """1,abc,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

    def test_invalid_identifier_begin_with_error_char(self):
        input = """#abc"""
        expect = """Error Token #"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))

    
    ################################ Test expression ###############################

    def test_valid_variable_declaration(self):
        input = """Var: identifier"""
        expect = """Var,:,identifier,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))

    def test_valid_variable_initialization(self):
        input = """Var: a = 5;"""
        expect = """Var,:,a,=,5,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))

    def test_valid_sequence_of_tokens_like_pointer(self):
        input = """*p"""
        expect = """*,p,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))

    def test_valid_sequence_of_tokens_like_decrement(self):
        input = """a--"""
        expect = """a,-,-,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

    def test_valid_sequence_of_tokens_like_increment(self):
        input = """a++"""
        expect = """a,+,+,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 171))

    def test_valid_sequence_of_tokens_like_expression(self):
        input = """a && b == 1"""
        expect = """a,&&,b,==,1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

    def test_valid_sequence_of_tokens_like_comparison(self):
        input = """a == 1"""
        expect = """a,==,1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

    def test_valid_sequence_of_tokens_like_unequal_comparison(self):
        input = """a != 1"""
        expect = """a,!=,1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

    def test_valid_relational_expression_1(self):
        input = """a >= b"""
        expect = """a,>=,b,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 175))

    def test_valid_relational_expression_2(self):
        input = """a >=. b"""
        expect = """a,>=.,b,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

    def test_valid_relational_expression_3(self):
        input = """a =/= b"""
        expect = """a,=/=,b,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))

    def test_valid_sequence_of_tokens_like_assignment_expression(self):
        input = """foo(a)[x*y] = b[c[9]]+11;"""
        expect = """foo,(,a,),[,x,*,y,],=,b,[,c,[,9,],],+,11,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test_valid_sequence_of_tokens_like_function_declaration(self):
        input = """int foo(double n[80]) {"""
        expect = """int,foo,(,double,n,[,80,],),{,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))

    def test_valid_sequence_of_tokens_like_complicated_expression(self):
        input = """v = (4. \. 3.)*.3.14"""
        expect = """v,=,(,4.,\.,3.,),*.,3.14,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))
    
    def test_valid_sequence_of_tokens_with_comment(self):
        input = """boolean a[2]={false, false}; ** array declaration **"""
        expect = """boolean,a,[,2,],=,{,false,,,false,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))

    def test_valid_sequence_of_tokens_with_lots_of_whitespace(self):
        input = """int i, j, k = 10;"""
        expect = """int,i,,,j,,,k,=,10,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))
    
    ################################### Test error char ######################################
    def test_error_char(self):
        input = """ "\"\'" """
        expect = """,Error Token \'"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))

    def test_error_char_1(self):
        input = """|"""
        expect = """Error Token |"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))

    def test_error_char_2(self):
        input = """?"""
        expect = """Error Token ?"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))

    def test_error_char_3(self):
        input = """~"""
        expect = """Error Token ~"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 186))

    def test_error_char_4(self):
        input = """@"""
        expect = """Error Token @"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))

    def test_error_char_5(self):
        input = """#"""
        expect = """Error Token #"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))

    def test_error_char_6(self):
        input = """$"""
        expect = """Error Token $"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))

    def test_error_char_7(self):
        input = """EOF"""
        expect = """Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))

    def test_error_char_8(self):
        input = """Bool"""
        expect = """Error Token B"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))

    def test_error_char_9(self):
        input = """v = (4. \. 3.) /*. 3.14"""
        expect = """v,=,(,4.,\.,3.,),Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))

    ################################ Test comment #####################################

    def test_valid_single_line_comment(self):
        input = r"""
                ** @Author: Nguyen Tien Thanh **
                Var: x = 1;
                """
        expect = """Var,:,x,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))
    
    def test_valid_spanning_single_line_comments(self):
        input = r"""
                ** @Author: Nguyen Tien Thanh **
                ** A comment**
                Var: x = 1;
                ** Another comment at the end**
                """
        expect = """Var,:,x,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))
    
    def test_valid_multi_line_comment_1(self):
        input = r"""
                ** @Author: Nguyen Tien Thanh 
                 * This is a
                 * multi-line
                 * Comment
                **
                Var: x = 1;
                """
        expect = """Var,:,x,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))
    
    def test_valid_multi_line_comment_2(self):
        input = r"""
                ** @Author: Nguyen Tien Thanh 
                 * This is a
                 * multi-line
                 * Comment
                Var: x = 1;
                **
                """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))
    
    def test_strange_comment(self):
        input = r"""
                ** @Author: Nguyen Tien Thanh ***
                Var: x = 1;
                """
        expect = """*,Var,:,x,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))
    
    def test_unterminated_single_line_comment(self):
        input = r"""
                ** @Author: Nguyen Tien Thanh *
                Var: x = 1;
                """
        expect = """Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))
    
    def test_unterminated_multi_line_comment(self):
        input = r"""
                ** @Author: Nguyen Tien Thanh 
                 * This is
                 * a unterminated
                 * multi-line
                 * Comment
                /*
                Var: x = 1;
                """
        expect = """Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))
    
    def test_weird_comment_inside_array(self):
        input = r"""
                ** @Author: Nguyen Tien Thanh 
                 * This is weird testcase
                **
                Var: x, b[2] = {
                    ** This is a comment inside array **
                    1, 2, 5
                    ** another comment,
                    3, 4 **
                };
                """
        expect = """Var,:,x,,,b,[,2,],=,{,1,,,2,,,5,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))