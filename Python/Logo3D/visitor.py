if __name__ is not None and "." in __name__:
    from .Logo3DParser import Logo3DParser
    from .Logo3DVisitor import Logo3DVisitor
else:
    from Logo3DParser import Logo3DParser
    from Logo3DVisitor import Logo3DVisitor
from collections import defaultdict
from Turtle3D import Turtle3D


class Logo3DException(Exception):
    def __init__(self, message):
        self.message = 'Error: ' + message


class Process:
    def __init__(self, name, params, inss):
        self.name = name
        self.params = params
        self.inss = inss


class EvalVisitor(Logo3DVisitor):
    __TURTLE_LIBRARY = [
        'left',
        'right',
        'up',
        'down',
        'forward',
        'backward',
        'color',
        'hide',
        'show',
        'home'
    ]

    def __init__(self, entryProc='main', entryParams=[]):
        self.entryProc = entryProc
        self.entryParams = entryParams

        self.turtle = Turtle3D()
        self.procs = {}
        self.stack = []

    def __turtle__(self, name, paramsValues):
        getattr(self.turtle, name)(*paramsValues)

    def __proc__(self, name, paramsValues):
        if len(self.procs[name].params) != len(paramsValues):
            raise Logo3DException('In \"' + name + '\" proc expected ' + str(len(
                self.procs[name].params)) + ' param(s), ' + str(len(paramsValues)) + ' given.')
        variables = defaultdict(lambda: 0)
        for param, value in zip(self.procs[name].params, paramsValues):
            variables[param] = value
        self.stack.append(variables)
        self.visit(self.procs[name].inss)
        self.stack.pop()

    # Visit a parse tree produced by Logo3DParser#root.
    def visitRoot(self, ctx):
        for proc in list(ctx.getChildren()):
            self.visit(proc)
        self.__proc__(self.entryProc, self.entryParams)

    # Visit a parse tree produced by Logo3DParser#inss.
    def visitInss(self, ctx):
        for ins in list(ctx.getChildren()):
            self.visit(ins)

    # Visit a parse tree produced by Logo3DParser#ins.
    def visitIns(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3DParser#input_.
    def visitInput_(self, ctx):
        self.stack[-1][ctx.getChild(1).getText()] = float(input())

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
        self.stack[-1][ctx.VAR().getText()] = self.visit(ctx.expr(0))
        while self.stack[-1][ctx.VAR().getText()] <= self.visit(ctx.expr(1)):
            self.visit(ctx.inss())
            self.stack[-1][ctx.VAR().getText()] += 1

    # Visit a parse tree produced by Logo3DParser#proc.
    def visitProc(self, ctx):
        name = ctx.PROCNAME().getText()[:-1]
        i = 1
        paramsValues = []
        while ctx.getChild(i).getText() != ')':
            if ctx.getChild(i).getText() != ',':
                paramsValues.append(self.visit(ctx.getChild(i)))
            i += 1

        if name in self.__TURTLE_LIBRARY:
            self.__turtle__(name, paramsValues)
        elif name in self.procs:
            self.__proc__(name, paramsValues)
        else:
            raise Logo3DException('Proc \"' + name + '\" not defined.')

    # Visit a parse tree produced by Logo3DParser#procDef.
    def visitProcDef(self, ctx):
        name = ctx.PROCNAME().getText()[:-1]
        i = 2
        params = []
        while ctx.getChild(i).getText() != ')':
            if ctx.getChild(i).getText() != ',':
                param = ctx.getChild(i).getText()
                if param in params:
                    raise Logo3DException(
                        'Duplicated param in \"' + name + '\" proc definition.')
                else:
                    params.append(ctx.getChild(i).getText())
            i += 1
        if name in self.procs:
            raise Logo3DException('Proc \"' + name + '\" already defined.')
        elif name in self.__TURTLE_LIBRARY:
            raise Logo3DException(
                'In \"' + name + '\" proc, cannot override language procs.')
        else:
            self.procs[name] = Process(name, params, ctx.inss())

    # Visit a parse tree produced by Logo3DParser#assign.
    def visitAssign(self, ctx):
        self.stack[-1][ctx.VAR().getText()] = self.visit(ctx.expr())

    # Visit a parse tree produced by Logo3DParser#Mul.
    def visitMul(self, ctx):
        return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

    # Visit a parse tree produced by Logo3DParser#Var.
    def visitVar(self, ctx):
        return self.stack[-1][ctx.VAR().getText()]

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
        den = self.visit(ctx.expr(1))
        if den == 0:
            raise Logo3DException('Division by zero.')
        return self.visit(ctx.expr(0)) / den

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

    # Visit a parse tree produced by Logo3DParser#Mod.
    def visitMod(self, ctx):
        return self.visit(ctx.expr(0)) % self.visit(ctx.expr(1))
