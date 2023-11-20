# Generated from ThreeAdress_parser/ThreeAddressCode.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,122,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,1,1,5,1,25,8,1,10,
        1,12,1,28,9,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,41,
        8,3,10,3,12,3,44,9,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,90,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,100,8,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,3,6,120,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,2,0,2,2,23,23,137,0,
        15,1,0,0,0,2,19,1,0,0,0,4,29,1,0,0,0,6,34,1,0,0,0,8,89,1,0,0,0,10,
        99,1,0,0,0,12,119,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,
        0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,20,5,1,0,0,20,21,
        5,23,0,0,21,26,5,21,0,0,22,25,3,4,2,0,23,25,3,6,3,0,24,22,1,0,0,
        0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,3,1,
        0,0,0,28,26,1,0,0,0,29,30,5,23,0,0,30,31,5,4,0,0,31,32,3,12,6,0,
        32,33,5,20,0,0,33,5,1,0,0,0,34,35,5,23,0,0,35,36,5,21,0,0,36,37,
        5,12,0,0,37,38,5,2,0,0,38,42,5,20,0,0,39,41,3,8,4,0,40,39,1,0,0,
        0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,42,
        1,0,0,0,45,46,5,13,0,0,46,47,5,20,0,0,47,7,1,0,0,0,48,49,5,11,0,
        0,49,50,3,12,6,0,50,51,5,20,0,0,51,90,1,0,0,0,52,53,5,23,0,0,53,
        54,5,4,0,0,54,55,3,12,6,0,55,56,5,20,0,0,56,90,1,0,0,0,57,58,5,23,
        0,0,58,59,5,5,0,0,59,60,3,12,6,0,60,61,5,20,0,0,61,90,1,0,0,0,62,
        63,5,23,0,0,63,64,5,6,0,0,64,65,3,12,6,0,65,66,5,20,0,0,66,90,1,
        0,0,0,67,68,5,23,0,0,68,69,5,7,0,0,69,70,3,12,6,0,70,71,5,20,0,0,
        71,90,1,0,0,0,72,73,5,14,0,0,73,74,5,23,0,0,74,75,5,15,0,0,75,76,
        5,22,0,0,76,90,5,20,0,0,77,78,5,15,0,0,78,79,5,22,0,0,79,90,5,20,
        0,0,80,81,5,16,0,0,81,82,5,23,0,0,82,90,5,20,0,0,83,84,5,17,0,0,
        84,85,5,2,0,0,85,90,5,20,0,0,86,90,3,10,5,0,87,88,5,22,0,0,88,90,
        5,21,0,0,89,48,1,0,0,0,89,52,1,0,0,0,89,57,1,0,0,0,89,62,1,0,0,0,
        89,67,1,0,0,0,89,72,1,0,0,0,89,77,1,0,0,0,89,80,1,0,0,0,89,83,1,
        0,0,0,89,86,1,0,0,0,89,87,1,0,0,0,90,9,1,0,0,0,91,92,5,18,0,0,92,
        93,5,23,0,0,93,94,5,10,0,0,94,95,5,23,0,0,95,100,5,20,0,0,96,97,
        5,18,0,0,97,98,5,23,0,0,98,100,5,20,0,0,99,91,1,0,0,0,99,96,1,0,
        0,0,100,11,1,0,0,0,101,120,5,23,0,0,102,120,5,2,0,0,103,120,5,3,
        0,0,104,120,5,22,0,0,105,106,7,0,0,0,106,107,5,19,0,0,107,120,7,
        0,0,0,108,109,5,6,0,0,109,120,7,0,0,0,110,111,7,0,0,0,111,112,5,
        7,0,0,112,120,7,0,0,0,113,114,7,0,0,0,114,115,5,8,0,0,115,120,7,
        0,0,0,116,117,7,0,0,0,117,118,5,9,0,0,118,120,7,0,0,0,119,101,1,
        0,0,0,119,102,1,0,0,0,119,103,1,0,0,0,119,104,1,0,0,0,119,105,1,
        0,0,0,119,108,1,0,0,0,119,110,1,0,0,0,119,113,1,0,0,0,119,116,1,
        0,0,0,120,13,1,0,0,0,7,17,24,26,42,89,99,119
    ]

