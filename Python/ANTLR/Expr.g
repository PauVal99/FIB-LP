grammar Expr;
root : expr EOF;
expr : expr POT expr
    | expr (MUL|DIV) expr
    | expr (MES|MENYS) expr
    | NUM;

NUM : [0-9]+;

MES : '+';
MENYS : '-';
MUL : '*';
DIV : '/';
POT : '^';

WS : [ \n]+ -> skip;