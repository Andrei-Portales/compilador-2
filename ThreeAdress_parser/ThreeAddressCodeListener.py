# Generated from ThreeAdress_parser/ThreeAddressCode.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by ThreeAddressCodeParser#instruction.
    def enterInstruction(self, ctx:ThreeAddressCodeParser.InstructionContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#instruction.
    def exitInstruction(self, ctx:ThreeAddressCodeParser.InstructionContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#fCallStatement.
    def enterFCallStatement(self, ctx:ThreeAddressCodeParser.FCallStatementContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#fCallStatement.
    def exitFCallStatement(self, ctx:ThreeAddressCodeParser.FCallStatementContext):
        pass


    # Enter a parse tree produced by ThreeAddressCodeParser#expression.
    def enterExpression(self, ctx:ThreeAddressCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ThreeAddressCodeParser#expression.
    def exitExpression(self, ctx:ThreeAddressCodeParser.ExpressionContext):
        pass



del ThreeAddressCodeParser