# Generated from grammar/YALPParser.g4 by ANTLR 4.13.0
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
        4,1,47,196,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,1,1,3,1,24,8,1,1,1,1,1,
        1,1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        5,2,42,8,2,10,2,12,2,45,9,2,3,2,47,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,61,8,2,3,2,63,8,2,1,3,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        5,4,86,8,4,10,4,12,4,89,9,4,3,4,91,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,112,8,4,11,
        4,12,4,113,1,4,1,4,1,4,1,4,1,4,1,4,5,4,122,8,4,10,4,12,4,125,9,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,140,8,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,175,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,183,8,4,10,4,12,4,186,
        9,4,3,4,188,8,4,1,4,5,4,191,8,4,10,4,12,4,194,9,4,1,4,0,1,8,5,0,
        2,4,6,8,0,0,231,0,13,1,0,0,0,2,19,1,0,0,0,4,62,1,0,0,0,6,64,1,0,
        0,0,8,139,1,0,0,0,10,11,3,2,1,0,11,12,5,35,0,0,12,14,1,0,0,0,13,
        10,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,
        0,17,18,5,0,0,1,18,1,1,0,0,0,19,20,5,4,0,0,20,23,5,43,0,0,21,22,
        5,15,0,0,22,24,5,43,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,
        0,25,31,5,39,0,0,26,27,3,4,2,0,27,28,5,35,0,0,28,30,1,0,0,0,29,26,
        1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,
        33,31,1,0,0,0,34,35,5,40,0,0,35,3,1,0,0,0,36,37,5,44,0,0,37,46,5,
        37,0,0,38,43,3,6,3,0,39,40,5,36,0,0,40,42,3,6,3,0,41,39,1,0,0,0,
        42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,47,1,0,0,0,45,43,1,
        0,0,0,46,38,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,5,38,0,0,49,
        50,5,34,0,0,50,51,5,43,0,0,51,52,5,39,0,0,52,53,3,8,4,0,53,54,5,
        40,0,0,54,63,1,0,0,0,55,56,5,44,0,0,56,57,5,34,0,0,57,60,5,43,0,
        0,58,59,5,31,0,0,59,61,3,8,4,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,
        1,0,0,0,62,36,1,0,0,0,62,55,1,0,0,0,63,5,1,0,0,0,64,65,5,44,0,0,
        65,66,5,34,0,0,66,67,5,43,0,0,67,7,1,0,0,0,68,69,6,4,-1,0,69,70,
        5,30,0,0,70,140,3,8,4,18,71,72,5,20,0,0,72,140,3,8,4,17,73,140,5,
        1,0,0,74,140,5,2,0,0,75,140,5,12,0,0,76,140,5,13,0,0,77,78,5,44,
        0,0,78,79,5,31,0,0,79,140,3,8,4,12,80,81,5,44,0,0,81,90,5,37,0,0,
        82,87,3,8,4,0,83,84,5,36,0,0,84,86,3,8,4,0,85,83,1,0,0,0,86,89,1,
        0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,90,
        82,1,0,0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,140,5,38,0,0,93,94,5,5,
        0,0,94,95,3,8,4,0,95,96,5,6,0,0,96,97,3,8,4,0,97,98,5,7,0,0,98,99,
        3,8,4,0,99,100,5,8,0,0,100,140,1,0,0,0,101,102,5,9,0,0,102,103,3,
        8,4,0,103,104,5,10,0,0,104,105,3,8,4,0,105,106,5,11,0,0,106,140,
        1,0,0,0,107,111,5,39,0,0,108,109,3,8,4,0,109,110,5,35,0,0,110,112,
        1,0,0,0,111,108,1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,
        1,0,0,0,114,115,1,0,0,0,115,116,5,40,0,0,116,140,1,0,0,0,117,118,
        5,16,0,0,118,123,3,4,2,0,119,120,5,36,0,0,120,122,3,4,2,0,121,119,
        1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,126,
        1,0,0,0,125,123,1,0,0,0,126,127,5,14,0,0,127,128,3,8,4,6,128,140,
        1,0,0,0,129,130,5,17,0,0,130,140,5,43,0,0,131,132,5,21,0,0,132,140,
        3,8,4,4,133,134,5,37,0,0,134,135,3,8,4,0,135,136,5,38,0,0,136,140,
        1,0,0,0,137,140,5,44,0,0,138,140,5,43,0,0,139,68,1,0,0,0,139,71,
        1,0,0,0,139,73,1,0,0,0,139,74,1,0,0,0,139,75,1,0,0,0,139,76,1,0,
        0,0,139,77,1,0,0,0,139,80,1,0,0,0,139,93,1,0,0,0,139,101,1,0,0,0,
        139,107,1,0,0,0,139,117,1,0,0,0,139,129,1,0,0,0,139,131,1,0,0,0,
        139,133,1,0,0,0,139,137,1,0,0,0,139,138,1,0,0,0,140,192,1,0,0,0,
        141,142,10,28,0,0,142,143,5,22,0,0,143,191,3,8,4,29,144,145,10,27,
        0,0,145,146,5,23,0,0,146,191,3,8,4,28,147,148,10,26,0,0,148,149,
        5,26,0,0,149,191,3,8,4,27,150,151,10,25,0,0,151,152,5,24,0,0,152,
        191,3,8,4,26,153,154,10,24,0,0,154,155,5,25,0,0,155,191,3,8,4,25,
        156,157,10,23,0,0,157,158,5,29,0,0,158,191,3,8,4,24,159,160,10,22,
        0,0,160,161,5,27,0,0,161,191,3,8,4,23,162,163,10,21,0,0,163,164,
        5,28,0,0,164,191,3,8,4,22,165,166,10,20,0,0,166,167,5,32,0,0,167,
        191,3,8,4,21,168,169,10,19,0,0,169,170,5,33,0,0,170,191,3,8,4,20,
        171,174,10,11,0,0,172,173,5,19,0,0,173,175,5,43,0,0,174,172,1,0,
        0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,5,18,0,0,177,178,5,44,
        0,0,178,187,5,37,0,0,179,184,3,8,4,0,180,181,5,36,0,0,181,183,3,
        8,4,0,182,180,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,
        0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,187,179,1,0,0,0,187,188,1,
        0,0,0,188,189,1,0,0,0,189,191,5,38,0,0,190,141,1,0,0,0,190,144,1,
        0,0,0,190,147,1,0,0,0,190,150,1,0,0,0,190,153,1,0,0,0,190,156,1,
        0,0,0,190,159,1,0,0,0,190,162,1,0,0,0,190,165,1,0,0,0,190,168,1,
        0,0,0,190,171,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,
        0,0,0,193,9,1,0,0,0,194,192,1,0,0,0,17,15,23,31,43,46,60,62,87,90,
        113,123,139,174,184,187,190,192
    ]

