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
temp_vars = []
lv = 0;

op_table = {"+": "addps", "-": "subps", "*": "mulps", "/": "divps"}

def is_operator(op_parent, destination, local_var_count, lv):
	
	asm = ""
	
	for child in op_parent.children:
		if str(child) in op_table:
			tvar = getdefine_template.substitute(var_num = str(local_var_count))
			local_var_count += 1
			asm += is_operator(child, tvar, local_var_count, lv)
			if int(str(child.getChildIndex())) == 0:
				ifn_c1 = ""
				sa1 = tvar % {"destreg": "%ebx"}
			else:
				ifn_c2 = ""
				sa2 = tvar % {"destreg": "%edx"}
		else:
			if util.is_numeric(str(child)):
				if str(child) not in symbol_table:
					print consttable_template.substitute(val = float(str(child)))
					symbol_table[str(child)] = constaddr_template.substitute(val = float(str(child)))
				if int(str(child.getChildIndex())) == 0:
					ifn_c1 = ""
				else:
					ifn_c2 = ""
			elif str(child).isalpha():
				if int(str(child.getChildIndex())) == 0:
					ifn_c1 = "addl $16, %ebx"
				else:
					ifn_c2 = "addl $16, %edx"
		
			if int(str(child.getChildIndex())) == 0:
				sa1 = symbol_table[str(child)] % {"destreg": "%ebx"}
			else:
				sa2 = symbol_table[str(child)] % {"destreg": "%edx"}
	
	if str(destination) in symbol_table:
		da = symbol_table[str(destination)] % {"destreg": "%eax"}
	else:
		da = destination % {"destreg": "%eax"}
	asm += equWithOp_template.substitute(sourceaddr_1 = sa1, sourceaddr_2 = sa2, destaddr = da, loop_val = lv, operation = op_table[str(op_parent)], ifnot_constant_1 = ifn_c1, ifnot_constant_2 = ifn_c2)
	lv += 1
	return asm
	
for func in root.children:

	local_var_count = 0;
	stmts = "";

	for i, param in enumerate(func.children[0].children):
		symbol_table[str(param)] = par_template.substitute(var_num= str(i+1));

	for i, define in enumerate(func.children[1].children):
		symbol_table[str(define)] = getdefine_template.substitute(var_num= str(i+1));
		local_var_count += 1;

	for statement in func.children[2].children:
		if(str(statement) == '='):
			if str(statement.children[1]) in op_table:
				if str(str(statement.children[0])) not in symbol_table:
					symbol_table[str(statement.children[0])] = getdefine_template.substitute(var_num= local_var_count +1)
					local_var_count += 1
				stmts += is_operator(statement.children[1], statement.children[0], local_var_count, lv)
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