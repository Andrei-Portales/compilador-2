grammar ThreeAddressCode;

// Reglas del Lexer
CLASS: 'class';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
ASSIGN: '<-';
EQUAL: '=';
NEGATE: '~';
LT: '<';
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
WHITESPACE: [ \t\r\n]+ -> skip;

// Reglas del Parser
program: classDeclaration+ ;

classDeclaration: CLASS IDENTIFIER COLON (globalVarDeclaration | methodDeclaration)* ;

globalVarDeclaration: IDENTIFIER ASSIGN expression SEMI ;

methodDeclaration: IDENTIFIER COLON BEGIN_FUNC NUMBER SEMI instruction* END_FUNC SEMI ;

instruction
    : RETURN expression SEMI
    | IDENTIFIER ASSIGN expression SEMI
    | IDENTIFIER EQUAL expression SEMI
    | IDENTIFIER NEGATE expression SEMI
    | IDENTIFIER LT expression SEMI
    | IFZ IDENTIFIER GOTO IDENTIFIER SEMI
    | PUSH_PARAM IDENTIFIER SEMI
    | POP_PARAMS NUMBER SEMI
    | fCallStatement
    ;

fCallStatement: FCALL IDENTIFIER DOT IDENTIFIER SEMI;

expression
    : IDENTIFIER
    | NUMBER
    | IDENTIFIER OP IDENTIFIER
    ;
