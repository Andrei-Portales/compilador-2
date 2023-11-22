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
        4,1,27,130,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,1,1,5,1,25,8,1,10,
        1,12,1,28,9,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,41,
        8,3,10,3,12,3,44,9,3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,52,8,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,89,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,99,8,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,111,8,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,125,8,6,10,6,12,6,128,9,6,1,6,
        0,1,12,7,0,2,4,6,8,10,12,0,0,148,0,15,1,0,0,0,2,19,1,0,0,0,4,29,
        1,0,0,0,6,34,1,0,0,0,8,88,1,0,0,0,10,98,1,0,0,0,12,110,1,0,0,0,14,
        16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,
        0,18,1,1,0,0,0,19,20,5,1,0,0,20,21,5,26,0,0,21,26,5,23,0,0,22,25,
        3,4,2,0,23,25,3,6,3,0,24,22,1,0,0,0,24,23,1,0,0,0,25,28,1,0,0,0,
        26,24,1,0,0,0,26,27,1,0,0,0,27,3,1,0,0,0,28,26,1,0,0,0,29,30,5,26,
        0,0,30,31,5,6,0,0,31,32,3,12,6,0,32,33,5,22,0,0,33,5,1,0,0,0,34,
        35,5,26,0,0,35,36,5,23,0,0,36,37,5,14,0,0,37,38,5,2,0,0,38,42,5,
        22,0,0,39,41,3,8,4,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,
        43,1,0,0,0,43,45,1,0,0,0,44,42,1,0,0,0,45,46,5,15,0,0,46,47,5,22,
        0,0,47,7,1,0,0,0,48,51,5,13,0,0,49,52,3,12,6,0,50,52,5,3,0,0,51,
        49,1,0,0,0,51,50,1,0,0,0,52,53,1,0,0,0,53,89,5,22,0,0,54,55,3,12,
        6,0,55,56,5,7,0,0,56,57,3,12,6,0,57,58,5,22,0,0,58,89,1,0,0,0,59,
        60,3,12,6,0,60,61,5,8,0,0,61,62,3,12,6,0,62,63,5,22,0,0,63,89,1,
        0,0,0,64,65,3,12,6,0,65,66,5,9,0,0,66,67,3,12,6,0,67,68,5,22,0,0,
        68,89,1,0,0,0,69,70,5,16,0,0,70,71,3,12,6,0,71,72,5,17,0,0,72,73,
        5,25,0,0,73,74,5,22,0,0,74,89,1,0,0,0,75,76,5,17,0,0,76,77,5,25,
        0,0,77,89,5,22,0,0,78,79,5,18,0,0,79,80,3,12,6,0,80,81,5,22,0,0,
        81,89,1,0,0,0,82,83,5,19,0,0,83,84,5,2,0,0,84,89,5,22,0,0,85,89,
        3,10,5,0,86,87,5,25,0,0,87,89,5,23,0,0,88,48,1,0,0,0,88,54,1,0,0,
        0,88,59,1,0,0,0,88,64,1,0,0,0,88,69,1,0,0,0,88,75,1,0,0,0,88,78,
        1,0,0,0,88,82,1,0,0,0,88,85,1,0,0,0,88,86,1,0,0,0,89,9,1,0,0,0,90,
        91,5,20,0,0,91,92,5,26,0,0,92,93,5,12,0,0,93,94,5,26,0,0,94,99,5,
        22,0,0,95,96,5,20,0,0,96,97,5,26,0,0,97,99,5,22,0,0,98,90,1,0,0,
        0,98,95,1,0,0,0,99,11,1,0,0,0,100,101,6,6,-1,0,101,111,5,3,0,0,102,
        111,5,24,0,0,103,111,5,25,0,0,104,111,5,26,0,0,105,111,5,5,0,0,106,
        111,5,2,0,0,107,111,5,4,0,0,108,109,5,8,0,0,109,111,3,12,6,4,110,
        100,1,0,0,0,110,102,1,0,0,0,110,103,1,0,0,0,110,104,1,0,0,0,110,
        105,1,0,0,0,110,106,1,0,0,0,110,107,1,0,0,0,110,108,1,0,0,0,111,
        126,1,0,0,0,112,113,10,5,0,0,113,114,5,21,0,0,114,125,3,12,6,6,115,
        116,10,3,0,0,116,117,5,9,0,0,117,125,3,12,6,4,118,119,10,2,0,0,119,
        120,5,10,0,0,120,125,3,12,6,3,121,122,10,1,0,0,122,123,5,11,0,0,
        123,125,3,12,6,2,124,112,1,0,0,0,124,115,1,0,0,0,124,118,1,0,0,0,
        124,121,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,
        127,13,1,0,0,0,128,126,1,0,0,0,10,17,24,26,42,51,88,98,110,124,126
    ]

