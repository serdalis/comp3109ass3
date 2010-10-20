grammar  VPL;

options {
	language=Python;
	output=AST;
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
	: (function)* EOF!
	;
	
function 
    @init { 
    parsed = 0; 
    PRINTOUT = "";
    }
    @after { 
    	if (parsed):
    		#do shit    
    }
	: FUNC IDENT param define statment END
	;
param
    @init { 
    parsed = 0; 
    PRINTOUT = "";
    }
    @after { 
    	if (parsed):
    		#do shit    
    }
	: (LB list RB)?
	;
list
    @init { 
    parsed = 0; 
    PRINTOUT = "";
    }
    @after { 
    	if (parsed):
     		#do shit   
    }
	: IDENT (COMMA IDENT)*
	;
define
    @init { 
    parsed = 0; 
    PRINTOUT = "";
    }
    @after { 
    	if (parsed):
    		#do shit    
    }
	: (VAR list)+
	;
	
statment
    @init { 
    parsed = 0; 
    PRINTOUT = "";
    }
    @after { 
    	if (parsed):
    		#do shit
    } 
	: (((IDENT EQUAL (arithmatic | min | nest | atom)) | (IDENT LB list RB)) COLEN)*
	;
	
arithmatic 
	: (( min | nest | atom) (PLUS | MINUS | MULT | DIV))*(min | nest | atom)
	; 
	
min     : MIN LB (arithmatic | nest | atom) COMMA (arithmatic | nest | atom) RB
	;
nest 
	: (LB (arithmatic | min | atom) RB)+
	;
atom 
    @init { 
    parsed = 0; 
    PRINTOUT = "";
    }
    @after { 
    	if (parsed):
    		#do shit    
    } 
	: IDENT | NUMBER
	;
/*----------------------------------------------------------------
* LEXAR RULES
*-----------------------------------------------------------------*/
IDENT : (ALPHA | SCORE)(STRING)*;

STRING : (ALPHA | NUMBER | SCORE)*;

fragment
	ALPHA : ('A'..'Z' | 'a'..'z');

FLOAT
    :   NUMBER+ '.' NUMBER* EXPONENT?
    |   '.' NUMBER+ EXPONENT
    |   NUMBER+ EXPONENT
    ;

fragment
	EXPONENT : ('e'|'E') (PLUS|MINUS)? NUMBER+ ;

NUMBER : (DIGIT)+ ;

fragment
	DIGIT : '0'..'9' ;
 
WHITESPACE : ( '\t' | ' ' | '\r' | '\n' | '\u000C' )+ { $channel = HIDDEN; } ;
