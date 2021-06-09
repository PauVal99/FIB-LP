import sys
from antlr4 import *
from Logo3DLexer import Logo3DLexer
from Logo3DParser import Logo3DParser
from visitor import EvalVisitor

input_stream = FileStream(sys.argv[1])
lexer = Logo3DLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = Logo3DParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))
visitor = EvalVisitor()
visitor.visit(tree)