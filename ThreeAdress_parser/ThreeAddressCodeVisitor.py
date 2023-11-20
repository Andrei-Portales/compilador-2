# Generated from ThreeAdress_parser/ThreeAddressCode.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ThreeAddressCodeParser import ThreeAddressCodeParser
else:
    from ThreeAddressCodeParser import ThreeAddressCodeParser

# This class defines a complete generic visitor for a parse tree produced by ThreeAddressCodeParser.

class ThreeAddressCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ThreeAddressCodeParser#program.
    def visitProgram(self, ctx:ThreeAddressCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#classDeclaration.
    def visitClassDeclaration(self, ctx:ThreeAddressCodeParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#globalVarDeclaration.
    def visitGlobalVarDeclaration(self, ctx:ThreeAddressCodeParser.GlobalVarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:ThreeAddressCodeParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#returnInstr.
    def visitReturnInstr(self, ctx:ThreeAddressCodeParser.ReturnInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#assignInstr.
    def visitAssignInstr(self, ctx:ThreeAddressCodeParser.AssignInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#equalInstr.
    def visitEqualInstr(self, ctx:ThreeAddressCodeParser.EqualInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#negateInstr.
    def visitNegateInstr(self, ctx:ThreeAddressCodeParser.NegateInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#ltInstr.
    def visitLtInstr(self, ctx:ThreeAddressCodeParser.LtInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#ifInstr.
    def visitIfInstr(self, ctx:ThreeAddressCodeParser.IfInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#gotoInstr.
    def visitGotoInstr(self, ctx:ThreeAddressCodeParser.GotoInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#pushParamInstr.
    def visitPushParamInstr(self, ctx:ThreeAddressCodeParser.PushParamInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#popParamInstr.
    def visitPopParamInstr(self, ctx:ThreeAddressCodeParser.PopParamInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#fCallInstr.
    def visitFCallInstr(self, ctx:ThreeAddressCodeParser.FCallInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#labelInstr.
    def visitLabelInstr(self, ctx:ThreeAddressCodeParser.LabelInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#fCallStatement.
    def visitFCallStatement(self, ctx:ThreeAddressCodeParser.FCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#selfExpr.
    def visitSelfExpr(self, ctx:ThreeAddressCodeParser.SelfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#idExpr.
    def visitIdExpr(self, ctx:ThreeAddressCodeParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#boolExpr.
    def visitBoolExpr(self, ctx:ThreeAddressCodeParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#numberExpr.
    def visitNumberExpr(self, ctx:ThreeAddressCodeParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#stringExpr.
    def visitStringExpr(self, ctx:ThreeAddressCodeParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#labelExpr.
    def visitLabelExpr(self, ctx:ThreeAddressCodeParser.LabelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#operatorExpr.
    def visitOperatorExpr(self, ctx:ThreeAddressCodeParser.OperatorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#negateExpr.
    def visitNegateExpr(self, ctx:ThreeAddressCodeParser.NegateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#graterThanExpr.
    def visitGraterThanExpr(self, ctx:ThreeAddressCodeParser.GraterThanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#graterEqualExpr.
    def visitGraterEqualExpr(self, ctx:ThreeAddressCodeParser.GraterEqualExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#comparateExpr.
    def visitComparateExpr(self, ctx:ThreeAddressCodeParser.ComparateExprContext):
        return self.visitChildren(ctx)



del ThreeAddressCodeParser