import sys
from antlr4 import *
from Logo3DLexer import Logo3DLexer
from Logo3DParser import Logo3DParser
from visitor import EvalVisitor, Logo3DException

input_stream = FileStream(sys.argv[1])

lexer = Logo3DLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = Logo3DParser(token_stream)
tree = parser.root()

#print(tree.toStringTree(recog=parser))

if len(sys.argv) == 3:
    visitor = EvalVisitor(sys.argv[2])
elif len(sys.argv) > 3:
    visitor = EvalVisitor(sys.argv[2], [float(param) for param in sys.argv[3:]])
else:
    visitor = EvalVisitor()

try:
    visitor.visit(tree)
except Logo3DException as e:
    print(e.message)