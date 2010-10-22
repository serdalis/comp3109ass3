import re
import codetemplates

ident = re.compile('[a-zA-Z_]+')
COMPERR = "unknown token reached!\n"
FUNCT_FOUND = "function %(fun)s found\n"
LOC_VAR_FOUND = "local variable found %(var)s\n"
DEFINE_FOUND = "DEFINES found with %(def)s\n" 
LIST_FOUND = "list found with %(list)d\n" 
IDENT_OP_FOUND = "%(base)s %(op)s %(rest)s "
MIN_FOUND = "min %(inner)s "
IDENT_FOUND = "ident %(ident)s "
ASSIGN_FOUND = "assign %(base)s to %(ident)s "

# traverse the tree and look for the lowest level parents
def traverse_tree(root, out=""):
	# handles M cases
	if str(root) == "BASE": 
		for t in root.children: 
			if ident.match(str(t)):
				out += FUNCT_FOUND % { "fun":str(t) } 
				out = funct(t.children, out)
	return out

# handles all F cases
# used for when a function is called
# goes through the PARAMS and initializes
# then goes through DEFINES and does stuff
# then goes through STATMENTS and executes
# then returns out
def funct(root, out):
	# handles all 'P' cases
	for i in root:
		if str(i) == "PARAMS":
			for t in i.children:
				out += LOC_VAR_FOUND % { "var":str(t) }

		# handles all 'D' cases
		elif str(i) == "DEFINES":
			for t in i.children:
				out += DEFINE_FOUND % { "def":str(t) }

		# handles all 'S' cases
		elif str(i) == "STATEMENTS": 
			for t in i.children:
				if str(t) == "=":
					out += element(t, out) + "\n"
				elif len(t.children) > 1:
					out += LIST_FOUND % { "list":len(t.children) }
				else:
					return COMPERR
		
		# return compiler error on failure
		else:
			return COMPERR
	return out
# END funct

# handles all E cases
# assuming level = 0, then the variables are global
# assuming level >= 1, then the variables are local
# parameter variables are unknown at the moment
# const variables may be == global
def element(root, out):
	# set the 2 children expected from element
	base = root.children[0]
	op = root.children[1]

	# check for E + | - | / | * E
	if str(op) in ['+', '-', '/', '*']: 
		out = IDENT_OP_FOUND % { "rest":element(op, out), "op":str(op), "base":str(base) }

	# check for min( E, E)
	elif str(op) == "min":
		out = MIN_FOUND % { "inner":element(op, out) }

	# check for E = num
	elif str(op).isdigit():
		out = ASSIGN_FOUND % {"base":str(base), "ident":str(op) }
	
	#check for other E cases
	elif ident.match(str(op)):
		# if both E are IDENTS
		if ident.match(str(base)):
			# nested operations
			if str(root) in ['+', '-', '/', '*']:
				out = str(base) + " " + str(op)
			# assign ident to ident
			else:
				out = ASSIGN_FOUND % { "base":str(base), "ident":str(op) }
		# assign num to ident
        elif str(base).isdigit():
			out = IDENT_FOUND % { "ident":str(base) }
	else:
		return COMPERR
	return out
# END element
