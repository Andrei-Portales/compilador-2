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
        4,1,26,126,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,1,1,5,1,25,8,1,10,
        1,12,1,28,9,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,41,
        8,3,10,3,12,3,44,9,3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,52,8,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,92,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,102,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,124,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,2,
        0,2,2,25,25,144,0,15,1,0,0,0,2,19,1,0,0,0,4,29,1,0,0,0,6,34,1,0,
        0,0,8,91,1,0,0,0,10,101,1,0,0,0,12,123,1,0,0,0,14,16,3,2,1,0,15,
        14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,
        0,19,20,5,1,0,0,20,21,5,25,0,0,21,26,5,23,0,0,22,25,3,4,2,0,23,25,
        3,6,3,0,24,22,1,0,0,0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,
        26,27,1,0,0,0,27,3,1,0,0,0,28,26,1,0,0,0,29,30,5,25,0,0,30,31,5,
        6,0,0,31,32,3,12,6,0,32,33,5,22,0,0,33,5,1,0,0,0,34,35,5,25,0,0,
        35,36,5,23,0,0,36,37,5,14,0,0,37,38,5,2,0,0,38,42,5,22,0,0,39,41,
        3,8,4,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,
        43,45,1,0,0,0,44,42,1,0,0,0,45,46,5,15,0,0,46,47,5,22,0,0,47,7,1,
        0,0,0,48,51,5,13,0,0,49,52,3,12,6,0,50,52,5,3,0,0,51,49,1,0,0,0,
        51,50,1,0,0,0,52,53,1,0,0,0,53,92,5,22,0,0,54,55,5,25,0,0,55,56,
        5,6,0,0,56,57,3,12,6,0,57,58,5,22,0,0,58,92,1,0,0,0,59,60,5,25,0,
        0,60,61,5,7,0,0,61,62,3,12,6,0,62,63,5,22,0,0,63,92,1,0,0,0,64,65,
        5,25,0,0,65,66,5,8,0,0,66,67,3,12,6,0,67,68,5,22,0,0,68,92,1,0,0,
        0,69,70,5,25,0,0,70,71,5,9,0,0,71,72,3,12,6,0,72,73,5,22,0,0,73,
        92,1,0,0,0,74,75,5,16,0,0,75,76,5,25,0,0,76,77,5,17,0,0,77,78,5,
        24,0,0,78,92,5,22,0,0,79,80,5,17,0,0,80,81,5,24,0,0,81,92,5,22,0,
        0,82,83,5,18,0,0,83,84,5,25,0,0,84,92,5,22,0,0,85,86,5,19,0,0,86,
        87,5,2,0,0,87,92,5,22,0,0,88,92,3,10,5,0,89,90,5,24,0,0,90,92,5,
        23,0,0,91,48,1,0,0,0,91,54,1,0,0,0,91,59,1,0,0,0,91,64,1,0,0,0,91,
        69,1,0,0,0,91,74,1,0,0,0,91,79,1,0,0,0,91,82,1,0,0,0,91,85,1,0,0,
        0,91,88,1,0,0,0,91,89,1,0,0,0,92,9,1,0,0,0,93,94,5,20,0,0,94,95,
        5,25,0,0,95,96,5,12,0,0,96,97,5,25,0,0,97,102,5,22,0,0,98,99,5,20,
        0,0,99,100,5,25,0,0,100,102,5,22,0,0,101,93,1,0,0,0,101,98,1,0,0,
        0,102,11,1,0,0,0,103,124,5,3,0,0,104,124,5,25,0,0,105,124,5,5,0,
        0,106,124,5,2,0,0,107,124,5,4,0,0,108,124,5,24,0,0,109,110,7,0,0,
        0,110,111,5,21,0,0,111,124,7,0,0,0,112,113,5,8,0,0,113,124,7,0,0,
        0,114,115,7,0,0,0,115,116,5,9,0,0,116,124,7,0,0,0,117,118,7,0,0,
        0,118,119,5,10,0,0,119,124,7,0,0,0,120,121,7,0,0,0,121,122,5,11,
        0,0,122,124,7,0,0,0,123,103,1,0,0,0,123,104,1,0,0,0,123,105,1,0,
        0,0,123,106,1,0,0,0,123,107,1,0,0,0,123,108,1,0,0,0,123,109,1,0,
        0,0,123,112,1,0,0,0,123,114,1,0,0,0,123,117,1,0,0,0,123,120,1,0,
        0,0,124,13,1,0,0,0,8,17,24,26,42,51,91,101,123
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
                      "OP", "SEMI", "COLON", "LABEL", "IDENTIFIER", "WHITESPACE" ]

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
    LABEL=24
    IDENTIFIER=25
    WHITESPACE=26

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
            while _la==25:
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 52371456) != 0):
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
            self.state = 91
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
                    self.expression()
                    pass

                elif la_ == 2:
                    self.state = 50
                    self.match(ThreeAddressCodeParser.SELF)
                    pass


                self.state = 53
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 2:
                localctx = ThreeAddressCodeParser.AssignInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 55
                self.match(ThreeAddressCodeParser.ASSIGN)
                self.state = 56
                self.expression()
                self.state = 57
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 3:
                localctx = ThreeAddressCodeParser.EqualInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 60
                self.match(ThreeAddressCodeParser.EQUAL)
                self.state = 61
                self.expression()
                self.state = 62
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 4:
                localctx = ThreeAddressCodeParser.NegateInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 65
                self.match(ThreeAddressCodeParser.NEGATE)
                self.state = 66
                self.expression()
                self.state = 67
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 5:
                localctx = ThreeAddressCodeParser.LtInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 70
                self.match(ThreeAddressCodeParser.LT)
                self.state = 71
                self.expression()
                self.state = 72
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 6:
                localctx = ThreeAddressCodeParser.IfInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.match(ThreeAddressCodeParser.IFZ)
                self.state = 75
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 76
                self.match(ThreeAddressCodeParser.GOTO)
                self.state = 77
                self.match(ThreeAddressCodeParser.LABEL)
                self.state = 78
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 7:
                localctx = ThreeAddressCodeParser.GotoInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 79
                self.match(ThreeAddressCodeParser.GOTO)
                self.state = 80
                self.match(ThreeAddressCodeParser.LABEL)
                self.state = 81
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 8:
                localctx = ThreeAddressCodeParser.PushParamInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 82
                self.match(ThreeAddressCodeParser.PUSH_PARAM)
                self.state = 83
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 84
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 9:
                localctx = ThreeAddressCodeParser.PopParamInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 85
                self.match(ThreeAddressCodeParser.POP_PARAMS)
                self.state = 86
                self.match(ThreeAddressCodeParser.NUMBER)
                self.state = 87
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 10:
                localctx = ThreeAddressCodeParser.FCallInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 88
                self.fCallStatement()
                pass

            elif la_ == 11:
                localctx = ThreeAddressCodeParser.LabelInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 89
                self.match(ThreeAddressCodeParser.LABEL)
                self.state = 90
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
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(ThreeAddressCodeParser.FCALL)
                self.state = 94
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 95
                self.match(ThreeAddressCodeParser.DOT)
                self.state = 96
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 97
                self.match(ThreeAddressCodeParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(ThreeAddressCodeParser.FCALL)
                self.state = 99
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                self.state = 100
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
        def NUMBER(self):
            return self.getToken(ThreeAddressCodeParser.NUMBER, 0)
        def IDENTIFIER(self):
            return self.getToken(ThreeAddressCodeParser.IDENTIFIER, 0)

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

        def COMPARE(self):
            return self.getToken(ThreeAddressCodeParser.COMPARE, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.NUMBER)
            else:
                return self.getToken(ThreeAddressCodeParser.NUMBER, i)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.IDENTIFIER)
            else:
                return self.getToken(ThreeAddressCodeParser.IDENTIFIER, i)

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

        def OP(self):
            return self.getToken(ThreeAddressCodeParser.OP, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.NUMBER)
            else:
                return self.getToken(ThreeAddressCodeParser.NUMBER, i)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.IDENTIFIER)
            else:
                return self.getToken(ThreeAddressCodeParser.IDENTIFIER, i)

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

        def LT(self):
            return self.getToken(ThreeAddressCodeParser.LT, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.NUMBER)
            else:
                return self.getToken(ThreeAddressCodeParser.NUMBER, i)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.IDENTIFIER)
            else:
                return self.getToken(ThreeAddressCodeParser.IDENTIFIER, i)

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

        def LT_EQUAL(self):
            return self.getToken(ThreeAddressCodeParser.LT_EQUAL, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.NUMBER)
            else:
                return self.getToken(ThreeAddressCodeParser.NUMBER, i)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.IDENTIFIER)
            else:
                return self.getToken(ThreeAddressCodeParser.IDENTIFIER, i)

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



    def expression(self):

        localctx = ThreeAddressCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = ThreeAddressCodeParser.SelfExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(ThreeAddressCodeParser.SELF)
                pass

            elif la_ == 2:
                localctx = ThreeAddressCodeParser.IdExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(ThreeAddressCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                localctx = ThreeAddressCodeParser.BoolExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.match(ThreeAddressCodeParser.BOOLEAN)
                pass

            elif la_ == 4:
                localctx = ThreeAddressCodeParser.NumberExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.match(ThreeAddressCodeParser.NUMBER)
                pass

            elif la_ == 5:
                localctx = ThreeAddressCodeParser.StringExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.match(ThreeAddressCodeParser.STRING)
                pass

            elif la_ == 6:
                localctx = ThreeAddressCodeParser.LabelExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.match(ThreeAddressCodeParser.LABEL)
                pass

            elif la_ == 7:
                localctx = ThreeAddressCodeParser.OperatorExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 109
                _la = self._input.LA(1)
                if not(_la==2 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 110
                self.match(ThreeAddressCodeParser.OP)
                self.state = 111
                _la = self._input.LA(1)
                if not(_la==2 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 8:
                localctx = ThreeAddressCodeParser.NegateExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 112
                self.match(ThreeAddressCodeParser.NEGATE)
                self.state = 113
                _la = self._input.LA(1)
                if not(_la==2 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 9:
                localctx = ThreeAddressCodeParser.GraterThanExprContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 114
                _la = self._input.LA(1)
                if not(_la==2 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 115
                self.match(ThreeAddressCodeParser.LT)
                self.state = 116
                _la = self._input.LA(1)
                if not(_la==2 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 10:
                localctx = ThreeAddressCodeParser.GraterEqualExprContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 117
                _la = self._input.LA(1)
                if not(_la==2 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 118
                self.match(ThreeAddressCodeParser.LT_EQUAL)
                self.state = 119
                _la = self._input.LA(1)
                if not(_la==2 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 11:
                localctx = ThreeAddressCodeParser.ComparateExprContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 120
                _la = self._input.LA(1)
                if not(_la==2 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 121
                self.match(ThreeAddressCodeParser.COMPARE)
                self.state = 122
                _la = self._input.LA(1)
                if not(_la==2 or _la==25):
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





