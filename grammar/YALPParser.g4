parser grammar YALPParser;

options {tokenVocab=YALPLexer;}


program:
    (class SEMICOLON)+ EOF
;

class:
    CLASS TYPE_ID (INHERITS TYPE_ID)? LBRACE (feature SEMICOLON)* RBRACE
;

feature:
    OBJECT_ID LPAREN (formal (COMMA formal)*)? RPAREN COLON TYPE_ID LBRACE expr RBRACE # MethodFeature
  | OBJECT_ID COLON TYPE_ID (ASSIGN expr)? # VariableFeature
;

formal:
    OBJECT_ID COLON TYPE_ID # MethodParam
;

expr:
    expr TIMES expr # TimesExpr
  | expr DIVIDE expr # DivideExpr
  | expr MOD expr # ModExpr
  | expr PLUS expr # PlusExpr
  | expr MINUS expr # MinusExpr
  | expr EQUAL expr # EqualExpr
  | expr LESS_EQUAL expr # LessEqualExpr
  | expr LESS_THAN expr # LessThanExpr
  | expr AND expr # AndExpr
  | expr OR expr # OrExpr
  | NOT expr # NotExpr
  | NEGATE expr # NegateExpr 

  | INTEGER # IntExpr
  | STRING # StringExpr
  | TRUE # TrueExpr
  | FALSE # FalseExpr
  
  | OBJECT_ID ASSIGN expr # AssignExpr
  | expr (SIGN TYPE_ID)? DOT OBJECT_ID LPAREN (expr (COMMA expr)*)? RPAREN # DotExpr
  | OBJECT_ID LPAREN (expr (COMMA expr)*)? RPAREN # CallExpr
  | IF expr THEN expr ELSE expr FI # IfExpr
  | WHILE expr LOOP expr POOL # WhileExpr
  | LBRACE (expr SEMICOLON)+ RBRACE # BlockExpr
  | LET feature (COMMA feature)* IN expr # LetExpr
  | NEW TYPE_ID # NewExpr
  | ISVOID expr # IsvoidExpr
  | LPAREN expr RPAREN # ParenExpr
  | OBJECT_ID # IdExpr
  | TYPE_ID # TypeExpr
;
