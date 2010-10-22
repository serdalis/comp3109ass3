#!/usr/bin/evn python
import sys
sys.path.append('./build')
import antlr3
import antlr3.tree
from VPLLexer import VPLLexer
from VPLParser import VPLParser
import util
from codetemplates import *
from string import Template

char_stream = antlr3.ANTLRInputStream(sys.stdin)
lexer = VPLLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = VPLParser(tokens)
r = parser.start()

root = r.tree

sys.stderr.write(util.print_tree(root))

symbol_table = {}
lv = 0;

for func in root.children:
	
	stmts = "";
	
	for i, param in enumerate(func.children[0].children):
		symbol_table[str(param)] = par_template.substitute(var_num= str(i+1));
		
	for i, define in enumerate(func.children[1].children):
		symbol_table[str(define)] = getdefine_template.substitute(var_num= str(i+1));
		
	for statement in func.children[2].children:
		if(str(statement) == '='):
			if util.is_numeric(str(statement.children[1])):
				print consttable_template.substitute(val = float(str(statement.children[1])))
				symbol_table[str(statement.children[1])] = constaddr_template.substitute(val = float(str(statement.children[1])))
				ifn_c = ""
			elif str(statement.children[1]).isalpha():
				ifn_c = "addl $16, %ebx"
			sa = symbol_table[str(statement.children[1])] % {"destreg": "%ebx"}
			da = symbol_table[str(statement.children[0])] % {"destreg": "%eax"}
			stmts += equ_template.substitute(sourceaddr = sa, destaddr = da, loop_val = lv, ifnot_constant = ifn_c)
			lv += 1
		###TODO: Function Calls
		
	fbody = stmts;
	allocate = setdefine_template.substitute(var_num= len(func.children[1].children), body = fbody)
	print func_template.substitute(name= str(root.children[0]), body= allocate)


