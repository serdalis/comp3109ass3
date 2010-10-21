import re

ident = re.compile('[a-zA-Z_]+')

# traverse the tree and look for the lowest level parents
def traverse_tree(root, out="", level=0):
  if level == 0:
    out += str(root) + "\n"
  else:
    # ident = E, only way E can be accessed
    if str(root) == '=':
      for t in root.children:
        element(t, out, level + 1)
    
# assuming level = 0, then the variables are global
# assuming level >= 1, then the variables are local
# parameter variables are unknown at the moment
# const variables may be == global
def element(root, out="", level=0):
  # E + E
  if str(root) in ['+', '-', '\', '*']:
    for t in root.children:
    out += "element = element %(sign)s element\n" % { "sign":str(root) }
    for t in root.children:
      out += element(t, out, level + 1)

  # min (E,E)
  if str(root) == "min":
    out += "min template\n"
    for t in root.children:
      out += element(t, out, level + 1)

  # IDENT
  if ident.match(str(root)):
    return "%(ident)s template\n" % { "ident":str(root) }

  # NUM
  if str(root).isdigit():
    return "%(ident)s template\n" % { "ident":str(root) }
# END element