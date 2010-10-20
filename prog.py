import antlr3
import antlr3.tree
from VPLLexer import VPLLexer
from VPLParser import VPLParser
from VPLWalker import VPLWalker

char_stream = antlr3.ANTLRStringStream("sentence.grm")
lexer = VPLLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = VPLParser(tokens)
r = parser.entry_rule()

root = r.tree

nodes = antlr3.tree.CommonTreeNodeStream(root)
nodes.setTokenStream(tokens)
walker = VPLWalker(nodes)
walker.entry_rule()
