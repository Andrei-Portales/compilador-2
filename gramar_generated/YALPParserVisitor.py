# Generated from grammar/YALPParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .YALPParser import YALPParser
else:
    from YALPParser import YALPParser

# This class defines a complete generic visitor for a parse tree produced by YALPParser.

class YALPParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YALPParser#program.
    def visitProgram(self, ctx:YALPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#class.
    def visitClass(self, ctx:YALPParser.ClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#MethodFeature.
    def visitMethodFeature(self, ctx:YALPParser.MethodFeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#VariableFeature.
    def visitVariableFeature(self, ctx:YALPParser.VariableFeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#formal.
    def visitFormal(self, ctx:YALPParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#WhileExpr.
    def visitWhileExpr(self, ctx:YALPParser.WhileExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#StringExpr.
    def visitStringExpr(self, ctx:YALPParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#EqualExpr.
    def visitEqualExpr(self, ctx:YALPParser.EqualExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#IfExpr.
    def visitIfExpr(self, ctx:YALPParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#TrueExpr.
    def visitTrueExpr(self, ctx:YALPParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#FalseExpr.
    def visitFalseExpr(self, ctx:YALPParser.FalseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#AssignExpr.
    def visitAssignExpr(self, ctx:YALPParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#DivideExpr.
    def visitDivideExpr(self, ctx:YALPParser.DivideExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#LessEqualExpr.
    def visitLessEqualExpr(self, ctx:YALPParser.LessEqualExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#PlusExpr.
    def visitPlusExpr(self, ctx:YALPParser.PlusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#CallExpr.
    def visitCallExpr(self, ctx:YALPParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#NotExpr.
    def visitNotExpr(self, ctx:YALPParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#LessThanExpr.
    def visitLessThanExpr(self, ctx:YALPParser.LessThanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#TimesExpr.
    def visitTimesExpr(self, ctx:YALPParser.TimesExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#MinusExpr.
    def visitMinusExpr(self, ctx:YALPParser.MinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#IdExpr.
    def visitIdExpr(self, ctx:YALPParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#LetExpr.
    def visitLetExpr(self, ctx:YALPParser.LetExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#DotExpr.
    def visitDotExpr(self, ctx:YALPParser.DotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#TypeExpr.
    def visitTypeExpr(self, ctx:YALPParser.TypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#BlockExpr.
    def visitBlockExpr(self, ctx:YALPParser.BlockExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#IsvoidExpr.
    def visitIsvoidExpr(self, ctx:YALPParser.IsvoidExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#NegateExpr.
    def visitNegateExpr(self, ctx:YALPParser.NegateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#NewExpr.
    def visitNewExpr(self, ctx:YALPParser.NewExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#IntExpr.
    def visitIntExpr(self, ctx:YALPParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#ModExpr.
    def visitModExpr(self, ctx:YALPParser.ModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YALPParser#ParenExpr.
    def visitParenExpr(self, ctx:YALPParser.ParenExprContext):
        return self.visitChildren(ctx)



del YALPParser