class ThreeAddressCodeParser ( Parser ):

    grammarFileName = "ThreeAddressCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "<INVALID>", "'self'", "<INVALID>", 
                     "<INVALID>", "'<-'", "'='", "'~'", "'<'", "'<='", "'=='", 
                     "'.'", "'Return'", "'BeginFunc'", "'EndFunc'", "'Ifz'", 
                     "'Goto'", "'PushParam'", "'PopParams'", "'FCall'", 
                     "<INVALID>", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "NUMBER", "SELF", "STRING", 
                      "BOOLEAN", "ASSIGN", "EQUAL", "NEGATE", "LT", "LT_EQUAL", 
                      "COMPARE", "DOT", "RETURN", "BEGIN_FUNC", "END_FUNC", 
                      "IFZ", "GOTO", "PUSH_PARAM", "POP_PARAMS", "FCALL", 
                      "OP", "SEMI", "COLON", "TEMPORAL", "LABEL", "IDENTIFIER", 
                      "WHITESPACE" ]

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
    SELF=3
    STRING=4
    BOOLEAN=5
    ASSIGN=6
    EQUAL=7
    NEGATE=8
    LT=9
    LT_EQUAL=10
    COMPARE=11
    DOT=12
    RETURN=13
    BEGIN_FUNC=14
    END_FUNC=15
    IFZ=16
    GOTO=17
    PUSH_PARAM=18
    POP_PARAMS=19
    FCALL=20
    OP=21
    SEMI=22
    COLON=23
    TEMPORAL=24
    LABEL=25
    IDENTIFIER=26
    WHITESPACE=27

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
            while _la==26:
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
            self.expression(0)
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 119480636) != 0):
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,i)

        def EQUAL(self):
            return self.getToken(ThreeAddressCodeParser.EQUAL, 0)
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
        def expression(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,0)

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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,i)

        def NEGATE(self):
            return self.getToken(ThreeAddressCodeParser.NEGATE, 0)
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
        def expression(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,0)

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
        def SEMI(self):
            return self.getToken(ThreeAddressCodeParser.SEMI, 0)
        def expression(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,0)

        def SELF(self):
            return self.getToken(ThreeAddressCodeParser.SELF, 0)

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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,i)

        def LT(self):
            return self.getToken(ThreeAddressCodeParser.LT, 0)
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
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = ThreeAddressCodeParser.ReturnInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(ThreeAddressCodeParser.RETURN)
                self.state = 51
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 49
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 50
                    self.match(ThreeAddressCodeParser.SELF)
                    pass


                self.state = 53
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 2:
                localctx = ThreeAddressCodeParser.EqualInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.expression(0)
                self.state = 55
                self.match(ThreeAddressCodeParser.EQUAL)
                self.state = 56
                self.expression(0)
                self.state = 57
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 3:
                localctx = ThreeAddressCodeParser.NegateInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.expression(0)
                self.state = 60
                self.match(ThreeAddressCodeParser.NEGATE)
                self.state = 61
                self.expression(0)
                self.state = 62
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 4:
                localctx = ThreeAddressCodeParser.LtInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.expression(0)
                self.state = 65
                self.match(ThreeAddressCodeParser.LT)
                self.state = 66
                self.expression(0)
                self.state = 67
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 5:
                localctx = ThreeAddressCodeParser.IfInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.match(ThreeAddressCodeParser.IFZ)
                self.state = 70
                self.expression(0)
                self.state = 71
                self.match(ThreeAddressCodeParser.GOTO)
                self.state = 72
                self.match(ThreeAddressCodeParser.LABEL)
                self.state = 73
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 6:
                localctx = ThreeAddressCodeParser.GotoInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 75
                self.match(ThreeAddressCodeParser.GOTO)
                self.state = 76
                self.match(ThreeAddressCodeParser.LABEL)
                self.state = 77
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 7:
                localctx = ThreeAddressCodeParser.PushParamInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 78
                self.match(ThreeAddressCodeParser.PUSH_PARAM)
                self.state = 79
                self.expression(0)
                self.state = 80
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 8:
                localctx = ThreeAddressCodeParser.PopParamInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 82
                self.match(ThreeAddressCodeParser.POP_PARAMS)
                self.state = 83
                self.match(ThreeAddressCodeParser.NUMBER)
                self.state = 84
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 9:
                localctx = ThreeAddressCodeParser.FCallInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 85
                self.fCallStatement()
                pass

            elif la_ == 10:
                localctx = ThreeAddressCodeParser.LabelInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 86
                self.match(ThreeAddressCodeParser.LABEL)
                self.state = 87
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
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(ThreeAddressCodeParser.FCALL)
                self.state = 91
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 92
                self.match(ThreeAddressCodeParser.DOT)
                self.state = 93
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 94
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(ThreeAddressCodeParser.FCALL)
                self.state = 96
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 97
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


        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TempExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEMPORAL(self):
            return self.getToken(ThreeAddressCodeParser.TEMPORAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTempExpr" ):
                listener.enterTempExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTempExpr" ):
                listener.exitTempExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTempExpr" ):
                return visitor.visitTempExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ThreeAddressCodeParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegateExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEGATE(self):
            return self.getToken(ThreeAddressCodeParser.NEGATE, 0)
        def expression(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegateExpr" ):
                listener.enterNegateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegateExpr" ):
                listener.exitNegateExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegateExpr" ):
                return visitor.visitNegateExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComparateExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,i)

        def COMPARE(self):
            return self.getToken(ThreeAddressCodeParser.COMPARE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparateExpr" ):
                listener.enterComparateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparateExpr" ):
                listener.exitComparateExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparateExpr" ):
                return visitor.visitComparateExpr(self)
            else:
                return visitor.visitChildren(self)


    class SelfExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SELF(self):
            return self.getToken(ThreeAddressCodeParser.SELF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelfExpr" ):
                listener.enterSelfExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelfExpr" ):
                listener.exitSelfExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelfExpr" ):
                return visitor.visitSelfExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(ThreeAddressCodeParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class OperatorExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,i)

        def OP(self):
            return self.getToken(ThreeAddressCodeParser.OP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorExpr" ):
                listener.enterOperatorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorExpr" ):
                listener.exitOperatorExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperatorExpr" ):
                return visitor.visitOperatorExpr(self)
            else:
                return visitor.visitChildren(self)


    class LabelExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LABEL(self):
            return self.getToken(ThreeAddressCodeParser.LABEL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelExpr" ):
                listener.enterLabelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelExpr" ):
                listener.exitLabelExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelExpr" ):
                return visitor.visitLabelExpr(self)
            else:
                return visitor.visitChildren(self)


    class GraterThanExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,i)

        def LT(self):
            return self.getToken(ThreeAddressCodeParser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraterThanExpr" ):
                listener.enterGraterThanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraterThanExpr" ):
                listener.exitGraterThanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraterThanExpr" ):
                return visitor.visitGraterThanExpr(self)
            else:
                return visitor.visitChildren(self)


    class GraterEqualExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.ExpressionContext,i)

        def LT_EQUAL(self):
            return self.getToken(ThreeAddressCodeParser.LT_EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraterEqualExpr" ):
                listener.enterGraterEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraterEqualExpr" ):
                listener.exitGraterEqualExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraterEqualExpr" ):
                return visitor.visitGraterEqualExpr(self)
            else:
                return visitor.visitChildren(self)


    class BoolExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(ThreeAddressCodeParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ThreeAddressCodeParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ThreeAddressCodeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = ThreeAddressCodeParser.SelfExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 101
                self.match(ThreeAddressCodeParser.SELF)
                pass
            elif token in [24]:
                localctx = ThreeAddressCodeParser.TempExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.match(ThreeAddressCodeParser.TEMPORAL)
                pass
            elif token in [25]:
                localctx = ThreeAddressCodeParser.LabelExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 103
                self.match(ThreeAddressCodeParser.LABEL)
                pass
            elif token in [26]:
                localctx = ThreeAddressCodeParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                pass
            elif token in [5]:
                localctx = ThreeAddressCodeParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 105
                self.match(ThreeAddressCodeParser.BOOLEAN)
                pass
            elif token in [2]:
                localctx = ThreeAddressCodeParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(ThreeAddressCodeParser.NUMBER)
                pass
            elif token in [4]:
                localctx = ThreeAddressCodeParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(ThreeAddressCodeParser.STRING)
                pass
            elif token in [8]:
                localctx = ThreeAddressCodeParser.NegateExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(ThreeAddressCodeParser.NEGATE)
                self.state = 109
                self.expression(4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 124
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = ThreeAddressCodeParser.OperatorExprContext(self, ThreeAddressCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 112
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 113
                        self.match(ThreeAddressCodeParser.OP)
                        self.state = 114
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = ThreeAddressCodeParser.GraterThanExprContext(self, ThreeAddressCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 115
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 116
                        self.match(ThreeAddressCodeParser.LT)
                        self.state = 117
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = ThreeAddressCodeParser.GraterEqualExprContext(self, ThreeAddressCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 118
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 119
                        self.match(ThreeAddressCodeParser.LT_EQUAL)
                        self.state = 120
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = ThreeAddressCodeParser.ComparateExprContext(self, ThreeAddressCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 121
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 122
                        self.match(ThreeAddressCodeParser.COMPARE)
                        self.state = 123
                        self.expression(2)
                        pass

             
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




