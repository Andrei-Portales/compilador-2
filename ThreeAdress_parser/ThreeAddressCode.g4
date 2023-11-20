grammar ThreeAddressCode;

// Reglas del Lexer
CLASS: 'class';

NUMBER: [0-9]+('.'[0-9]+)?;
STRING: '"' .*? '"';
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
LABEL: '_L' [0-9]+ ;
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
WHITESPACE: [ \n\f\r\t]+ -> skip;

// Reglas del Parser
program: classDeclaration+ ;

classDeclaration: CLASS IDENTIFIER COLON (globalVarDeclaration | methodDeclaration)* ;

globalVarDeclaration: IDENTIFIER ASSIGN expression SEMI ;

methodDeclaration: IDENTIFIER COLON BEGIN_FUNC NUMBER SEMI instruction* END_FUNC SEMI ;

instruction
    : 'Return' expression SEMI # returnInstr
    | IDENTIFIER ASSIGN expression SEMI # assignInstr
    | IDENTIFIER EQUAL expression SEMI # equalInstr
    | IDENTIFIER NEGATE expression SEMI # negateInstr
    | IDENTIFIER LT expression SEMI # ltInstr
    | IFZ IDENTIFIER GOTO LABEL SEMI # ifInstr
    | GOTO LABEL SEMI # gotoInstr
    | PUSH_PARAM IDENTIFIER SEMI # pushParamInstr
    | POP_PARAMS NUMBER SEMI # popParamInstr
    | fCallStatement # fCallInstr
    | LABEL COLON # labelInstr
    ;

fCallStatement: (FCALL IDENTIFIER DOT IDENTIFIER SEMI)|(FCALL IDENTIFIER SEMI);



expression
    : IDENTIFIER
    | NUMBER
    | STRING
    | LABEL
    | (NUMBER|IDENTIFIER) OP (NUMBER|IDENTIFIER)
    | NEGATE (NUMBER|IDENTIFIER)
    | (NUMBER|IDENTIFIER) LT (NUMBER|IDENTIFIER)
    | (NUMBER|IDENTIFIER) LT_EQUAL (NUMBER|IDENTIFIER)
    | (NUMBER|IDENTIFIER) COMPARE (NUMBER|IDENTIFIER)
    ;
