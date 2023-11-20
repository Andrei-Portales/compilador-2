# Generated from ThreeAdress_parser/ThreeAddressCode.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,27,212,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,1,0,1,0,1,0,1,0,1,0,1,0,1,1,4,1,63,8,1,11,1,12,1,64,1,1,
        1,1,4,1,69,8,1,11,1,12,1,70,3,1,73,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,
        3,5,3,82,8,3,10,3,12,3,85,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,98,8,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,
        1,9,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,23,4,23,187,
        8,23,11,23,12,23,188,1,24,1,24,1,24,1,24,4,24,195,8,24,11,24,12,
        24,196,1,25,1,25,5,25,201,8,25,10,25,12,25,204,9,25,1,26,4,26,207,
        8,26,11,26,12,26,208,1,26,1,26,1,83,0,27,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,
        35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,1,0,
        5,1,0,48,57,3,0,42,43,45,45,47,47,3,0,65,90,95,95,97,122,4,0,48,
        57,65,90,95,95,97,122,3,0,9,10,12,13,32,32,220,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,
        0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,
        0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,
        0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,
        0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,
        0,0,1,55,1,0,0,0,3,62,1,0,0,0,5,74,1,0,0,0,7,79,1,0,0,0,9,97,1,0,
        0,0,11,99,1,0,0,0,13,102,1,0,0,0,15,104,1,0,0,0,17,106,1,0,0,0,19,
        108,1,0,0,0,21,111,1,0,0,0,23,114,1,0,0,0,25,116,1,0,0,0,27,123,
        1,0,0,0,29,133,1,0,0,0,31,141,1,0,0,0,33,145,1,0,0,0,35,150,1,0,
        0,0,37,160,1,0,0,0,39,170,1,0,0,0,41,176,1,0,0,0,43,178,1,0,0,0,
        45,180,1,0,0,0,47,182,1,0,0,0,49,190,1,0,0,0,51,198,1,0,0,0,53,206,
        1,0,0,0,55,56,5,99,0,0,56,57,5,108,0,0,57,58,5,97,0,0,58,59,5,115,
        0,0,59,60,5,115,0,0,60,2,1,0,0,0,61,63,7,0,0,0,62,61,1,0,0,0,63,
        64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,72,1,0,0,0,66,68,5,46,
        0,0,67,69,7,0,0,0,68,67,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,
        1,0,0,0,71,73,1,0,0,0,72,66,1,0,0,0,72,73,1,0,0,0,73,4,1,0,0,0,74,
        75,5,115,0,0,75,76,5,101,0,0,76,77,5,108,0,0,77,78,5,102,0,0,78,
        6,1,0,0,0,79,83,5,34,0,0,80,82,9,0,0,0,81,80,1,0,0,0,82,85,1,0,0,
        0,83,84,1,0,0,0,83,81,1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,86,87,
        5,34,0,0,87,8,1,0,0,0,88,89,5,116,0,0,89,90,5,114,0,0,90,91,5,117,
        0,0,91,98,5,101,0,0,92,93,5,102,0,0,93,94,5,97,0,0,94,95,5,108,0,
        0,95,96,5,115,0,0,96,98,5,101,0,0,97,88,1,0,0,0,97,92,1,0,0,0,98,
        10,1,0,0,0,99,100,5,60,0,0,100,101,5,45,0,0,101,12,1,0,0,0,102,103,
        5,61,0,0,103,14,1,0,0,0,104,105,5,126,0,0,105,16,1,0,0,0,106,107,
        5,60,0,0,107,18,1,0,0,0,108,109,5,60,0,0,109,110,5,61,0,0,110,20,
        1,0,0,0,111,112,5,61,0,0,112,113,5,61,0,0,113,22,1,0,0,0,114,115,
        5,46,0,0,115,24,1,0,0,0,116,117,5,82,0,0,117,118,5,101,0,0,118,119,
        5,116,0,0,119,120,5,117,0,0,120,121,5,114,0,0,121,122,5,110,0,0,
        122,26,1,0,0,0,123,124,5,66,0,0,124,125,5,101,0,0,125,126,5,103,
        0,0,126,127,5,105,0,0,127,128,5,110,0,0,128,129,5,70,0,0,129,130,
        5,117,0,0,130,131,5,110,0,0,131,132,5,99,0,0,132,28,1,0,0,0,133,
        134,5,69,0,0,134,135,5,110,0,0,135,136,5,100,0,0,136,137,5,70,0,
        0,137,138,5,117,0,0,138,139,5,110,0,0,139,140,5,99,0,0,140,30,1,
        0,0,0,141,142,5,73,0,0,142,143,5,102,0,0,143,144,5,122,0,0,144,32,
        1,0,0,0,145,146,5,71,0,0,146,147,5,111,0,0,147,148,5,116,0,0,148,
        149,5,111,0,0,149,34,1,0,0,0,150,151,5,80,0,0,151,152,5,117,0,0,
        152,153,5,115,0,0,153,154,5,104,0,0,154,155,5,80,0,0,155,156,5,97,
        0,0,156,157,5,114,0,0,157,158,5,97,0,0,158,159,5,109,0,0,159,36,
        1,0,0,0,160,161,5,80,0,0,161,162,5,111,0,0,162,163,5,112,0,0,163,
        164,5,80,0,0,164,165,5,97,0,0,165,166,5,114,0,0,166,167,5,97,0,0,
        167,168,5,109,0,0,168,169,5,115,0,0,169,38,1,0,0,0,170,171,5,70,
        0,0,171,172,5,67,0,0,172,173,5,97,0,0,173,174,5,108,0,0,174,175,
        5,108,0,0,175,40,1,0,0,0,176,177,7,1,0,0,177,42,1,0,0,0,178,179,
        5,59,0,0,179,44,1,0,0,0,180,181,5,58,0,0,181,46,1,0,0,0,182,183,
        5,95,0,0,183,184,5,116,0,0,184,186,1,0,0,0,185,187,7,0,0,0,186,185,
        1,0,0,0,187,188,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,48,1,
        0,0,0,190,191,5,95,0,0,191,192,5,76,0,0,192,194,1,0,0,0,193,195,
        7,0,0,0,194,193,1,0,0,0,195,196,1,0,0,0,196,194,1,0,0,0,196,197,
        1,0,0,0,197,50,1,0,0,0,198,202,7,2,0,0,199,201,7,3,0,0,200,199,1,
        0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,52,1,0,
        0,0,204,202,1,0,0,0,205,207,7,4,0,0,206,205,1,0,0,0,207,208,1,0,
        0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,211,6,26,
        0,0,211,54,1,0,0,0,10,0,64,70,72,83,97,188,196,202,208,1,6,0,0
    ]

class ThreeAddressCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CLASS = 1
    NUMBER = 2
    SELF = 3
    STRING = 4
    BOOLEAN = 5
    ASSIGN = 6
    EQUAL = 7
    NEGATE = 8
    LT = 9
    LT_EQUAL = 10
    COMPARE = 11
    DOT = 12
    RETURN = 13
    BEGIN_FUNC = 14
    END_FUNC = 15
    IFZ = 16
    GOTO = 17
    PUSH_PARAM = 18
    POP_PARAMS = 19
    FCALL = 20
    OP = 21
    SEMI = 22
    COLON = 23
    TEMPORAL = 24
    LABEL = 25
    IDENTIFIER = 26
    WHITESPACE = 27

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'self'", "'<-'", "'='", "'~'", "'<'", "'<='", "'=='", 
            "'.'", "'Return'", "'BeginFunc'", "'EndFunc'", "'Ifz'", "'Goto'", 
            "'PushParam'", "'PopParams'", "'FCall'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "CLASS", "NUMBER", "SELF", "STRING", "BOOLEAN", "ASSIGN", "EQUAL", 
            "NEGATE", "LT", "LT_EQUAL", "COMPARE", "DOT", "RETURN", "BEGIN_FUNC", 
            "END_FUNC", "IFZ", "GOTO", "PUSH_PARAM", "POP_PARAMS", "FCALL", 
            "OP", "SEMI", "COLON", "TEMPORAL", "LABEL", "IDENTIFIER", "WHITESPACE" ]

    ruleNames = [ "CLASS", "NUMBER", "SELF", "STRING", "BOOLEAN", "ASSIGN", 
                  "EQUAL", "NEGATE", "LT", "LT_EQUAL", "COMPARE", "DOT", 
                  "RETURN", "BEGIN_FUNC", "END_FUNC", "IFZ", "GOTO", "PUSH_PARAM", 
                  "POP_PARAMS", "FCALL", "OP", "SEMI", "COLON", "TEMPORAL", 
                  "LABEL", "IDENTIFIER", "WHITESPACE" ]

    grammarFileName = "ThreeAddressCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


