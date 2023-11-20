# Generated from ThreeAdress_parser/ThreeAddressCode.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ThreeAddressCodeParser import ThreeAddressCodeParser
else:
    from ThreeAddressCodeParser import ThreeAddressCodeParser

# This class defines a complete listener for a parse tree produced by ThreeAddressCodeParser.
class ThreeAddressCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ThreeAddressCodeParser#program.
    def enterProgram(self, ctx:ThreeAddressCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#program.
    def exitProgram(self, ctx:ThreeAddressCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#classDeclaration.
    def enterClassDeclaration(self, ctx:ThreeAddressCodeParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#classDeclaration.
    def exitClassDeclaration(self, ctx:ThreeAddressCodeParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#globalVarDeclaration.
    def enterGlobalVarDeclaration(self, ctx:ThreeAddressCodeParser.GlobalVarDeclarationContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#globalVarDeclaration.
    def exitGlobalVarDeclaration(self, ctx:ThreeAddressCodeParser.GlobalVarDeclarationContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:ThreeAddressCodeParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:ThreeAddressCodeParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#returnInstr.
    def enterReturnInstr(self, ctx:ThreeAddressCodeParser.ReturnInstrContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#returnInstr.
    def exitReturnInstr(self, ctx:ThreeAddressCodeParser.ReturnInstrContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#equalInstr.
    def enterEqualInstr(self, ctx:ThreeAddressCodeParser.EqualInstrContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#equalInstr.
    def exitEqualInstr(self, ctx:ThreeAddressCodeParser.EqualInstrContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#negateInstr.
    def enterNegateInstr(self, ctx:ThreeAddressCodeParser.NegateInstrContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#negateInstr.
    def exitNegateInstr(self, ctx:ThreeAddressCodeParser.NegateInstrContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#ltInstr.
    def enterLtInstr(self, ctx:ThreeAddressCodeParser.LtInstrContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#ltInstr.
    def exitLtInstr(self, ctx:ThreeAddressCodeParser.LtInstrContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#ifInstr.
    def enterIfInstr(self, ctx:ThreeAddressCodeParser.IfInstrContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#ifInstr.
    def exitIfInstr(self, ctx:ThreeAddressCodeParser.IfInstrContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#gotoInstr.
    def enterGotoInstr(self, ctx:ThreeAddressCodeParser.GotoInstrContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#gotoInstr.
    def exitGotoInstr(self, ctx:ThreeAddressCodeParser.GotoInstrContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#pushParamInstr.
    def enterPushParamInstr(self, ctx:ThreeAddressCodeParser.PushParamInstrContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#pushParamInstr.
    def exitPushParamInstr(self, ctx:ThreeAddressCodeParser.PushParamInstrContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#popParamInstr.
    def enterPopParamInstr(self, ctx:ThreeAddressCodeParser.PopParamInstrContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#popParamInstr.
    def exitPopParamInstr(self, ctx:ThreeAddressCodeParser.PopParamInstrContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#fCallInstr.
    def enterFCallInstr(self, ctx:ThreeAddressCodeParser.FCallInstrContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#fCallInstr.
    def exitFCallInstr(self, ctx:ThreeAddressCodeParser.FCallInstrContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#labelInstr.
    def enterLabelInstr(self, ctx:ThreeAddressCodeParser.LabelInstrContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#labelInstr.
    def exitLabelInstr(self, ctx:ThreeAddressCodeParser.LabelInstrContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#fCallStatement.
    def enterFCallStatement(self, ctx:ThreeAddressCodeParser.FCallStatementContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#fCallStatement.
    def exitFCallStatement(self, ctx:ThreeAddressCodeParser.FCallStatementContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#tempExpr.
    def enterTempExpr(self, ctx:ThreeAddressCodeParser.TempExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#tempExpr.
    def exitTempExpr(self, ctx:ThreeAddressCodeParser.TempExprContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#stringExpr.
    def enterStringExpr(self, ctx:ThreeAddressCodeParser.StringExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#stringExpr.
    def exitStringExpr(self, ctx:ThreeAddressCodeParser.StringExprContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#negateExpr.
    def enterNegateExpr(self, ctx:ThreeAddressCodeParser.NegateExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#negateExpr.
    def exitNegateExpr(self, ctx:ThreeAddressCodeParser.NegateExprContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#comparateExpr.
    def enterComparateExpr(self, ctx:ThreeAddressCodeParser.ComparateExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#comparateExpr.
    def exitComparateExpr(self, ctx:ThreeAddressCodeParser.ComparateExprContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#selfExpr.
    def enterSelfExpr(self, ctx:ThreeAddressCodeParser.SelfExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#selfExpr.
    def exitSelfExpr(self, ctx:ThreeAddressCodeParser.SelfExprContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#numberExpr.
    def enterNumberExpr(self, ctx:ThreeAddressCodeParser.NumberExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#numberExpr.
    def exitNumberExpr(self, ctx:ThreeAddressCodeParser.NumberExprContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#operatorExpr.
    def enterOperatorExpr(self, ctx:ThreeAddressCodeParser.OperatorExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#operatorExpr.
    def exitOperatorExpr(self, ctx:ThreeAddressCodeParser.OperatorExprContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#labelExpr.
    def enterLabelExpr(self, ctx:ThreeAddressCodeParser.LabelExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#labelExpr.
    def exitLabelExpr(self, ctx:ThreeAddressCodeParser.LabelExprContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#graterThanExpr.
    def enterGraterThanExpr(self, ctx:ThreeAddressCodeParser.GraterThanExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#graterThanExpr.
    def exitGraterThanExpr(self, ctx:ThreeAddressCodeParser.GraterThanExprContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#graterEqualExpr.
    def enterGraterEqualExpr(self, ctx:ThreeAddressCodeParser.GraterEqualExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#graterEqualExpr.
    def exitGraterEqualExpr(self, ctx:ThreeAddressCodeParser.GraterEqualExprContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#boolExpr.
    def enterBoolExpr(self, ctx:ThreeAddressCodeParser.BoolExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#boolExpr.
    def exitBoolExpr(self, ctx:ThreeAddressCodeParser.BoolExprContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#idExpr.
    def enterIdExpr(self, ctx:ThreeAddressCodeParser.IdExprContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#idExpr.
    def exitIdExpr(self, ctx:ThreeAddressCodeParser.IdExprContext):
        pass



del ThreeAddressCodeParser