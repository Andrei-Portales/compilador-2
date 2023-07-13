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
        4,1,47,199,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,3,1,22,8,1,1,1,1,1,1,1,1,1,
        5,1,28,8,1,10,1,12,1,31,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,5,2,40,8,
        2,10,2,12,2,43,9,2,3,2,45,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,59,8,2,3,2,61,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,5,4,76,8,4,10,4,12,4,79,9,4,3,4,81,8,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,4,4,102,8,4,11,4,12,4,103,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,114,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,122,8,4,5,4,124,8,4,
        10,4,12,4,127,9,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,149,8,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,178,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,
        4,186,8,4,10,4,12,4,189,9,4,3,4,191,8,4,1,4,5,4,194,8,4,10,4,12,
        4,197,9,4,1,4,0,1,8,5,0,2,4,6,8,0,0,234,0,13,1,0,0,0,2,17,1,0,0,
        0,4,60,1,0,0,0,6,62,1,0,0,0,8,148,1,0,0,0,10,11,3,2,1,0,11,12,5,
        35,0,0,12,14,1,0,0,0,13,10,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,
        16,1,0,0,0,16,1,1,0,0,0,17,18,5,4,0,0,18,21,5,43,0,0,19,20,5,15,
        0,0,20,22,5,43,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,
        29,5,39,0,0,24,25,3,4,2,0,25,26,5,35,0,0,26,28,1,0,0,0,27,24,1,0,
        0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,
        1,0,0,0,32,33,5,40,0,0,33,3,1,0,0,0,34,35,5,44,0,0,35,44,5,37,0,
        0,36,41,3,6,3,0,37,38,5,36,0,0,38,40,3,6,3,0,39,37,1,0,0,0,40,43,
        1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,
        44,36,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,47,5,38,0,0,47,48,5,
        34,0,0,48,49,5,43,0,0,49,50,5,39,0,0,50,51,3,8,4,0,51,52,5,40,0,
        0,52,61,1,0,0,0,53,54,5,44,0,0,54,55,5,34,0,0,55,58,5,43,0,0,56,
        57,5,31,0,0,57,59,3,8,4,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,
        0,0,60,34,1,0,0,0,60,53,1,0,0,0,61,5,1,0,0,0,62,63,5,44,0,0,63,64,
        5,34,0,0,64,65,5,43,0,0,65,7,1,0,0,0,66,67,6,4,-1,0,67,68,5,44,0,
        0,68,69,5,31,0,0,69,149,3,8,4,26,70,71,5,44,0,0,71,80,5,37,0,0,72,
        77,3,8,4,0,73,74,5,36,0,0,74,76,3,8,4,0,75,73,1,0,0,0,76,79,1,0,
        0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,80,72,
        1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,149,5,38,0,0,83,84,5,5,0,
        0,84,85,3,8,4,0,85,86,5,6,0,0,86,87,3,8,4,0,87,88,5,7,0,0,88,89,
        3,8,4,0,89,90,5,8,0,0,90,149,1,0,0,0,91,92,5,9,0,0,92,93,3,8,4,0,
        93,94,5,10,0,0,94,95,3,8,4,0,95,96,5,11,0,0,96,149,1,0,0,0,97,101,
        5,39,0,0,98,99,3,8,4,0,99,100,5,35,0,0,100,102,1,0,0,0,101,98,1,
        0,0,0,102,103,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,105,1,
        0,0,0,105,106,5,40,0,0,106,149,1,0,0,0,107,108,5,16,0,0,108,109,
        5,44,0,0,109,110,5,34,0,0,110,113,5,43,0,0,111,112,5,31,0,0,112,
        114,3,8,4,0,113,111,1,0,0,0,113,114,1,0,0,0,114,125,1,0,0,0,115,
        116,5,36,0,0,116,117,5,44,0,0,117,118,5,34,0,0,118,121,5,43,0,0,
        119,120,5,31,0,0,120,122,3,8,4,0,121,119,1,0,0,0,121,122,1,0,0,0,
        122,124,1,0,0,0,123,115,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,
        125,126,1,0,0,0,126,128,1,0,0,0,127,125,1,0,0,0,128,129,5,14,0,0,
        129,149,3,8,4,20,130,131,5,17,0,0,131,149,5,43,0,0,132,133,5,21,
        0,0,133,149,3,8,4,18,134,135,5,30,0,0,135,149,3,8,4,9,136,137,5,
        20,0,0,137,149,3,8,4,8,138,139,5,37,0,0,139,140,3,8,4,0,140,141,
        5,38,0,0,141,149,1,0,0,0,142,149,5,44,0,0,143,149,5,43,0,0,144,149,
        5,1,0,0,145,149,5,2,0,0,146,149,5,12,0,0,147,149,5,13,0,0,148,66,
        1,0,0,0,148,70,1,0,0,0,148,83,1,0,0,0,148,91,1,0,0,0,148,97,1,0,
        0,0,148,107,1,0,0,0,148,130,1,0,0,0,148,132,1,0,0,0,148,134,1,0,
        0,0,148,136,1,0,0,0,148,138,1,0,0,0,148,142,1,0,0,0,148,143,1,0,
        0,0,148,144,1,0,0,0,148,145,1,0,0,0,148,146,1,0,0,0,148,147,1,0,
        0,0,149,195,1,0,0,0,150,151,10,17,0,0,151,152,5,24,0,0,152,194,3,
        8,4,18,153,154,10,16,0,0,154,155,5,25,0,0,155,194,3,8,4,17,156,157,
        10,15,0,0,157,158,5,22,0,0,158,194,3,8,4,16,159,160,10,14,0,0,160,
        161,5,23,0,0,161,194,3,8,4,15,162,163,10,13,0,0,163,164,5,26,0,0,
        164,194,3,8,4,14,165,166,10,12,0,0,166,167,5,28,0,0,167,194,3,8,
        4,13,168,169,10,11,0,0,169,170,5,27,0,0,170,194,3,8,4,12,171,172,
        10,10,0,0,172,173,5,29,0,0,173,194,3,8,4,11,174,177,10,25,0,0,175,
        176,5,19,0,0,176,178,5,43,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,
        179,1,0,0,0,179,180,5,18,0,0,180,181,5,44,0,0,181,190,5,37,0,0,182,
        187,3,8,4,0,183,184,5,36,0,0,184,186,3,8,4,0,185,183,1,0,0,0,186,
        189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,191,1,0,0,0,189,
        187,1,0,0,0,190,182,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,
        194,5,38,0,0,193,150,1,0,0,0,193,153,1,0,0,0,193,156,1,0,0,0,193,
        159,1,0,0,0,193,162,1,0,0,0,193,165,1,0,0,0,193,168,1,0,0,0,193,
        171,1,0,0,0,193,174,1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,
        196,1,0,0,0,196,9,1,0,0,0,197,195,1,0,0,0,19,15,21,29,41,44,58,60,
        77,80,103,113,121,125,148,177,187,190,193,195
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




    def class_(self):

        localctx = YALPParser.ClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(YALPParser.CLASS)
            self.state = 18
            self.match(YALPParser.TYPE_ID)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 19
                self.match(YALPParser.INHERITS)
                self.state = 20
                self.match(YALPParser.TYPE_ID)


            self.state = 23
            self.match(YALPParser.LBRACE)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 24
                self.feature()
                self.state = 25
                self.match(YALPParser.SEMICOLON)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
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

        def ASSIGN(self):
            return self.getToken(YALPParser.ASSIGN, 0)

        def getRuleIndex(self):
            return YALPParser.RULE_feature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature" ):
                listener.enterFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature" ):
                listener.exitFeature(self)




    def feature(self):

        localctx = YALPParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_feature)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(YALPParser.OBJECT_ID)
                self.state = 35
                self.match(YALPParser.LPAREN)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==44:
                    self.state = 36
                    self.formal()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==36:
                        self.state = 37
                        self.match(YALPParser.COMMA)
                        self.state = 38
                        self.formal()
                        self.state = 43
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 46
                self.match(YALPParser.RPAREN)
                self.state = 47
                self.match(YALPParser.COLON)
                self.state = 48
                self.match(YALPParser.TYPE_ID)
                self.state = 49
                self.match(YALPParser.LBRACE)
                self.state = 50
                self.expr(0)
                self.state = 51
                self.match(YALPParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(YALPParser.OBJECT_ID)
                self.state = 54
                self.match(YALPParser.COLON)
                self.state = 55
                self.match(YALPParser.TYPE_ID)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 56
                    self.match(YALPParser.ASSIGN)
                    self.state = 57
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

        def OBJECT_ID(self):
            return self.getToken(YALPParser.OBJECT_ID, 0)

        def COLON(self):
            return self.getToken(YALPParser.COLON, 0)

        def TYPE_ID(self):
            return self.getToken(YALPParser.TYPE_ID, 0)

        def getRuleIndex(self):
            return YALPParser.RULE_formal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal" ):
                listener.enterFormal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal" ):
                listener.exitFormal(self)




    def formal(self):

        localctx = YALPParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_formal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(YALPParser.OBJECT_ID)
            self.state = 63
            self.match(YALPParser.COLON)
            self.state = 64
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

        def OBJECT_ID(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.OBJECT_ID)
            else:
                return self.getToken(YALPParser.OBJECT_ID, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.ASSIGN)
            else:
                return self.getToken(YALPParser.ASSIGN, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YALPParser.ExprContext)
            else:
                return self.getTypedRuleContext(YALPParser.ExprContext,i)


        def LPAREN(self):
            return self.getToken(YALPParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(YALPParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.COMMA)
            else:
                return self.getToken(YALPParser.COMMA, i)

        def IF(self):
            return self.getToken(YALPParser.IF, 0)

        def THEN(self):
            return self.getToken(YALPParser.THEN, 0)

        def ELSE(self):
            return self.getToken(YALPParser.ELSE, 0)

        def FI(self):
            return self.getToken(YALPParser.FI, 0)

        def WHILE(self):
            return self.getToken(YALPParser.WHILE, 0)

        def LOOP(self):
            return self.getToken(YALPParser.LOOP, 0)

        def POOL(self):
            return self.getToken(YALPParser.POOL, 0)

        def LBRACE(self):
            return self.getToken(YALPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(YALPParser.RBRACE, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.SEMICOLON)
            else:
                return self.getToken(YALPParser.SEMICOLON, i)

        def LET(self):
            return self.getToken(YALPParser.LET, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.COLON)
            else:
                return self.getToken(YALPParser.COLON, i)

        def TYPE_ID(self, i:int=None):
            if i is None:
                return self.getTokens(YALPParser.TYPE_ID)
            else:
                return self.getToken(YALPParser.TYPE_ID, i)

        def IN(self):
            return self.getToken(YALPParser.IN, 0)

        def NEW(self):
            return self.getToken(YALPParser.NEW, 0)

        def ISVOID(self):
            return self.getToken(YALPParser.ISVOID, 0)

        def NOT(self):
            return self.getToken(YALPParser.NOT, 0)

        def NEGATE(self):
            return self.getToken(YALPParser.NEGATE, 0)

        def INTEGER(self):
            return self.getToken(YALPParser.INTEGER, 0)

        def STRING(self):
            return self.getToken(YALPParser.STRING, 0)

        def TRUE(self):
            return self.getToken(YALPParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(YALPParser.FALSE, 0)

        def PLUS(self):
            return self.getToken(YALPParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(YALPParser.MINUS, 0)

        def TIMES(self):
            return self.getToken(YALPParser.TIMES, 0)

        def DIVIDE(self):
            return self.getToken(YALPParser.DIVIDE, 0)

        def MOD(self):
            return self.getToken(YALPParser.MOD, 0)

        def LESS_THAN(self):
            return self.getToken(YALPParser.LESS_THAN, 0)

        def LESS_EQUAL(self):
            return self.getToken(YALPParser.LESS_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(YALPParser.EQUAL, 0)

        def DOT(self):
            return self.getToken(YALPParser.DOT, 0)

        def SIGN(self):
            return self.getToken(YALPParser.SIGN, 0)

        def getRuleIndex(self):
            return YALPParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



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
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 67
                self.match(YALPParser.OBJECT_ID)
                self.state = 68
                self.match(YALPParser.ASSIGN)
                self.state = 69
                self.expr(26)
                pass

            elif la_ == 2:
                self.state = 70
                self.match(YALPParser.OBJECT_ID)
                self.state = 71
                self.match(YALPParser.LPAREN)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 27076550930982) != 0):
                    self.state = 72
                    self.expr(0)
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==36:
                        self.state = 73
                        self.match(YALPParser.COMMA)
                        self.state = 74
                        self.expr(0)
                        self.state = 79
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 82
                self.match(YALPParser.RPAREN)
                pass

            elif la_ == 3:
                self.state = 83
                self.match(YALPParser.IF)
                self.state = 84
                self.expr(0)
                self.state = 85
                self.match(YALPParser.THEN)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(YALPParser.ELSE)
                self.state = 88
                self.expr(0)
                self.state = 89
                self.match(YALPParser.FI)
                pass

            elif la_ == 4:
                self.state = 91
                self.match(YALPParser.WHILE)
                self.state = 92
                self.expr(0)
                self.state = 93
                self.match(YALPParser.LOOP)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(YALPParser.POOL)
                pass

            elif la_ == 5:
                self.state = 97
                self.match(YALPParser.LBRACE)
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 98
                    self.expr(0)
                    self.state = 99
                    self.match(YALPParser.SEMICOLON)
                    self.state = 103 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 27076550930982) != 0)):
                        break

                self.state = 105
                self.match(YALPParser.RBRACE)
                pass

            elif la_ == 6:
                self.state = 107
                self.match(YALPParser.LET)
                self.state = 108
                self.match(YALPParser.OBJECT_ID)
                self.state = 109
                self.match(YALPParser.COLON)
                self.state = 110
                self.match(YALPParser.TYPE_ID)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 111
                    self.match(YALPParser.ASSIGN)
                    self.state = 112
                    self.expr(0)


                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 115
                    self.match(YALPParser.COMMA)
                    self.state = 116
                    self.match(YALPParser.OBJECT_ID)
                    self.state = 117
                    self.match(YALPParser.COLON)
                    self.state = 118
                    self.match(YALPParser.TYPE_ID)
                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==31:
                        self.state = 119
                        self.match(YALPParser.ASSIGN)
                        self.state = 120
                        self.expr(0)


                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 128
                self.match(YALPParser.IN)
                self.state = 129
                self.expr(20)
                pass

            elif la_ == 7:
                self.state = 130
                self.match(YALPParser.NEW)
                self.state = 131
                self.match(YALPParser.TYPE_ID)
                pass

            elif la_ == 8:
                self.state = 132
                self.match(YALPParser.ISVOID)
                self.state = 133
                self.expr(18)
                pass

            elif la_ == 9:
                self.state = 134
                self.match(YALPParser.NOT)
                self.state = 135
                self.expr(9)
                pass

            elif la_ == 10:
                self.state = 136
                self.match(YALPParser.NEGATE)
                self.state = 137
                self.expr(8)
                pass

            elif la_ == 11:
                self.state = 138
                self.match(YALPParser.LPAREN)
                self.state = 139
                self.expr(0)
                self.state = 140
                self.match(YALPParser.RPAREN)
                pass

            elif la_ == 12:
                self.state = 142
                self.match(YALPParser.OBJECT_ID)
                pass

            elif la_ == 13:
                self.state = 143
                self.match(YALPParser.TYPE_ID)
                pass

            elif la_ == 14:
                self.state = 144
                self.match(YALPParser.INTEGER)
                pass

            elif la_ == 15:
                self.state = 145
                self.match(YALPParser.STRING)
                pass

            elif la_ == 16:
                self.state = 146
                self.match(YALPParser.TRUE)
                pass

            elif la_ == 17:
                self.state = 147
                self.match(YALPParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 193
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = YALPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 150
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 151
                        self.match(YALPParser.PLUS)
                        self.state = 152
                        self.expr(18)
                        pass

                    elif la_ == 2:
                        localctx = YALPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 153
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 154
                        self.match(YALPParser.MINUS)
                        self.state = 155
                        self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = YALPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 156
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 157
                        self.match(YALPParser.TIMES)
                        self.state = 158
                        self.expr(16)
                        pass

                    elif la_ == 4:
                        localctx = YALPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 159
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 160
                        self.match(YALPParser.DIVIDE)
                        self.state = 161
                        self.expr(15)
                        pass

                    elif la_ == 5:
                        localctx = YALPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 163
                        self.match(YALPParser.MOD)
                        self.state = 164
                        self.expr(14)
                        pass

                    elif la_ == 6:
                        localctx = YALPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 166
                        self.match(YALPParser.LESS_THAN)
                        self.state = 167
                        self.expr(13)
                        pass

                    elif la_ == 7:
                        localctx = YALPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 169
                        self.match(YALPParser.LESS_EQUAL)
                        self.state = 170
                        self.expr(12)
                        pass

                    elif la_ == 8:
                        localctx = YALPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 172
                        self.match(YALPParser.EQUAL)
                        self.state = 173
                        self.expr(11)
                        pass

                    elif la_ == 9:
                        localctx = YALPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 174
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 177
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==19:
                            self.state = 175
                            self.match(YALPParser.SIGN)
                            self.state = 176
                            self.match(YALPParser.TYPE_ID)


                        self.state = 179
                        self.match(YALPParser.DOT)
                        self.state = 180
                        self.match(YALPParser.OBJECT_ID)
                        self.state = 181
                        self.match(YALPParser.LPAREN)
                        self.state = 190
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 27076550930982) != 0):
                            self.state = 182
                            self.expr(0)
                            self.state = 187
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==36:
                                self.state = 183
                                self.match(YALPParser.COMMA)
                                self.state = 184
                                self.expr(0)
                                self.state = 189
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 192
                        self.match(YALPParser.RPAREN)
                        pass

             
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 25)
         




