# Generated from ThreeAdress_parser/ThreeAddressCode.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by ThreeAddressCodeParser#instruction.
    def visitInstruction(self, ctx:ThreeAddressCodeParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#fCallStatement.
    def visitFCallStatement(self, ctx:ThreeAddressCodeParser.FCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#expression.
    def visitExpression(self, ctx:ThreeAddressCodeParser.ExpressionContext):
        return self.visitChildren(ctx)



del ThreeAddressCodeParser