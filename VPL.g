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
	
function : FUNC! IDENT^ param define statements END!;

param: (LB list RB)? -> ^(PARAMS list);

list: IDENT (COMMA! IDENT)* ;

define: (VAR list SEMICOLON)? -> ^(DEFINES list?);

statements: statement (SEMICOLON statement)* -> ^(STATEMENTS statement*);
	
statement: ((IDENT EQUAL^ e)? | IDENT^ LB! list RB!) ;

e: e2((PLUS|MINUS)^ e2)*;

e2: e3((MULT|DIV)^ e3)*;
	
min : MIN^ LB! e COMMA! e RB!;

nest : LB! e RB!;

e3 : (IDENT | NUMBER | min | nest) ;

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
