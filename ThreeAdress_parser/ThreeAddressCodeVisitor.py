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


    # Visit a parse tree produced by ThreeAddressCodeParser#expression.
    def visitExpression(self, ctx:ThreeAddressCodeParser.ExpressionContext):
        return self.visitChildren(ctx)



del ThreeAddressCodeParser