grammar  VPL;

options {
	language=Python;
	output=AST;
}

tokens {
	
	BASE;
	PARAMS;
	DEFINES;
	STATEMENTS;

	FUNC = 'func';
	END = 'end';
	PLUS = '+';
	MINUS = '-';
	MULT = '*';
	DIV = '/';
	MIN = 'min';
	COMMA = ',';
	LB = '(';
	RB = ')';
	SEMICOLON = ';';
	EQUAL = '=';
	VAR = 'var';
	SCORE = '_';
}

/*----------------------------------------------------------------
* PARSER RULES
*-----------------------------------------------------------------*/

start : (function)* -> ^(BASE function*);
	
function : FUNC IDENT param define statements END;

param: (LB list RB)? ;

list: IDENT (COMMA IDENT)* ;

define: (VAR list SEMICOLON)? ;

statements: statement (SEMICOLON statement)* ;
	
statement: ((IDENT EQUAL arithmetic)? | IDENT LB list RB);
	
arithmetic :  atom (( MULT | DIV ) atom )* (( PLUS | MINUS ) atom (( MULT | DIV ) atom )*)*;
	
min : MIN LB arithmetic COMMA arithmetic RB;

nest : LB arithmetic RB;

atom : (IDENT | NUMBER | min | nest) ;

/*----------------------------------------------------------------
* LEXAR RULES
*-----------------------------------------------------------------*/

IDENT : (ALPHA|SCORE)+;

fragment
	ALPHA : 'A'..'Z' | 'a'..'z';

FLOAT
    :   NUMBER+ '.' NUMBER* EXPONENT?
    |   '.' NUMBER+ EXPONENT
    |   NUMBER+ EXPONENT
    ;

fragment
	EXPONENT : ('e'|'E') (PLUS|MINUS)? NUMBER+ ;

NUMBER : DIGIT+ ;

fragment
	DIGIT : '0'..'9' ;
 
WHITESPACE : ( '\t' | ' ' | '\r' | '\n' | '\u000C' )+ { $channel = HIDDEN; } ;
