parser grammar YALPParser;

options {tokenVocab=YALPLexer;}


program:
    (class SEMICOLON)+
;

class:
    CLASS TYPE_ID (INHERITS TYPE_ID)? LBRACE (feature SEMICOLON)* RBRACE
;

feature:
    OBJECT_ID LPAREN (formal (COMMA formal)*)? RPAREN COLON TYPE_ID LBRACE expr RBRACE
  | OBJECT_ID COLON TYPE_ID (ASSIGN expr)?
;

formal:
    OBJECT_ID COLON TYPE_ID
;

expr:
    OBJECT_ID ASSIGN expr
  | expr (SIGN TYPE_ID)? DOT OBJECT_ID LPAREN (expr (COMMA expr)*)? RPAREN 
  | OBJECT_ID LPAREN (expr (COMMA expr)*)? RPAREN
  | IF expr THEN expr ELSE expr FI
  | WHILE expr LOOP expr POOL
  | LBRACE (expr SEMICOLON)+ RBRACE
  | LET OBJECT_ID COLON TYPE_ID (ASSIGN expr)? (COMMA OBJECT_ID COLON TYPE_ID (ASSIGN expr)?)* IN expr
  | NEW TYPE_ID
  | ISVOID expr
  | expr PLUS expr
  | expr MINUS expr
  | expr TIMES expr
  | expr DIVIDE expr
  | expr MOD expr
  | expr LESS_THAN expr
  | expr LESS_EQUAL expr
  | expr EQUAL expr
  | NOT expr
  | NEGATE expr
  | LPAREN expr RPAREN
  | OBJECT_ID
  | TYPE_ID
  | INTEGER
  | STRING
  | TRUE
  | FALSE
;