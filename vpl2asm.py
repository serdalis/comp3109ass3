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

for func in root.children:
	for i, param in enumerate(func.children[0].children):
		symbol_table[str(param)] = par_template.substitute(var_num= str(i));
	print symbol_table
	for i, define in enumerate(func.children[1].children):
		symbol_table[str(define)] = getdefine_template.substitute(var_num= str(i));
	for statement in func.children[2].children:
		if(str(statement) == '='):
			print "assignment"
		else:
			print str(statement)
	fbody = "";
	allocate = setdefine_template.substitute(var_num= len(func.children[1].children), body = fbody)
	print func_template.substitute(name= str(root.children[0]), body= allocate)


