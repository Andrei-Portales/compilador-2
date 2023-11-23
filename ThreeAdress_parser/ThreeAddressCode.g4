grammar ThreeAddressCode;

// Reglas del Lexer
CLASS: 'class';

NUMBER: [0-9]+('.'[0-9]+)?;
SELF: 'self';
STRING: '"' .*? '"';
BOOLEAN: 'true' | 'false';
NULL: 'null';
ASSIGN: '<-';
EQUAL: '=';
NEGATE: '~';
LT: '<';
LT_EQUAL: '<=';
COMPARE: '==';
DOT: '.';
RETURN: 'Return';
BEGIN_FUNC: 'BeginFunc';
END_FUNC: 'EndFunc';
IFZ: 'Ifz';
GOTO: 'Goto';
PUSH_PARAM: 'PushParam';
POP_PARAMS: 'PopParams';
FCALL: 'FCall';
OP: [+\-*/];
SEMI: ';';
COLON: ':';
TEMPORAL: '_t' [0-9]+ ;
LABEL: '_L' [0-9]+ ;
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
WHITESPACE: [ \n\f\r\t]+ -> skip;

// Reglas del Parser
program: classDeclaration+ ;

classDeclaration: CLASS IDENTIFIER COLON (globalVarDeclaration | methodDeclaration)* ;

globalVarDeclaration: IDENTIFIER ASSIGN expression SEMI ;

methodDeclaration: IDENTIFIER COLON BEGIN_FUNC NUMBER SEMI instruction* END_FUNC SEMI ;

instruction
    : 'Return' (expression | SELF) SEMI # returnInstr
    | expression EQUAL expression SEMI # equalInstr
    | expression NEGATE expression SEMI # negateInstr
    | expression LT expression SEMI # ltInstr
    | IFZ expression GOTO LABEL SEMI # ifInstr
    | GOTO LABEL SEMI # gotoInstr
    | PUSH_PARAM expression SEMI # pushParamInstr
    | POP_PARAMS NUMBER SEMI # popParamInstr
    | fCallStatement # fCallInstr
    | LABEL COLON # labelInstr
    ;

fCallStatement: (FCALL IDENTIFIER DOT IDENTIFIER SEMI)|(FCALL IDENTIFIER SEMI);



expression
    : SELF # selfExpr
    | TEMPORAL # tempExpr
    | LABEL # labelExpr
    | IDENTIFIER # idExpr
    | BOOLEAN # boolExpr
    | NULL # nullExpr
    | NUMBER # numberExpr
    | STRING # stringExpr
    | expression OP expression # operatorExpr
    | NEGATE expression # negateExpr
    | expression LT expression # graterThanExpr
    | expression LT_EQUAL expression # graterEqualExpr
    | expression COMPARE expression # comparateExpr
    ;