class ThreeAddressCodeParser ( Parser ):

    grammarFileName = "ThreeAddressCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "<INVALID>", "<INVALID>", "'<-'", 
                     "'='", "'~'", "'<'", "'<='", "'=='", "'.'", "'Return'", 
                     "'BeginFunc'", "'EndFunc'", "'Ifz'", "'Goto'", "'PushParam'", 
                     "'PopParams'", "'FCall'", "<INVALID>", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "NUMBER", "STRING", "ASSIGN", 
                      "EQUAL", "NEGATE", "LT", "LT_EQUAL", "COMPARE", "DOT", 
                      "RETURN", "BEGIN_FUNC", "END_FUNC", "IFZ", "GOTO", 
                      "PUSH_PARAM", "POP_PARAMS", "FCALL", "OP", "SEMI", 
                      "COLON", "LABEL", "IDENTIFIER", "WHITESPACE" ]

    RULE_program = 0
    RULE_classDeclaration = 1
    RULE_globalVarDeclaration = 2
    RULE_methodDeclaration = 3
    RULE_instruction = 4
    RULE_fCallStatement = 5
    RULE_expression = 6

    ruleNames =  [ "program", "classDeclaration", "globalVarDeclaration", 
                   "methodDeclaration", "instruction", "fCallStatement", 
                   "expression" ]

    EOF = Token.EOF
    CLASS=1
    NUMBER=2
    STRING=3
    ASSIGN=4
    EQUAL=5
    NEGATE=6
    LT=7
    LT_EQUAL=8
    COMPARE=9
    DOT=10
    RETURN=11
    BEGIN_FUNC=12
    END_FUNC=13
    IFZ=14
    GOTO=15
    PUSH_PARAM=16
    POP_PARAMS=17
    FCALL=18
    OP=19
    SEMI=20
    COLON=21
    LABEL=22
    IDENTIFIER=23
    WHITESPACE=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.ClassDeclarationContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.ClassDeclarationContext,i)


        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ThreeAddressCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.classDeclaration()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(ThreeAddressCodeParser.CLASS, 0)

        def IDENTIFIER(self):
            return self.getToken(ThreeAddressCodeParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(ThreeAddressCodeParser.COLON, 0)

        def globalVarDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.GlobalVarDeclarationContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.GlobalVarDeclarationContext,i)


        def methodDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.MethodDeclarationContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.MethodDeclarationContext,i)


        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = ThreeAddressCodeParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(ThreeAddressCodeParser.CLASS)
            self.state = 20
            self.match(ThreeAddressCodeParser.IDENTIFIER)
            self.state = 21
            self.match(ThreeAddressCodeParser.COLON)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 24
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 22
                    self.globalVarDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 23
                    self.methodDeclaration()
                    pass


                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalVarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ThreeAddressCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ThreeAddressCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)

        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_globalVarDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalVarDeclaration" ):
                listener.enterGlobalVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalVarDeclaration" ):
                listener.exitGlobalVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalVarDeclaration" ):
                return visitor.visitGlobalVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def globalVarDeclaration(self):

        localctx = ThreeAddressCodeParser.GlobalVarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_globalVarDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(ThreeAddressCodeParser.IDENTIFIER)
            self.state = 30
            self.match(ThreeAddressCodeParser.ASSIGN)
            self.state = 31
            self.expression()
            self.state = 32
            self.match(ThreeAddressCodeParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ThreeAddressCodeParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(ThreeAddressCodeParser.COLON, 0)

        def BEGIN_FUNC(self):
            return self.getToken(ThreeAddressCodeParser.BEGIN_FUNC, 0)

        def NUMBER(self):
            return self.getToken(ThreeAddressCodeParser.NUMBER, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.SEMI)
            else:
                return self.getToken(ThreeAddressCodeParser.SEMI, i)

        def END_FUNC(self):
            return self.getToken(ThreeAddressCodeParser.END_FUNC, 0)

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.InstructionContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.InstructionContext,i)


        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = ThreeAddressCodeParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ThreeAddressCodeParser.IDENTIFIER)
            self.state = 35
            self.match(ThreeAddressCodeParser.COLON)
            self.state = 36
            self.match(ThreeAddressCodeParser.BEGIN_FUNC)
            self.state = 37
            self.match(ThreeAddressCodeParser.NUMBER)
            self.state = 38
            self.match(ThreeAddressCodeParser.SEMI)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13092864) != 0):
                self.state = 39
                self.instruction()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(ThreeAddressCodeParser.END_FUNC)
            self.state = 46
            self.match(ThreeAddressCodeParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_instruction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EqualInstrContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ThreeAddressCodeParser.IDENTIFIER, 0)
        def EQUAL(self):
            return self.getToken(ThreeAddressCodeParser.EQUAL, 0)
        def expression(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualInstr" ):
                listener.enterEqualInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualInstr" ):
                listener.exitEqualInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualInstr" ):
                return visitor.visitEqualInstr(self)
            else:
                return visitor.visitChildren(self)


    class AssignInstrContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ThreeAddressCodeParser.IDENTIFIER, 0)
        def ASSIGN(self):
            return self.getToken(ThreeAddressCodeParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignInstr" ):
                listener.enterAssignInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignInstr" ):
                listener.exitAssignInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignInstr" ):
                return visitor.visitAssignInstr(self)
            else:
                return visitor.visitChildren(self)


    class PopParamInstrContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POP_PARAMS(self):
            return self.getToken(ThreeAddressCodeParser.POP_PARAMS, 0)
        def NUMBER(self):
            return self.getToken(ThreeAddressCodeParser.NUMBER, 0)
        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPopParamInstr" ):
                listener.enterPopParamInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPopParamInstr" ):
                listener.exitPopParamInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPopParamInstr" ):
                return visitor.visitPopParamInstr(self)
            else:
                return visitor.visitChildren(self)


    class PushParamInstrContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUSH_PARAM(self):
            return self.getToken(ThreeAddressCodeParser.PUSH_PARAM, 0)
        def IDENTIFIER(self):
            return self.getToken(ThreeAddressCodeParser.IDENTIFIER, 0)
        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPushParamInstr" ):
                listener.enterPushParamInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPushParamInstr" ):
                listener.exitPushParamInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPushParamInstr" ):
                return visitor.visitPushParamInstr(self)
            else:
                return visitor.visitChildren(self)


    class NegateInstrContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ThreeAddressCodeParser.IDENTIFIER, 0)
        def NEGATE(self):
            return self.getToken(ThreeAddressCodeParser.NEGATE, 0)
        def expression(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegateInstr" ):
                listener.enterNegateInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegateInstr" ):
                listener.exitNegateInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegateInstr" ):
                return visitor.visitNegateInstr(self)
            else:
                return visitor.visitChildren(self)


    class GotoInstrContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GOTO(self):
            return self.getToken(ThreeAddressCodeParser.GOTO, 0)
        def LABEL(self):
            return self.getToken(ThreeAddressCodeParser.LABEL, 0)
        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoInstr" ):
                listener.enterGotoInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoInstr" ):
                listener.exitGotoInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoInstr" ):
                return visitor.visitGotoInstr(self)
            else:
                return visitor.visitChildren(self)


    class IfInstrContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IFZ(self):
            return self.getToken(ThreeAddressCodeParser.IFZ, 0)
        def IDENTIFIER(self):
            return self.getToken(ThreeAddressCodeParser.IDENTIFIER, 0)
        def GOTO(self):
            return self.getToken(ThreeAddressCodeParser.GOTO, 0)
        def LABEL(self):
            return self.getToken(ThreeAddressCodeParser.LABEL, 0)
        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfInstr" ):
                listener.enterIfInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfInstr" ):
                listener.exitIfInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfInstr" ):
                return visitor.visitIfInstr(self)
            else:
                return visitor.visitChildren(self)


    class FCallInstrContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fCallStatement(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.FCallStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFCallInstr" ):
                listener.enterFCallInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFCallInstr" ):
                listener.exitFCallInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFCallInstr" ):
                return visitor.visitFCallInstr(self)
            else:
                return visitor.visitChildren(self)


    class ReturnInstrContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(ThreeAddressCodeParser.RETURN, 0)
        def expression(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnInstr" ):
                listener.enterReturnInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnInstr" ):
                listener.exitReturnInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnInstr" ):
                return visitor.visitReturnInstr(self)
            else:
                return visitor.visitChildren(self)


    class LabelInstrContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LABEL(self):
            return self.getToken(ThreeAddressCodeParser.LABEL, 0)
        def COLON(self):
            return self.getToken(ThreeAddressCodeParser.COLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelInstr" ):
                listener.enterLabelInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelInstr" ):
                listener.exitLabelInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelInstr" ):
                return visitor.visitLabelInstr(self)
            else:
                return visitor.visitChildren(self)


    class LtInstrContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ThreeAddressCodeParser.IDENTIFIER, 0)
        def LT(self):
            return self.getToken(ThreeAddressCodeParser.LT, 0)
        def expression(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLtInstr" ):
                listener.enterLtInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLtInstr" ):
                listener.exitLtInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLtInstr" ):
                return visitor.visitLtInstr(self)
            else:
                return visitor.visitChildren(self)



    def instruction(self):

        localctx = ThreeAddressCodeParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instruction)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ThreeAddressCodeParser.ReturnInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(ThreeAddressCodeParser.RETURN)
                self.state = 49
                self.expression()
                self.state = 50
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 2:
                localctx = ThreeAddressCodeParser.AssignInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 53
                self.match(ThreeAddressCodeParser.ASSIGN)
                self.state = 54
                self.expression()
                self.state = 55
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 3:
                localctx = ThreeAddressCodeParser.EqualInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 58
                self.match(ThreeAddressCodeParser.EQUAL)
                self.state = 59
                self.expression()
                self.state = 60
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 4:
                localctx = ThreeAddressCodeParser.NegateInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 63
                self.match(ThreeAddressCodeParser.NEGATE)
                self.state = 64
                self.expression()
                self.state = 65
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 5:
                localctx = ThreeAddressCodeParser.LtInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 68
                self.match(ThreeAddressCodeParser.LT)
                self.state = 69
                self.expression()
                self.state = 70
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 6:
                localctx = ThreeAddressCodeParser.IfInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 72
                self.match(ThreeAddressCodeParser.IFZ)
                self.state = 73
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 74
                self.match(ThreeAddressCodeParser.GOTO)
                self.state = 75
                self.match(ThreeAddressCodeParser.LABEL)
                self.state = 76
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 7:
                localctx = ThreeAddressCodeParser.GotoInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.match(ThreeAddressCodeParser.GOTO)
                self.state = 78
                self.match(ThreeAddressCodeParser.LABEL)
                self.state = 79
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 8:
                localctx = ThreeAddressCodeParser.PushParamInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 80
                self.match(ThreeAddressCodeParser.PUSH_PARAM)
                self.state = 81
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 82
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 9:
                localctx = ThreeAddressCodeParser.PopParamInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 83
                self.match(ThreeAddressCodeParser.POP_PARAMS)
                self.state = 84
                self.match(ThreeAddressCodeParser.NUMBER)
                self.state = 85
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 10:
                localctx = ThreeAddressCodeParser.FCallInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 86
                self.fCallStatement()
                pass

            elif la_ == 11:
                localctx = ThreeAddressCodeParser.LabelInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 87
                self.match(ThreeAddressCodeParser.LABEL)
                self.state = 88
                self.match(ThreeAddressCodeParser.COLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FCallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FCALL(self):
            return self.getToken(ThreeAddressCodeParser.FCALL, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.IDENTIFIER)
            else:
                return self.getToken(ThreeAddressCodeParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(ThreeAddressCodeParser.DOT, 0)

        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)

        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_fCallStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFCallStatement" ):
                listener.enterFCallStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFCallStatement" ):
                listener.exitFCallStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFCallStatement" ):
                return visitor.visitFCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def fCallStatement(self):

        localctx = ThreeAddressCodeParser.FCallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fCallStatement)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(ThreeAddressCodeParser.FCALL)
                self.state = 92
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 93
                self.match(ThreeAddressCodeParser.DOT)
                self.state = 94
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 95
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(ThreeAddressCodeParser.FCALL)
                self.state = 97
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 98
                self.match(ThreeAddressCodeParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.IDENTIFIER)
            else:
                return self.getToken(ThreeAddressCodeParser.IDENTIFIER, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.NUMBER)
            else:
                return self.getToken(ThreeAddressCodeParser.NUMBER, i)

        def STRING(self):
            return self.getToken(ThreeAddressCodeParser.STRING, 0)

        def LABEL(self):
            return self.getToken(ThreeAddressCodeParser.LABEL, 0)

        def OP(self):
            return self.getToken(ThreeAddressCodeParser.OP, 0)

        def NEGATE(self):
            return self.getToken(ThreeAddressCodeParser.NEGATE, 0)

        def LT(self):
            return self.getToken(ThreeAddressCodeParser.LT, 0)

        def LT_EQUAL(self):
            return self.getToken(ThreeAddressCodeParser.LT_EQUAL, 0)

        def COMPARE(self):
            return self.getToken(ThreeAddressCodeParser.COMPARE, 0)

        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ThreeAddressCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(ThreeAddressCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.match(ThreeAddressCodeParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.match(ThreeAddressCodeParser.LABEL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 105
                _la = self._input.LA(1)
                if not(_la==2 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self.match(ThreeAddressCodeParser.OP)
                self.state = 107
                _la = self._input.LA(1)
                if not(_la==2 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.match(ThreeAddressCodeParser.NEGATE)
                self.state = 109
                _la = self._input.LA(1)
                if not(_la==2 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 110
                _la = self._input.LA(1)
                if not(_la==2 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 111
                self.match(ThreeAddressCodeParser.LT)
                self.state = 112
                _la = self._input.LA(1)
                if not(_la==2 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 113
                _la = self._input.LA(1)
                if not(_la==2 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self.match(ThreeAddressCodeParser.LT_EQUAL)
                self.state = 115
                _la = self._input.LA(1)
                if not(_la==2 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 116
                _la = self._input.LA(1)
                if not(_la==2 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 117
                self.match(ThreeAddressCodeParser.COMPARE)
                self.state = 118
                _la = self._input.LA(1)
                if not(_la==2 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





