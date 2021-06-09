if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor
class TreeVisitor(ExprVisitor):
    def __init__(self):
        self.nivell = 0
        
    def visitExpr(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            print("  " * self.nivell +
                  ExprParser.symbolicNames[l[0].getSymbol().type] +
                  '(' +l[0].getText() + ')')
        else:  # len(l) == 3
            print('  ' *  self.nivell + ExprParser.symbolicNames[l[1].getSymbol().type] + '(' +l[1].getText() + ')')
            self.nivell += 1
            self.visit(l[0])
            self.visit(l[2])
            self.nivell -= 1