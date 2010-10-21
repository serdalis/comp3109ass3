import re
import codetemplates

ident = re.compile('[a-zA-Z_]+')
COMPERR = "unknown token reached!\n"
FUNCT_FOUND = "function %(fun)s found\n"
LOC_VAR_FOUND = "local variable found %(var)s\n"
DEFINE_FOUND = "DEFINES found with %(def)s\n" 
LIST_FOUND = "list found with %(list)d\n" 
MIN_FOUND = "min found\n"
IDENT_FOUND = "ident %(ident)s found\n"
ASSIGN_FOUND = "assign %(base)s to %(ident)s found\n"

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
					out += element(t.children, out)
				elif len(t.children) > 1:
					out += LIST_FOUND % { "list":len(t.children) }
				else:
					return COMPERR
		else:
			return COMPERR
	return out
# END funct

# handles all E cases
# assuming level = 0, then the variables are global
# assuming level >= 1, then the variables are local
# parameter variables are unknown at the moment
# const variables may be == global
def element(childs, out):
	base = childs[0]
	# E + E, nesting not working
	if str(childs[1]) in ['+', '-', '\\', '*']:
		out = element(childs[1].children, out)
		
	# min (E,E) not working
	elif str(childs[1]) == "min":
		out = MIN_FOUND
		out += element(childs[1].children, out)
	
	# IDENT
	elif ident.match(str(childs[1])):
		return IDENT_FOUND % { "ident":str(childs[0]) }
	
	# NUM
	elif str(childs[1]).isdigit():
		return ASSIGN_FOUND % { "base":str(childs[1]), "ident":str(childs[0]) }
	
	else:
		return COMPERR
	return out
# END element
