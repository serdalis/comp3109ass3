import re

ident = re.compile('[a-zA-Z_]+')
COMPERR = "unknown token reached!\n"

# noticed something with the element part of the tree, when using  min, +, -, /, * etc 

# traverse the tree and look for the lowest level parents
def traverse_tree(root, out=""):
  if str(root) == "BASE":
    if ident.match(str(root)):
      funct(root.children, out)
  return out
      
# used for when a function is called
# goes through the PARAMS and initializes
# then goes through DEFINES and does stuff
# then goes through STATMENTS and executes
# then returns out
def funct(root, out):

    if str(root) == "PARAMS":
      for t in root.children:
        out += "local variable template for %(var)s\n" % { "var":str(t) }

    else if str(root) == "DEFINES":
      for t in root.children:
        out += "defines template for %(def)s\n" % { "def":str(t) } 

    else if str(root) == "STATEMENTS": 
      for t in root.children:
        if str(t) == "=":
          out += element(t.children, out)
        else if str(t) == "nest":
          pass
        else:
          out += COMPERR
    
    else:
      return COMPERR
    return out
# END funct

# assuming level = 0, then the variables are global
# assuming level >= 1, then the variables are local
# parameter variables are unknown at the moment
# const variables may be == global
def element( childs, out):
  base = childs[0]
  # E + E
  if str(childs[1]) in ['+', '-', '\', '*']:
    out += element(childs[1].children, out)

  # min (E,E)
  else if str(childs[1]) == "min":
    out += element(childs[1].children, out)

  # IDENT
  else if ident.match(str(childs[1])):
    return "%(ident)s template\n" % { "ident":str(childs[0]) }

  # NUM
  else if str(root).isdigit():
    return "assign %(base)s to %(ident)s template\n" % { "base":str(childs[0]), "ident":str(childs[1]) }

  else:
    return COMPERR
  return out
# END element