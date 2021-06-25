# Generated from Logo3D.g by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Logo3DParser import Logo3DParser
else:
    from Logo3DParser import Logo3DParser

# This class defines a complete generic visitor for a parse tree produced by Logo3DParser.

class Logo3DVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Logo3DParser#root.
    def visitRoot(self, ctx:Logo3DParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#inss.
    def visitInss(self, ctx:Logo3DParser.InssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#ins.
    def visitIns(self, ctx:Logo3DParser.InsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#input_.
    def visitInput_(self, ctx:Logo3DParser.Input_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#output_.
    def visitOutput_(self, ctx:Logo3DParser.Output_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#condition.
    def visitCondition(self, ctx:Logo3DParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#while_.
    def visitWhile_(self, ctx:Logo3DParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#for_.
    def visitFor_(self, ctx:Logo3DParser.For_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#procDef.
    def visitProcDef(self, ctx:Logo3DParser.ProcDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#proc.
    def visitProc(self, ctx:Logo3DParser.ProcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#assign.
    def visitAssign(self, ctx:Logo3DParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Mod.
    def visitMod(self, ctx:Logo3DParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Mul.
    def visitMul(self, ctx:Logo3DParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Var.
    def visitVar(self, ctx:Logo3DParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Parens.
    def visitParens(self, ctx:Logo3DParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Num.
    def visitNum(self, ctx:Logo3DParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Lt.
    def visitLt(self, ctx:Logo3DParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Sum.
    def visitSum(self, ctx:Logo3DParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Eq.
    def visitEq(self, ctx:Logo3DParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Gt.
    def visitGt(self, ctx:Logo3DParser.GtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Div.
    def visitDiv(self, ctx:Logo3DParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Min.
    def visitMin(self, ctx:Logo3DParser.MinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Get.
    def visitGet(self, ctx:Logo3DParser.GetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Let.
    def visitLet(self, ctx:Logo3DParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3DParser#Neq.
    def visitNeq(self, ctx:Logo3DParser.NeqContext):
        return self.visitChildren(ctx)



del Logo3DParser