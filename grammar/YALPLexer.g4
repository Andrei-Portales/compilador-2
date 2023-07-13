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

INHERITS: 'inherits';
LET: 'let';
NEW: 'new';



// ----- OPERATORS -----
DOT: '.';
SIGN: '@';
NEGATE: '~';
ISVOID: 'isvoid';
TIMES: '*';
DIVIDE: '/';
PLUS: '+';
MINUS: '-';
MOD: '%';
LESS_EQUAL: '<=';
LESS_THAN: '<';
EQUAL: '=';
NOT: 'not';
ASSIGN: '<-';
AND: '&&';
OR: '||';



// ----- Punctuation -----
COLON: ':';
SEMICOLON: ';';
COMMA: ',';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRAKE: '[';
RBRAKE: ']';



// ----- Identifiers type tokens -----
TYPE_ID: 'SELF_TYPE' | [A-Z]([A-Za-z] | [0-9] | '_')*;
OBJECT_ID: 'self' | [a-z]([A-Za-z] | [0-9] | '_')*;



// ----- Skip tokens -----
WS: [ \n\f\r\t]+ -> skip;
COMMENT: '--' .*? '\n' -> skip;
LARGE_COMMENT
    :   '(*' .*? '*)' -> skip
    ;
