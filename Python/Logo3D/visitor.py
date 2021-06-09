if __name__ is not None and "." in __name__:
    from .Logo3DParser import Logo3DParser
    from .Logo3DVisitor import Logo3DVisitor
else:
    from Logo3DParser import Logo3DParser
    from Logo3DVisitor import Logo3DVisitor
from collections import defaultdict


class EvalVisitor(Logo3DVisitor):
    def __init__(self):
        self.variables = defaultdict(lambda: 0)

    # Visit a parse tree produced by Logo3DParser#root.
    def visitRoot(self, ctx):
        self.visitInss(ctx)

    # Visit a parse tree produced by Logo3DParser#inss.
    def visitInss(self, ctx):
        for ins in list(ctx.getChildren()):
            self.visit(ins)

    # Visit a parse tree produced by Logo3DParser#ins.
    def visitIns(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3DParser#input_.
    def visitInput_(self, ctx):
        self.variables[ctx.getChild(1).getText()] = float(input())

    # Visit a parse tree produced by Logo3DParser#output_.
    def visitOutput_(self, ctx):
        print(('%f' % self.visit(ctx.expr())).rstrip('0').rstrip('.')) 

    # Visit a parse tree produced by Logo3DParser#condition.
    def visitCondition(self, ctx):
        if self.visit(ctx.expr()) == 1:
            self.visit(ctx.inss(0))
        elif ctx.getChild(4).getText() == 'ELSE':
            self.visit(ctx.inss(1))

    # Visit a parse tree produced by Logo3DParser#while_.
    def visitWhile_(self, ctx):
        while self.visit(ctx.expr()) == 1:
            self.visit(ctx.inss())

    # Visit a parse tree produced by Logo3DParser#for_.
    def visitFor_(self, ctx):
        self.variables[ctx.VAR().getText()] = int(self.visit(ctx.expr(0)))
        while self.variables[ctx.VAR().getText()] < int(self.visit(ctx.expr(1))):
            self.visit(ctx.inss())
            self.variables[ctx.VAR().getText()] += 1

    # Visit a parse tree produced by Logo3DParser#procDef.
    def visitProcDef(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3DParser#proc.
    def visitProc(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3DParser#assign.
    def visitAssign(self, ctx):
        self.variables[ctx.VAR().getText()] = self.visit(ctx.expr())

    # Visit a parse tree produced by Logo3DParser#Mul.
    def visitMul(self, ctx):
        return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

    # Visit a parse tree produced by Logo3DParser#Var.
    def visitVar(self, ctx):
        return self.variables[ctx.VAR().getText()]

    # Visit a parse tree produced by Logo3DParser#Parens.
    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by Logo3DParser#Num.
    def visitNum(self, ctx):
        return float(ctx.NUM().getText())

    # Visit a parse tree produced by Logo3DParser#Lt.
    def visitLt(self, ctx):
        return int(self.visit(ctx.expr(0)) < self.visit(ctx.expr(1)))

    # Visit a parse tree produced by Logo3DParser#Sum.
    def visitSum(self, ctx):
        return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))

    # Visit a parse tree produced by Logo3DParser#Eq.
    def visitEq(self, ctx):
        return int(self.visit(ctx.expr(0)) == self.visit(ctx.expr(1)))

    # Visit a parse tree produced by Logo3DParser#Gt.
    def visitGt(self, ctx):
        return int(self.visit(ctx.expr(0)) > self.visit(ctx.expr(1)))

    # Visit a parse tree produced by Logo3DParser#Div.
    def visitDiv(self, ctx):
        return self.visit(ctx.expr(0)) / self.visit(ctx.expr(1))

    # Visit a parse tree produced by Logo3DParser#Min.
    def visitMin(self, ctx):
        return self.visit(ctx.expr(0)) - self.visit(ctx.expr(1))

    # Visit a parse tree produced by Logo3DParser#Get.
    def visitGet(self, ctx):
        return int(self.visit(ctx.expr(0)) >= self.visit(ctx.expr(1)))

    # Visit a parse tree produced by Logo3DParser#Let.
    def visitLet(self, ctx):
        return int(self.visit(ctx.expr(0)) <= self.visit(ctx.expr(1)))

    # Visit a parse tree produced by Logo3DParser#Neq.
    def visitNeq(self, ctx):
        return int(self.visit(ctx.expr(0)) != self.visit(ctx.expr(1)))
