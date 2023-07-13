lexer grammar YALPLexer;


// ----- Tokens -----
INTEGER: [0-9]+;
STRING: '"' .*? '"';
ANY: '_';

// ----- Reserved words -----
CLASS: 'class';

IF: 'if';
THEN: 'then';
ELSE: 'else';
FI: 'fi';

WHILE: 'while';
LOOP: 'loop';
POOL: 'pool';

TRUE: 'true';
FALSE: 'false';

IN: 'in';
NOT: 'not';

INHERITS: 'inherits';
ISVOID: 'isvoid';
LET: 'let';
NEW: 'new';
SIGN: '@';



// ----- Identifiers type tokens -----
TYPE_ID: 'SELF_TYPE' | [A-Z]([A-Za-z] | [0-9] | '_')*;
OBJECT_ID: 'self' | [a-z]([A-Za-z] | [0-9] | '_')*;



// ----- Operators -----
PLUS: '+';
MINUS: '-';
TIMES: '*';
DIVIDE: '/';
MOD: '%';

LESS_THAN: '<';
LESS_EQUAL: '<=';
EQUAL: '=';
AND: '&&';
OR: '||';
NEGATE: '~';

ASSIGN: '<-';
COLON: ':';
SEMICOLON: ';';
DOT: '.';
COMMA: ',';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRAKE: '[';
RBRAKE: ']';



// ----- Skip tokens -----
WS: [ \n\f\r\t]+ -> skip;
COMMENT: '--' .*? '\n' -> skip;
LARGE_COMMENT
    :   '(*' .*? '*)' -> skip
    ;
