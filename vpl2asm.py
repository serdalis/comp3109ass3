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

op_table = {"+": "addps", "-": "subps", "*": "mulps", "/": "divps"}

for func in root.children:
	
	local_var_count = 0;
	stmts = "";
	
	for i, param in enumerate(func.children[0].children):
		symbol_table[str(param)] = par_template.substitute(var_num= str(i+1));
		
	for i, define in enumerate(func.children[1].children):
		symbol_table[str(define)] = getdefine_template.substitute(var_num= str(i+1));
		varcount += 1;
		
	for statement in func.children[2].children:
		if(str(statement) == '='):
			if str(statement.children[1]) in op_table:
				op_parent = statement.children[1]
				if str(op_parent) not in symbol_table:
					symbol_table[str(statement.children[0])] = getdefine_template.substitute(var_num= local_var_count +1);
					local_var_count += 1;
				if util.is_numeric(str(op_parent.children[0])):
					if str(op_parent.children[0]) not in symbol_table:
						print consttable_template.substitute(val = float(str(op_parent.children[0])))
						symbol_table[str(op_parent.children[0])] = constaddr_template.substitute(val = float(str(op_parent.children[0])))
					ifn_c1 = ""
				elif str(op_parent.children[0]).isalpha():
					ifn_c1 = "addl $16, %ebx"
				if util.is_numeric(str(op_parent.children[1])):
					if str(op_parent.children[1]) not in symbol_table:
						print consttable_template.substitute(val = float(str(op_parent.children[1])))
						symbol_table[str(op_parent.children[1])] = constaddr_template.substitute(val = float(str(op_parent.children[1])))
					ifn_c2 = ""
				elif str(op_parent.children[1]).isalpha():
					ifn_c2 = "addl $16, %edx"
					
				sa1 = symbol_table[str(op_parent.children[0])] % {"destreg": "%ebx"}
				sa2 = symbol_table[str(op_parent.children[1])] % {"destreg": "%edx"}
				da = symbol_table[str(statement.children[0])] % {"destreg": "%eax"}
				stmts += equWithOp_template.substitute(sourceaddr_1 = sa1, sourceaddr_2 = sa2, destaddr = da, loop_val = lv, operation = op_table[str(op_parent)], ifnot_constant_1 = ifn_c1, ifnot_constant_2 = ifn_c2)
				lv += 1
			else:
				if str(statement.children[0]) not in symbol_table:
					symbol_table[str(statement.children[0])] = getdefine_template.substitute(var_num= local_var_count +1);
					local_var_count += 1;
				if util.is_numeric(str(statement.children[1])):
					if str(statement.children[1]) not in symbol_table:
						print consttable_template.substitute(val = float(str(statement.children[1])))
						symbol_table[str(statement.children[1])] = constaddr_template.substitute(val = float(str(statement.children[1])))
					ifn_c = ""
				elif str(statement.children[1]).isalpha():
					ifn_c = "addl $16, %ebx"
					
				sa = symbol_table[str(statement.children[1])] % {"destreg": "%ebx"}
				da = symbol_table[str(statement.children[0])] % {"destreg": "%eax"}
				stmts += equ_template.substitute(sourceaddr = sa, destaddr = da, loop_val = lv, ifnot_constant = ifn_c)
				lv += 1
		###else:
			
		
	fbody = stmts;
	allocate = setdefine_template.substitute(var_num= util.max_locals(func), body = fbody)
	print func_template.substitute(name= str(root.children[0]), body= allocate)


