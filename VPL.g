grammar  VPL;

options {
	language=Python;
	output=AST;
	ASTLabelType=CommonTree;
}

tokens {
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
	COLEN = ';';
	EQUAL = '=';
	VAR = 'var';
	SCORE = '_';
}

/*----------------------------------------------------------------
* PARSER RULES
*-----------------------------------------------------------------*/
start 
	: (function)*
	;
function 
	: FUNC IDENT param define statment END
	;
param
	: (LB list RB)?
	;
list
	: ident (COMMA ident)*
	;
define 
	: (VAR list)+;
statment 
	: ((IDENT EQUAL element) | (IDENT LB list RB) COLEN)*
	;
element 
	: arithmatic | min | nest | atom
	;
arithmatic 
	: (element|atom) (PLUS | MINUS | MULT | DIV) (element|atom)
	; 
min : MIN LB element COMMA element RB
	;
nest 
	: LB element RB
	;
atom 
	: IDENT | NUMBER
	;
/*----------------------------------------------------------------
* LEXAR RULES
*-----------------------------------------------------------------*/
IDENT : (ALPHA | SCORE)(STRING)*;

STRING : (ALPHA | NUMBER | SCORE)*;

fragment
	ALPHA : ('A'..'Z' | 'a'..'z');

NUMBER : (DIGIT)+ ;
 
WHITESPACE : ( '\t' | ' ' | '\r' | '\n' | '\u000C' )+ { $channel = HIDDEN; } ;

fragment
	DIGIT : '0'..'9' ;
