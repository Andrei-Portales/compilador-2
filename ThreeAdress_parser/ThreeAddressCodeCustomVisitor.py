# Generated from ThreeAdress_parser/ThreeAddressCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ThreeAddressCodeParser import ThreeAddressCodeParser
else:
    from ThreeAddressCodeParser import ThreeAddressCodeParser

# This class defines a complete generic visitor for a parse tree produced by ThreeAddressCodeParser.

# this is the class that will be used to generate the tree
# and then the tree will be used to generate the MIPS code

class ThreeAddressCodeCustomVisitor(ParseTreeVisitor):

    def __init__(self):
        self.registers = {'$t0': None, '$t1': None, '$t2': None, '$t3': None, '$t4': None, '$t5': None, '$t6': None, '$t7': None, '$t8': None, '$t9': None}
        self.memory_addresses = {}
        self.variables = {}
        self.functions = {}
        self.classes = []
        self.code = []
    
    def print_code(self):
        for line in self.code:
            print(line)

    def get_register(self):
        # if there is a register available
        for register in self.registers:
            if self.registers[register] == None:
                return register
            
        # if there is no register available
        # we need to save one of the registers in memory
        # we will use the first register that is not being used
        # to save a variable
        for register in self.registers:
            if self.registers[register] != None:
                # we need to save the variable in memory
                # and then we can use the register
                variable = self.registers[register]
                self.save_variable_in_memory(variable)
                self.registers[register] = None
                return register
        return None
    
    def save_variable_in_memory(self, variable):
        # we need to save the variable in memory
        # we will use the first memory address that is not being used
        for memory_address in self.memory_addresses:
            if self.memory_addresses[memory_address] == None:
                self.memory_addresses[memory_address] = variable
                return memory_address
        return None
    
    def get_memory_address(self, variable):
        # we need to save the variable in memory
        # we will use the first memory address that is not being used
        for memory_address in self.memory_addresses:
            if self.memory_addresses[memory_address] == variable:
                return memory_address
        return None
    
    def get_variable(self, memory_address):
        return self.memory_addresses[memory_address]
    
    def get_function(self, function_name):
        return self.functions[function_name]
    
    def get_variable_value(self, variable):
        if variable in self.variables:
            return self.variables[variable]
        return None
    
    def set_variable_value(self, variable, value):
        self.variables[variable] = value

    # Visit a parse tree produced by ThreeAddressCodeParser#program.
    def visitProgram(self, ctx:ThreeAddressCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#classDeclaration.
    def visitClassDeclaration(self, ctx:ThreeAddressCodeParser.ClassDeclarationContext):
        class_name = ctx.IDENTIFIER().getText()
        print(class_name)
        self.classes.append(class_name)
        return self.visitChildren(ctx)

        # Visit a parse tree produced by ThreeAddressCodeParser#globalVarDeclaration.
    def visitGlobalVarDeclaration(self, ctx:ThreeAddressCodeParser.GlobalVarDeclarationContext):
        variable = ctx.IDENTIFIER().getText()
        print(variable)
        value = ctx.IDENTIFIER().getText()
        print(variable, value)
        self.set_variable_value(variable, value)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:ThreeAddressCodeParser.MethodDeclarationContext):
        function_name = ctx.IDENTIFIER(0).getText()
        print(function_name)
        parameters = []
        for i in range(1, len(ctx.IDENTIFIER())):
            parameters.append(ctx.IDENTIFIER(i).getText())
        self.functions[function_name] = {'parameters': parameters}

        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#instruction.
    def visitInstruction(self, ctx:ThreeAddressCodeParser.InstructionContext):
        if ctx.ASSIGN():
            dest =ctx.IDENTIFIER(0).getText()
            src = ctx.IDENTIFIER(1).getText()
            reg = self.get_register()

            self.code.append(f"move {reg}, {src}")
            self.code.append(f"move {dest}, {reg}")
        elif ctx.RETURN():
            value = ctx.IDENTIFIER(0).getText()
            self.code.append(f"move $v0, {value}")
            self.code.append("jr $ra")
        elif ctx.IFZ():
            value = ctx.IDENTIFIER(0).getText()
            label = ctx.IDENTIFIER(1).getText()
            self.code.append(f"beqz {value}, {label}")
        elif ctx.GOTO():
            label = ctx.IDENTIFIER(0).getText()
            self.code.append(f"j {label}")
        elif ctx.NEGATE():
            dest = ctx.IDENTIFIER(0).getText()
            src = ctx.IDENTIFIER(1).getText()
            self.code.append(f"neg {dest}, {src}")

        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#fCallStatement.
    def visitFCallStatement(self, ctx:ThreeAddressCodeParser.FCallStatementContext):
        function_name = ctx.IDENTIFIER(0).getText()
        function = self.get_function(function_name)
        parameters = function['parameters']
        for i in range(len(parameters)):
            parameter = parameters[i]
            value = ctx.IDENTIFIER(i+1).getText()
            self.code.append(f"move {parameter}, {value}")
        self.code.append(f"jal {function_name}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#expression.
    def visitExpression(self, ctx:ThreeAddressCodeParser.ExpressionContext):
        if ctx.OP().getText() == "+":
            dest = ctx.IDENTIFIER(0).getText()
            src1 = ctx.IDENTIFIER(1).getText()
            src2 = ctx.IDENTIFIER(2).getText()
            self.code.append(f"add {dest}, {src1}, {src2}")
        elif ctx.OP().getText() == "-":
            dest = ctx.IDENTIFIER(0).getText()
            src1 = ctx.IDENTIFIER(1).getText()
            src2 = ctx.IDENTIFIER(2).getText()
            self.code.append(f"sub {dest}, {src1}, {src2}")
        elif ctx.OP().getText() == "*":
            dest = ctx.IDENTIFIER(0).getText()
            src1 = ctx.IDENTIFIER(1).getText()
            src2 = ctx.IDENTIFIER(2).getText()
            self.code.append(f"mul {dest}, {src1}, {src2}")
        elif ctx.OP().getText() == "/":
            dest = ctx.IDENTIFIER(0).getText()
            src1 = ctx.IDENTIFIER(1).getText()
            src2 = ctx.IDENTIFIER(2).getText()
            self.code.append(f"div {dest}, {src1}, {src2}")
        return self.visitChildren(ctx)



del ThreeAddressCodeParser