import sys
sys.path.append('./build')
import antlr3
import antlr3.tree
from VPLLexer import VPLLexer
from VPLParser import VPLParser
import util

char_stream = antlr3.ANTLRStringStream()
lexer = VPLLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = VPLParser(tokens)
r = parser.start()

root = r.tree

sys.stderr.write(util.print_tree(root))

#nodes = antlr3.tree.CommonTreeNodeStream(root)
#nodes.setTokenStream(tokens)
#walker = VPLWalker(nodes)
#walker.entry_rule()
