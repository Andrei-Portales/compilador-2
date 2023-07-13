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


    # Enter a parse tree produced by YALPParser#feature.
    def enterFeature(self, ctx:YALPParser.FeatureContext):
        pass

    # Exit a parse tree produced by YALPParser#feature.
    def exitFeature(self, ctx:YALPParser.FeatureContext):
        pass


    # Enter a parse tree produced by YALPParser#formal.
    def enterFormal(self, ctx:YALPParser.FormalContext):
        pass

    # Exit a parse tree produced by YALPParser#formal.
    def exitFormal(self, ctx:YALPParser.FormalContext):
        pass


    # Enter a parse tree produced by YALPParser#expr.
    def enterExpr(self, ctx:YALPParser.ExprContext):
        pass

    # Exit a parse tree produced by YALPParser#expr.
    def exitExpr(self, ctx:YALPParser.ExprContext):
        pass



del YALPParser