class YALPParser ( Parser ):

    grammarFileName = "YALPParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'_'", "'class'", 
                     "'if'", "'then'", "'else'", "'fi'", "'while'", "'loop'", 
                     "'pool'", "'true'", "'false'", "'in'", "'inherits'", 
                     "'let'", "'new'", "'.'", "'@'", "'~'", "'isvoid'", 
                     "'*'", "'/'", "'+'", "'-'", "'%'", "'<='", "'<'", "'='", 
                     "'not'", "'<-'", "'&&'", "'||'", "':'", "';'", "','", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "INTEGER", "STRING", "ANY", "CLASS", 
                      "IF", "THEN", "ELSE", "FI", "WHILE", "LOOP", "POOL", 
                      "TRUE", "FALSE", "IN", "INHERITS", "LET", "NEW", "DOT", 
                      "SIGN", "NEGATE", "ISVOID", "TIMES", "DIVIDE", "PLUS", 
                      "MINUS", "MOD", "LESS_EQUAL", "LESS_THAN", "EQUAL", 
                      "NOT", "ASSIGN", "AND", "OR", "COLON", "SEMICOLON", 
                      "COMMA", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRAKE", 
                      "RBRAKE", "TYPE_ID", "OBJECT_ID", "WS", "COMMENT", 
                      "LARGE_COMMENT" ]

    RULE_program = 0
    RULE_class = 1
    RULE_feature = 2
    RULE_formal = 3
    RULE_expr = 4

    ruleNames =  [ "program", "class", "feature", "formal", "expr" ]

    EOF = Token.EOF
    INTEGER=1
    STRING=2
    ANY=3
    CLASS=4
    IF=5
    THEN=6
    ELSE=7
    FI=8
    WHILE=9
    LOOP=10
    POOL=11
    TRUE=12
    FALSE=13
    IN=14
    INHERITS=15
    LET=16
    NEW=17
    DOT=18
    SIGN=19
    NEGATE=20
    ISVOID=21
    TIMES=22
    DIVIDE=23
    PLUS=24
    MINUS=25
    MOD=26
    LESS_EQUAL=27
    LESS_THAN=28
    EQUAL=29
    NOT=30
    ASSIGN=31
    AND=32
    OR=33
    COLON=34
    SEMICOLON=35
    COMMA=36
    LPAREN=37
    RPAREN=38
    LBRACE=39
    RBRACE=40
    LBRAKE=41
    RBRAKE=42
    TYPE_ID=43
    OBJECT_ID=44
    WS=45
    COMMENT=46
    LARGE_COMMENT=47

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

        def EOF(self):
            return self.getToken(YALPParser.EOF, 0)

        def class_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ClassContext)
            else:
                return self.getTypedRuleContext(YALPParser.ClassContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.SEMICOLON)
            else:
                return self.getToken(YALPParser.SEMICOLON, i)

        def getRuleIndex(self):
            return YALPParser.RULE_program

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

        localctx = YALPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.class_()
                self.state = 11
                self.match(YALPParser.SEMICOLON)
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 17
            self.match(YALPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(YALPParser.CLASS, 0)

        def TYPE_ID(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.TYPE_ID)
            else:
                return self.getToken(YALPParser.TYPE_ID, i)

        def LBRACE(self):
            return self.getToken(YALPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(YALPParser.RBRACE, 0)

        def INHERITS(self):
            return self.getToken(YALPParser.INHERITS, 0)

        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.FeatureContext)
            else:
                return self.getTypedRuleContext(YALPParser.FeatureContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.SEMICOLON)
            else:
                return self.getToken(YALPParser.SEMICOLON, i)

        def getRuleIndex(self):
            return YALPParser.RULE_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass" ):
                listener.enterClass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass" ):
                listener.exitClass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass" ):
                return visitor.visitClass(self)
            else:
                return visitor.visitChildren(self)




    def class_(self):

        localctx = YALPParser.ClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(YALPParser.CLASS)
            self.state = 20
            self.match(YALPParser.TYPE_ID)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 21
                self.match(YALPParser.INHERITS)
                self.state = 22
                self.match(YALPParser.TYPE_ID)


            self.state = 25
            self.match(YALPParser.LBRACE)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 26
                self.feature()
                self.state = 27
                self.match(YALPParser.SEMICOLON)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(YALPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return YALPParser.RULE_feature

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VariableFeatureContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJECT_ID(self):
            return self.getToken(YALPParser.OBJECT_ID, 0)
        def COLON(self):
            return self.getToken(YALPParser.COLON, 0)
        def TYPE_ID(self):
            return self.getToken(YALPParser.TYPE_ID, 0)
        def ASSIGN(self):
            return self.getToken(YALPParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(YALPParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableFeature" ):
                listener.enterVariableFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableFeature" ):
                listener.exitVariableFeature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableFeature" ):
                return visitor.visitVariableFeature(self)
            else:
                return visitor.visitChildren(self)


    class MethodFeatureContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJECT_ID(self):
            return self.getToken(YALPParser.OBJECT_ID, 0)
        def LPAREN(self):
            return self.getToken(YALPParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(YALPParser.RPAREN, 0)
        def COLON(self):
            return self.getToken(YALPParser.COLON, 0)
        def TYPE_ID(self):
            return self.getToken(YALPParser.TYPE_ID, 0)
        def LBRACE(self):
            return self.getToken(YALPParser.LBRACE, 0)
        def expr(self):
            return self.getTypedRuleContext(YALPParser.ExprContext,0)

        def RBRACE(self):
            return self.getToken(YALPParser.RBRACE, 0)
        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.FormalContext)
            else:
                return self.getTypedRuleContext(YALPParser.FormalContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.COMMA)
            else:
                return self.getToken(YALPParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodFeature" ):
                listener.enterMethodFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodFeature" ):
                listener.exitMethodFeature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodFeature" ):
                return visitor.visitMethodFeature(self)
            else:
                return visitor.visitChildren(self)



    def feature(self):

        localctx = YALPParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_feature)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = YALPParser.MethodFeatureContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(YALPParser.OBJECT_ID)
                self.state = 37
                self.match(YALPParser.LPAREN)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==44:
                    self.state = 38
                    self.formal()
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==36:
                        self.state = 39
                        self.match(YALPParser.COMMA)
                        self.state = 40
                        self.formal()
                        self.state = 45
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 48
                self.match(YALPParser.RPAREN)
                self.state = 49
                self.match(YALPParser.COLON)
                self.state = 50
                self.match(YALPParser.TYPE_ID)
                self.state = 51
                self.match(YALPParser.LBRACE)
                self.state = 52
                self.expr(0)
                self.state = 53
                self.match(YALPParser.RBRACE)
                pass

            elif la_ == 2:
                localctx = YALPParser.VariableFeatureContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(YALPParser.OBJECT_ID)
                self.state = 56
                self.match(YALPParser.COLON)
                self.state = 57
                self.match(YALPParser.TYPE_ID)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 58
                    self.match(YALPParser.ASSIGN)
                    self.state = 59
                    self.expr(0)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return YALPParser.RULE_formal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MethodParamContext(FormalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.FormalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJECT_ID(self):
            return self.getToken(YALPParser.OBJECT_ID, 0)
        def COLON(self):
            return self.getToken(YALPParser.COLON, 0)
        def TYPE_ID(self):
            return self.getToken(YALPParser.TYPE_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodParam" ):
                listener.enterMethodParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodParam" ):
                listener.exitMethodParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodParam" ):
                return visitor.visitMethodParam(self)
            else:
                return visitor.visitChildren(self)



    def formal(self):

        localctx = YALPParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_formal)
        try:
            localctx = YALPParser.MethodParamContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(YALPParser.OBJECT_ID)
            self.state = 65
            self.match(YALPParser.COLON)
            self.state = 66
            self.match(YALPParser.TYPE_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return YALPParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class WhileExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(YALPParser.WHILE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def LOOP(self):
            return self.getToken(YALPParser.LOOP, 0)
        def POOL(self):
            return self.getToken(YALPParser.POOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileExpr" ):
                listener.enterWhileExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileExpr" ):
                listener.exitWhileExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileExpr" ):
                return visitor.visitWhileExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def AND(self):
            return self.getToken(YALPParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(YALPParser.STRING, 0)

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


    class EqualExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def EQUAL(self):
            return self.getToken(YALPParser.EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualExpr" ):
                listener.enterEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualExpr" ):
                listener.exitEqualExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualExpr" ):
                return visitor.visitEqualExpr(self)
            else:
                return visitor.visitChildren(self)


    class IfExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(YALPParser.IF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def THEN(self):
            return self.getToken(YALPParser.THEN, 0)
        def ELSE(self):
            return self.getToken(YALPParser.ELSE, 0)
        def FI(self):
            return self.getToken(YALPParser.FI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpr" ):
                listener.enterIfExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpr" ):
                listener.exitIfExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpr" ):
                return visitor.visitIfExpr(self)
            else:
                return visitor.visitChildren(self)


    class TrueExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(YALPParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueExpr" ):
                listener.enterTrueExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueExpr" ):
                listener.exitTrueExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueExpr" ):
                return visitor.visitTrueExpr(self)
            else:
                return visitor.visitChildren(self)


    class FalseExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(YALPParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseExpr" ):
                listener.enterFalseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseExpr" ):
                listener.exitFalseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseExpr" ):
                return visitor.visitFalseExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJECT_ID(self):
            return self.getToken(YALPParser.OBJECT_ID, 0)
        def ASSIGN(self):
            return self.getToken(YALPParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(YALPParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivideExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def DIVIDE(self):
            return self.getToken(YALPParser.DIVIDE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivideExpr" ):
                listener.enterDivideExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivideExpr" ):
                listener.exitDivideExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivideExpr" ):
                return visitor.visitDivideExpr(self)
            else:
                return visitor.visitChildren(self)


    class LessEqualExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def LESS_EQUAL(self):
            return self.getToken(YALPParser.LESS_EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessEqualExpr" ):
                listener.enterLessEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessEqualExpr" ):
                listener.exitLessEqualExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessEqualExpr" ):
                return visitor.visitLessEqualExpr(self)
            else:
                return visitor.visitChildren(self)


    class PlusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(YALPParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusExpr" ):
                listener.enterPlusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusExpr" ):
                listener.exitPlusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusExpr" ):
                return visitor.visitPlusExpr(self)
            else:
                return visitor.visitChildren(self)


    class CallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJECT_ID(self):
            return self.getToken(YALPParser.OBJECT_ID, 0)
        def LPAREN(self):
            return self.getToken(YALPParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(YALPParser.RPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.COMMA)
            else:
                return self.getToken(YALPParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExpr" ):
                listener.enterCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExpr" ):
                listener.exitCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpr" ):
                return visitor.visitCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(YALPParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(YALPParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class LessThanExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def LESS_THAN(self):
            return self.getToken(YALPParser.LESS_THAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThanExpr" ):
                listener.enterLessThanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThanExpr" ):
                listener.exitLessThanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThanExpr" ):
                return visitor.visitLessThanExpr(self)
            else:
                return visitor.visitChildren(self)


    class TimesExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def TIMES(self):
            return self.getToken(YALPParser.TIMES, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimesExpr" ):
                listener.enterTimesExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimesExpr" ):
                listener.exitTimesExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimesExpr" ):
                return visitor.visitTimesExpr(self)
            else:
                return visitor.visitChildren(self)


    class MinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def MINUS(self):
            return self.getToken(YALPParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinusExpr" ):
                listener.enterMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinusExpr" ):
                listener.exitMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinusExpr" ):
                return visitor.visitMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJECT_ID(self):
            return self.getToken(YALPParser.OBJECT_ID, 0)

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


    class LetExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(YALPParser.LET, 0)
        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.FeatureContext)
            else:
                return self.getTypedRuleContext(YALPParser.FeatureContext,i)

        def IN(self):
            return self.getToken(YALPParser.IN, 0)
        def expr(self):
            return self.getTypedRuleContext(YALPParser.ExprContext,0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.COMMA)
            else:
                return self.getToken(YALPParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetExpr" ):
                listener.enterLetExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetExpr" ):
                listener.exitLetExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetExpr" ):
                return visitor.visitLetExpr(self)
            else:
                return visitor.visitChildren(self)


    class DotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def DOT(self):
            return self.getToken(YALPParser.DOT, 0)
        def OBJECT_ID(self):
            return self.getToken(YALPParser.OBJECT_ID, 0)
        def LPAREN(self):
            return self.getToken(YALPParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(YALPParser.RPAREN, 0)
        def SIGN(self):
            return self.getToken(YALPParser.SIGN, 0)
        def TYPE_ID(self):
            return self.getToken(YALPParser.TYPE_ID, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.COMMA)
            else:
                return self.getToken(YALPParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDotExpr" ):
                listener.enterDotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDotExpr" ):
                listener.exitDotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDotExpr" ):
                return visitor.visitDotExpr(self)
            else:
                return visitor.visitChildren(self)


    class TypeExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE_ID(self):
            return self.getToken(YALPParser.TYPE_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeExpr" ):
                listener.enterTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeExpr" ):
                listener.exitTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeExpr" ):
                return visitor.visitTypeExpr(self)
            else:
                return visitor.visitChildren(self)


    class BlockExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(YALPParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(YALPParser.RBRACE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.SEMICOLON)
            else:
                return self.getToken(YALPParser.SEMICOLON, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockExpr" ):
                listener.enterBlockExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockExpr" ):
                listener.exitBlockExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockExpr" ):
                return visitor.visitBlockExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def OR(self):
            return self.getToken(YALPParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegateExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEGATE(self):
            return self.getToken(YALPParser.NEGATE, 0)
        def expr(self):
            return self.getTypedRuleContext(YALPParser.ExprContext,0)


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


    class IsvoidExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ISVOID(self):
            return self.getToken(YALPParser.ISVOID, 0)
        def expr(self):
            return self.getTypedRuleContext(YALPParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsvoidExpr" ):
                listener.enterIsvoidExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsvoidExpr" ):
                listener.exitIsvoidExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsvoidExpr" ):
                return visitor.visitIsvoidExpr(self)
            else:
                return visitor.visitChildren(self)


    class NewExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(YALPParser.NEW, 0)
        def TYPE_ID(self):
            return self.getToken(YALPParser.TYPE_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewExpr" ):
                listener.enterNewExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewExpr" ):
                listener.exitNewExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewExpr" ):
                return visitor.visitNewExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(YALPParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class ModExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)

        def MOD(self):
            return self.getToken(YALPParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModExpr" ):
                listener.enterModExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModExpr" ):
                listener.exitModExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModExpr" ):
                return visitor.visitModExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YALPParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(YALPParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(YALPParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(YALPParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = YALPParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = YALPParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 69
                self.match(YALPParser.NOT)
                self.state = 70
                self.expr(18)
                pass

            elif la_ == 2:
                localctx = YALPParser.NegateExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(YALPParser.NEGATE)
                self.state = 72
                self.expr(17)
                pass

            elif la_ == 3:
                localctx = YALPParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 73
                self.match(YALPParser.INTEGER)
                pass

            elif la_ == 4:
                localctx = YALPParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                self.match(YALPParser.STRING)
                pass

            elif la_ == 5:
                localctx = YALPParser.TrueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 75
                self.match(YALPParser.TRUE)
                pass

            elif la_ == 6:
                localctx = YALPParser.FalseExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(YALPParser.FALSE)
                pass

            elif la_ == 7:
                localctx = YALPParser.AssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                self.match(YALPParser.OBJECT_ID)
                self.state = 78
                self.match(YALPParser.ASSIGN)
                self.state = 79
                self.expr(12)
                pass

            elif la_ == 8:
                localctx = YALPParser.CallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self.match(YALPParser.OBJECT_ID)
                self.state = 81
                self.match(YALPParser.LPAREN)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 27076550930982) != 0):
                    self.state = 82
                    self.expr(0)
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==36:
                        self.state = 83
                        self.match(YALPParser.COMMA)
                        self.state = 84
                        self.expr(0)
                        self.state = 89
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 92
                self.match(YALPParser.RPAREN)
                pass

            elif la_ == 9:
                localctx = YALPParser.IfExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                self.match(YALPParser.IF)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(YALPParser.THEN)
                self.state = 96
                self.expr(0)
                self.state = 97
                self.match(YALPParser.ELSE)
                self.state = 98
                self.expr(0)
                self.state = 99
                self.match(YALPParser.FI)
                pass

            elif la_ == 10:
                localctx = YALPParser.WhileExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.match(YALPParser.WHILE)
                self.state = 102
                self.expr(0)
                self.state = 103
                self.match(YALPParser.LOOP)
                self.state = 104
                self.expr(0)
                self.state = 105
                self.match(YALPParser.POOL)
                pass

            elif la_ == 11:
                localctx = YALPParser.BlockExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(YALPParser.LBRACE)
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 108
                    self.expr(0)
                    self.state = 109
                    self.match(YALPParser.SEMICOLON)
                    self.state = 113 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 27076550930982) != 0)):
                        break

                self.state = 115
                self.match(YALPParser.RBRACE)
                pass

            elif la_ == 12:
                localctx = YALPParser.LetExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                self.match(YALPParser.LET)
                self.state = 118
                self.feature()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 119
                    self.match(YALPParser.COMMA)
                    self.state = 120
                    self.feature()
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 126
                self.match(YALPParser.IN)
                self.state = 127
                self.expr(6)
                pass

            elif la_ == 13:
                localctx = YALPParser.NewExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 129
                self.match(YALPParser.NEW)
                self.state = 130
                self.match(YALPParser.TYPE_ID)
                pass

            elif la_ == 14:
                localctx = YALPParser.IsvoidExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(YALPParser.ISVOID)
                self.state = 132
                self.expr(4)
                pass

            elif la_ == 15:
                localctx = YALPParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(YALPParser.LPAREN)
                self.state = 134
                self.expr(0)
                self.state = 135
                self.match(YALPParser.RPAREN)
                pass

            elif la_ == 16:
                localctx = YALPParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(YALPParser.OBJECT_ID)
                pass

            elif la_ == 17:
                localctx = YALPParser.TypeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(YALPParser.TYPE_ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 190
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = YALPParser.TimesExprContext(self, YALPParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 141
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 142
                        self.match(YALPParser.TIMES)
                        self.state = 143
                        self.expr(29)
                        pass

                    elif la_ == 2:
                        localctx = YALPParser.DivideExprContext(self, YALPParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 144
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 145
                        self.match(YALPParser.DIVIDE)
                        self.state = 146
                        self.expr(28)
                        pass

                    elif la_ == 3:
                        localctx = YALPParser.ModExprContext(self, YALPParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 147
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 148
                        self.match(YALPParser.MOD)
                        self.state = 149
                        self.expr(27)
                        pass

                    elif la_ == 4:
                        localctx = YALPParser.PlusExprContext(self, YALPParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 150
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 151
                        self.match(YALPParser.PLUS)
                        self.state = 152
                        self.expr(26)
                        pass

                    elif la_ == 5:
                        localctx = YALPParser.MinusExprContext(self, YALPParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 153
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 154
                        self.match(YALPParser.MINUS)
                        self.state = 155
                        self.expr(25)
                        pass

                    elif la_ == 6:
                        localctx = YALPParser.EqualExprContext(self, YALPParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 156
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 157
                        self.match(YALPParser.EQUAL)
                        self.state = 158
                        self.expr(24)
                        pass

                    elif la_ == 7:
                        localctx = YALPParser.LessEqualExprContext(self, YALPParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 159
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 160
                        self.match(YALPParser.LESS_EQUAL)
                        self.state = 161
                        self.expr(23)
                        pass

                    elif la_ == 8:
                        localctx = YALPParser.LessThanExprContext(self, YALPParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 163
                        self.match(YALPParser.LESS_THAN)
                        self.state = 164
                        self.expr(22)
                        pass

                    elif la_ == 9:
                        localctx = YALPParser.AndExprContext(self, YALPParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 166
                        self.match(YALPParser.AND)
                        self.state = 167
                        self.expr(21)
                        pass

                    elif la_ == 10:
                        localctx = YALPParser.OrExprContext(self, YALPParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 169
                        self.match(YALPParser.OR)
                        self.state = 170
                        self.expr(20)
                        pass

                    elif la_ == 11:
                        localctx = YALPParser.DotExprContext(self, YALPParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 174
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==19:
                            self.state = 172
                            self.match(YALPParser.SIGN)
                            self.state = 173
                            self.match(YALPParser.TYPE_ID)


                        self.state = 176
                        self.match(YALPParser.DOT)
                        self.state = 177
                        self.match(YALPParser.OBJECT_ID)
                        self.state = 178
                        self.match(YALPParser.LPAREN)
                        self.state = 187
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 27076550930982) != 0):
                            self.state = 179
                            self.expr(0)
                            self.state = 184
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==36:
                                self.state = 180
                                self.match(YALPParser.COMMA)
                                self.state = 181
                                self.expr(0)
                                self.state = 186
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 189
                        self.match(YALPParser.RPAREN)
                        pass

             
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 11)
         




