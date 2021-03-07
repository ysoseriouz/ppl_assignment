/* Nguyen Tien Thanh _ 1852740 */

grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result
}

options{
	language=Python3;
}

// Tokens Set
// Keywords
BODY : 'Body' ;
BREAK : 'Break' ;
CONTINUE : 'Continue' ;
DO : 'Do' ;
ELSE : 'Else' ;
ELSEIF : 'ElseIf' ;
ENDBODY : 'EndBody' ;
ENDIF : 'EndIf' ;
ENDFOR : 'EndFor' ;
ENDWHILE : 'EndWhile' ;
FOR : 'For' ;
FUNCTION : 'Function' ;
IF : 'If' ;
PARAMETER : 'Parameter' ;
RETURN : 'Return' ;
THEN : 'Then' ;
VAR : 'Var' ;
WHILE : 'While' ;
ENDDO : 'EndDo' ;


WS : [ \f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines
CMT : '**' .*? '**' -> skip ; // skip comment

EQ : '=' ;
LP : '(' ;
RP : ')' ;
LS : '[' ;
RS : ']' ;
LB : '{' ;
RB : '}' ;
COLON : ':' ;
DOT : '.' ;
COMMA: ',' ;
SEMI: ';' ;
RELOP : '=='
      | '!='
      | '<'
      | '>'
      | '<='
      | '>='
      | '=/='
      | '<.'
      | '>.'
      | '<=.'
      | '>=.'
      ;

fragment LETTER : [a-zA-Z] ;
fragment DIGIT : [0-9] ;
fragment HEX : [0-9A-F] ;
fragment OCT : [0-7] ;
fragment CHAR : ~[\n'"\\] | '\\'[bfrnt'\\] | '\'' '"' ;

// Identifier
ID : [a-z] (LETTER | DIGIT | '_')* ;

// Literal
INTLIT : [1-9] DIGIT* 
       | ('0x' | '0X') [1-9A-F] HEX*
       | ('0o' | '0O') [1-7] OCT*
       | '0' 
       ;
FLOATLIT : DIGIT? DOT DIGIT* ([eE][+-]? DIGIT+)?
         | DIGIT+ DOT? DIGIT* [eE][+-]? DIGIT+
         ;
BOOLLIT : 'True' | 'False' ;

STRINGLIT : '"' CHAR*? '"'
        { 
            self.text = self.text[1:-1] 
        } 
        ;

arraylit : LB litlist? RB ;
litlist : literal (COMMA literal)* ;
literal : INTLIT
        | FLOATLIT  
        | BOOLLIT
        | STRINGLIT
        | arraylit
        ;

/*--------------------- Main program structure--------------------------- */
program  : globdecs funcdecs EOF ;
globdecs : vardec* ;
funcdecs : funcdec* ;

/*-------------------------Statement structure--------------------------- */
// Variable declaration statement
vardec : VAR COLON varlist (EQ initlist)? SEMI ;
varlist : variable (COMMA variable)* ;
// Variable definition
variable : ID dim* ;
dim : LS INTLIT RS ;
initlist : init (COMMA init)* ;
init : expr ;

// Assignment statement
assign : ID (LS expr RS)* EQ expr SEMI;

// If statement
ifstmt : IF cond_block (ELSEIF cond_block)* (ELSE stmtlist)? ENDIF DOT;
cond_block : expr THEN stmtlist ;

// For statement
forstmt : FOR LP iter_block RP DO stmtlist ENDFOR DOT ;
iter_block : iter_init COMMA iter_cond COMMA iter_update ;
iter_init : ID EQ expr ;
iter_cond : expr ;
iter_update : expr ;

// While statement
whilestmt : WHILE expr DO stmtlist ENDWHILE DOT ;

// Do-while statement
dowhilestmt : DO stmtlist WHILE expr ENDDO DOT ;

// Break statement
breakstmt : BREAK SEMI ;

// Continue statement
continuestmt : CONTINUE SEMI ;

// Function call statement
callstmt : call SEMI ;

// Return statement
returnstmt : RETURN expr? SEMI ;

// Statment list always begins with variable declarations
stmtlist : vardec* stmt* ;
stmt : assign 
     | ifstmt 
     | forstmt
     | whilestmt
     | dowhilestmt
     | breakstmt
     | continuestmt
     | callstmt
     | returnstmt
     ;
/*----------------------------------------------------------------------- */

// Function declaration
funcdec : FUNCTION COLON ID paramdec? bodydec ;
paramdec : PARAMETER COLON varlist ;
bodydec : BODY COLON stmtlist ENDBODY DOT ;

// Function call
call : ID LP exprlist? RP ;

// Expression
expr : relexpr RELOP relexpr | relexpr ;
relexpr : <assoc=right> ('-' | '-.') relexpr
     | <assoc=right> '!' relexpr
     | relexpr ('*' | '*.' | '\\' | '\\.' | '%') relexpr
     | relexpr ('+' | '+.' | '-' | '-.') relexpr
     | relexpr ('&&' | '||') relexpr
     | operand
     ;
operand : LP expr RP
        | call
        | ID (LS expr RS)+
        | ID
        | literal
        ;
// List of expressions
exprlist : expr (COMMA expr)* ;


UNCLOSE_STRING: '"' (~'"')* ( '\n' | EOF )
        { 
            self.text = self.text[1:]
        } 
        ;
ILLEGAL_ESCAPE: '"' CHAR* ( '\\' ~[bfrnt'\\] | '\'' ~'"' )
        { 
            self.text = self.text[1:]
        }
        ;
// UNTERMINATED_COMMENT: '**' (~'*')* '*' ~'*' ;
UNTERMINATED_COMMENT: '**' (~'*' | '*' ~'*')* EOF ;
ERROR_CHAR: . ;
