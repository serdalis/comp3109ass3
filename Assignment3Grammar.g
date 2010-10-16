grammar Assignment3Grammar;

options {
    language=C;
}

tokens {
	PLUS 	= '+' ;
	MINUS	= '-' ;
	MULT	= '*' ;
	DIV	= '/' ;
	DEL	= ';' ;
	EQUAL	= '=' ;
	LB	= '(' ;
	RB	= ')' ;
	COMMA	= ',' ;
}


@members {

 #include "Assignment3Grammar.h"

 int main(int argc, char * argv[]) {

    pANTLR3_INPUT_STREAM           input;
    pSimpleCalcLexer               lex;
    pANTLR3_COMMON_TOKEN_STREAM    tokens;
    pSimpleCalcParser              parser;

    input  = antlr3AsciiFileStreamNew          ((pANTLR3_UINT8)argv[1]);
    lex    = SimpleCalcLexerNew                (input);
    tokens = antlr3CommonTokenStreamSourceNew  (ANTLR3_SIZE_HINT, TOKENSOURCE(lex));
    parser = SimpleCalcParserNew               (tokens);

    parser  ->expr(parser);

    // Must manually clean up
    //
    parser ->free(parser);
    tokens ->free(tokens);
    lex    ->free(lex);
    input  ->close(input);

    return 0;
 }

}

/*------------------------------------------------------------------
 * PARSER RULES
 *------------------------------------------------------------------*/
 // DONE
prog   
    :  func*
    ;
// DONE	
func   
    :  FUNC IDENT parameter declare sequence END
    ;
// DONE
parameter   
    :  (LB list RB)?
    ;
// DONE
list   
    :  (IDENT COMMA)* IDENT
    ;
// DONE
declare  
    :  VAR list
    ;
	
sequence   
    :   (IDENT EQUAL element DEL|IDENT LB list RB)* 
        (IDENT EQUAL element|IDENT LB list RB)?
    ;

element
    :  arithmatic
    |  emin
    |  elist
    |  atom
    ;

arithmatic
    :  (element (PLUS|MINUS|MULT|DIV))+ element
    ;

emin
    :  MIN LB element COMMA element RB
    ;

elist
    :  LB element RB
    ;
    
atom
    :  IDENT
    |  FLOAT
    ;
    
/*------------------------------------------------------------------
 * LEXER RULES
 *------------------------------------------------------------------*/
FUNC	: 'func';
END	: 'end';
VAR	: 'var';
MIN	: 'min';

IDENT  :  ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')* ;

FLOAT
    :   ('0'..'9')+ '.' ('0'..'9')* EXPONENT?
    |   '.' ('0'..'9')+ EXPONENT?
    |   ('0'..'9')+ EXPONENT
    ;

fragment
EXPONENT : ('e'|'E') (PLUS|MINUS)? ('0'..'9')+ ;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) {$channel=HIDDEN;}
    ;