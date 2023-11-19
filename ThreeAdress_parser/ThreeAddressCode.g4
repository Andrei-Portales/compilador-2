grammar ThreeAddressCode;

// Reglas del Lexer
CLASS: 'class';

NUMBER: [0-9]+('.'[0-9]+)?;
ASSIGN: '<-';
EQUAL: '=';
NEGATE: '~';
LT: '<';
LT_EQUAL: '<=';
COMPARE: '==';
DOT: '.';
RETURN: 'Return';
BEGIN_FUNC: 'BeginFunc 0';
END_FUNC: 'EndFunc';
IFZ: 'Ifz';
GOTO: 'Goto';
PUSH_PARAM: 'PushParam';
POP_PARAMS: 'PopParams';
FCALL: 'FCall';
OP: [+\-*/];
SEMI: ';';
COLON: ':';
LABEL: '_L' [0-9]+ ;
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
WHITESPACE: [ \n\f\r\t]+ -> skip;

// Reglas del Parser
program: classDeclaration+ ;

classDeclaration: CLASS IDENTIFIER COLON (globalVarDeclaration | methodDeclaration)* ;

globalVarDeclaration: IDENTIFIER ASSIGN expression SEMI ;

methodDeclaration: IDENTIFIER COLON BEGIN_FUNC SEMI instruction* END_FUNC SEMI ;

instruction
    : 'Return' expression SEMI
    | IDENTIFIER ASSIGN expression SEMI
    | IDENTIFIER EQUAL expression SEMI
    | IDENTIFIER NEGATE expression SEMI
    | IDENTIFIER LT expression SEMI
    | IFZ IDENTIFIER GOTO LABEL SEMI
    | GOTO LABEL SEMI
    | PUSH_PARAM IDENTIFIER SEMI
    | POP_PARAMS NUMBER SEMI
    | fCallStatement
    | LABEL COLON
    ;

fCallStatement: (FCALL IDENTIFIER DOT IDENTIFIER SEMI)|(FCALL IDENTIFIER SEMI);



expression
    : IDENTIFIER
    | NUMBER
    | LABEL
    | (NUMBER|IDENTIFIER) OP (NUMBER|IDENTIFIER)
    | NEGATE (NUMBER|IDENTIFIER)
    | (NUMBER|IDENTIFIER) LT (NUMBER|IDENTIFIER)
    | (NUMBER|IDENTIFIER) LT_EQUAL (NUMBER|IDENTIFIER)
    | (NUMBER|IDENTIFIER) COMPARE (NUMBER|IDENTIFIER)
    ;
