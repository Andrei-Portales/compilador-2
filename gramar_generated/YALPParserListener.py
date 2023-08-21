# Generated from grammar/YALPParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .YALPParser import YALPParser
else:
    from YALPParser import YALPParser

# This class defines a complete listener for a parse tree produced by YALPParser.
class YALPParserListener(ParseTreeListener):

    # Enter a parse tree produced by YALPParser#program.
    def enterProgram(self, ctx:YALPParser.ProgramContext):
        pass

    # Exit a parse tree produced by YALPParser#program.
    def exitProgram(self, ctx:YALPParser.ProgramContext):
        pass


    # Enter a parse tree produced by YALPParser#class.
    def enterClass(self, ctx:YALPParser.ClassContext):
        pass

    # Exit a parse tree produced by YALPParser#class.
    def exitClass(self, ctx:YALPParser.ClassContext):
        pass


    # Enter a parse tree produced by YALPParser#MethodFeature.
    def enterMethodFeature(self, ctx:YALPParser.MethodFeatureContext):
        pass

    # Exit a parse tree produced by YALPParser#MethodFeature.
    def exitMethodFeature(self, ctx:YALPParser.MethodFeatureContext):
        pass


    # Enter a parse tree produced by YALPParser#VariableFeature.
    def enterVariableFeature(self, ctx:YALPParser.VariableFeatureContext):
        pass

    # Exit a parse tree produced by YALPParser#VariableFeature.
    def exitVariableFeature(self, ctx:YALPParser.VariableFeatureContext):
        pass


    # Enter a parse tree produced by YALPParser#MethodParam.
    def enterMethodParam(self, ctx:YALPParser.MethodParamContext):
        pass

    # Exit a parse tree produced by YALPParser#MethodParam.
    def exitMethodParam(self, ctx:YALPParser.MethodParamContext):
        pass


    # Enter a parse tree produced by YALPParser#WhileExpr.
    def enterWhileExpr(self, ctx:YALPParser.WhileExprContext):
        pass

    # Exit a parse tree produced by YALPParser#WhileExpr.
    def exitWhileExpr(self, ctx:YALPParser.WhileExprContext):
        pass


    # Enter a parse tree produced by YALPParser#StringExpr.
    def enterStringExpr(self, ctx:YALPParser.StringExprContext):
        pass

    # Exit a parse tree produced by YALPParser#StringExpr.
    def exitStringExpr(self, ctx:YALPParser.StringExprContext):
        pass


    # Enter a parse tree produced by YALPParser#EqualExpr.
    def enterEqualExpr(self, ctx:YALPParser.EqualExprContext):
        pass

    # Exit a parse tree produced by YALPParser#EqualExpr.
    def exitEqualExpr(self, ctx:YALPParser.EqualExprContext):
        pass


    # Enter a parse tree produced by YALPParser#IfExpr.
    def enterIfExpr(self, ctx:YALPParser.IfExprContext):
        pass

    # Exit a parse tree produced by YALPParser#IfExpr.
    def exitIfExpr(self, ctx:YALPParser.IfExprContext):
        pass


    # Enter a parse tree produced by YALPParser#TrueExpr.
    def enterTrueExpr(self, ctx:YALPParser.TrueExprContext):
        pass

    # Exit a parse tree produced by YALPParser#TrueExpr.
    def exitTrueExpr(self, ctx:YALPParser.TrueExprContext):
        pass


    # Enter a parse tree produced by YALPParser#FalseExpr.
    def enterFalseExpr(self, ctx:YALPParser.FalseExprContext):
        pass

    # Exit a parse tree produced by YALPParser#FalseExpr.
    def exitFalseExpr(self, ctx:YALPParser.FalseExprContext):
        pass


    # Enter a parse tree produced by YALPParser#AssignExpr.
    def enterAssignExpr(self, ctx:YALPParser.AssignExprContext):
        pass

    # Exit a parse tree produced by YALPParser#AssignExpr.
    def exitAssignExpr(self, ctx:YALPParser.AssignExprContext):
        pass


    # Enter a parse tree produced by YALPParser#DivideExpr.
    def enterDivideExpr(self, ctx:YALPParser.DivideExprContext):
        pass

    # Exit a parse tree produced by YALPParser#DivideExpr.
    def exitDivideExpr(self, ctx:YALPParser.DivideExprContext):
        pass


    # Enter a parse tree produced by YALPParser#LessEqualExpr.
    def enterLessEqualExpr(self, ctx:YALPParser.LessEqualExprContext):
        pass

    # Exit a parse tree produced by YALPParser#LessEqualExpr.
    def exitLessEqualExpr(self, ctx:YALPParser.LessEqualExprContext):
        pass


    # Enter a parse tree produced by YALPParser#PlusExpr.
    def enterPlusExpr(self, ctx:YALPParser.PlusExprContext):
        pass

    # Exit a parse tree produced by YALPParser#PlusExpr.
    def exitPlusExpr(self, ctx:YALPParser.PlusExprContext):
        pass


    # Enter a parse tree produced by YALPParser#CallExpr.
    def enterCallExpr(self, ctx:YALPParser.CallExprContext):
        pass

    # Exit a parse tree produced by YALPParser#CallExpr.
    def exitCallExpr(self, ctx:YALPParser.CallExprContext):
        pass


    # Enter a parse tree produced by YALPParser#NotExpr.
    def enterNotExpr(self, ctx:YALPParser.NotExprContext):
        pass

    # Exit a parse tree produced by YALPParser#NotExpr.
    def exitNotExpr(self, ctx:YALPParser.NotExprContext):
        pass


    # Enter a parse tree produced by YALPParser#LessThanExpr.
    def enterLessThanExpr(self, ctx:YALPParser.LessThanExprContext):
        pass

    # Exit a parse tree produced by YALPParser#LessThanExpr.
    def exitLessThanExpr(self, ctx:YALPParser.LessThanExprContext):
        pass


    # Enter a parse tree produced by YALPParser#TimesExpr.
    def enterTimesExpr(self, ctx:YALPParser.TimesExprContext):
        pass

    # Exit a parse tree produced by YALPParser#TimesExpr.
    def exitTimesExpr(self, ctx:YALPParser.TimesExprContext):
        pass


    # Enter a parse tree produced by YALPParser#MinusExpr.
    def enterMinusExpr(self, ctx:YALPParser.MinusExprContext):
        pass

    # Exit a parse tree produced by YALPParser#MinusExpr.
    def exitMinusExpr(self, ctx:YALPParser.MinusExprContext):
        pass


    # Enter a parse tree produced by YALPParser#IdExpr.
    def enterIdExpr(self, ctx:YALPParser.IdExprContext):
        pass

    # Exit a parse tree produced by YALPParser#IdExpr.
    def exitIdExpr(self, ctx:YALPParser.IdExprContext):
        pass


    # Enter a parse tree produced by YALPParser#LetExpr.
    def enterLetExpr(self, ctx:YALPParser.LetExprContext):
        pass

    # Exit a parse tree produced by YALPParser#LetExpr.
    def exitLetExpr(self, ctx:YALPParser.LetExprContext):
        pass


    # Enter a parse tree produced by YALPParser#DotExpr.
    def enterDotExpr(self, ctx:YALPParser.DotExprContext):
        pass

    # Exit a parse tree produced by YALPParser#DotExpr.
    def exitDotExpr(self, ctx:YALPParser.DotExprContext):
        pass


    # Enter a parse tree produced by YALPParser#TypeExpr.
    def enterTypeExpr(self, ctx:YALPParser.TypeExprContext):
        pass

    # Exit a parse tree produced by YALPParser#TypeExpr.
    def exitTypeExpr(self, ctx:YALPParser.TypeExprContext):
        pass


    # Enter a parse tree produced by YALPParser#BlockExpr.
    def enterBlockExpr(self, ctx:YALPParser.BlockExprContext):
        pass

    # Exit a parse tree produced by YALPParser#BlockExpr.
    def exitBlockExpr(self, ctx:YALPParser.BlockExprContext):
        pass


    # Enter a parse tree produced by YALPParser#IsvoidExpr.
    def enterIsvoidExpr(self, ctx:YALPParser.IsvoidExprContext):
        pass

    # Exit a parse tree produced by YALPParser#IsvoidExpr.
    def exitIsvoidExpr(self, ctx:YALPParser.IsvoidExprContext):
        pass


    # Enter a parse tree produced by YALPParser#NegateExpr.
    def enterNegateExpr(self, ctx:YALPParser.NegateExprContext):
        pass

    # Exit a parse tree produced by YALPParser#NegateExpr.
    def exitNegateExpr(self, ctx:YALPParser.NegateExprContext):
        pass


    # Enter a parse tree produced by YALPParser#NewExpr.
    def enterNewExpr(self, ctx:YALPParser.NewExprContext):
        pass

    # Exit a parse tree produced by YALPParser#NewExpr.
    def exitNewExpr(self, ctx:YALPParser.NewExprContext):
        pass


    # Enter a parse tree produced by YALPParser#IntExpr.
    def enterIntExpr(self, ctx:YALPParser.IntExprContext):
        pass

    # Exit a parse tree produced by YALPParser#IntExpr.
    def exitIntExpr(self, ctx:YALPParser.IntExprContext):
        pass


    # Enter a parse tree produced by YALPParser#ModExpr.
    def enterModExpr(self, ctx:YALPParser.ModExprContext):
        pass

    # Exit a parse tree produced by YALPParser#ModExpr.
    def exitModExpr(self, ctx:YALPParser.ModExprContext):
        pass


    # Enter a parse tree produced by YALPParser#ParenExpr.
    def enterParenExpr(self, ctx:YALPParser.ParenExprContext):
        pass

    # Exit a parse tree produced by YALPParser#ParenExpr.
    def exitParenExpr(self, ctx:YALPParser.ParenExprContext):
        pass



del YALPParser