grammar Logo3D;
root: procDef* EOF;

inss: ins*;
ins: (condition | while_ | for_)
    | (input_ | output_ | proc | assign);

input_: '>>' VAR;
output_: '<<' expr;

condition: 'IF' expr 'THEN' inss ('ELSE' inss)? 'END';
while_: 'WHILE' expr 'DO' inss 'END';
for_: 'FOR' VAR 'FROM' expr 'TO' expr 'DO' inss 'END';

COMMA: ',';
PROCNAME: [a-zA-Z][a-zA-Z0-9_]*LP;
procDef: 'PROC' PROCNAME (VAR (COMMA VAR)*)? RP 'IS' inss 'END';
proc: PROCNAME (expr (COMMA expr)*)? RP;

assign: VAR ASSIGN expr;
ASSIGN: ':=';

expr: expr MUL expr #Mul
    | expr DIV expr #Div
    | expr MOD expr #Mod
    | expr SUM expr #Sum
    | expr MIN expr #Min
    | expr GT expr  #Gt
    | expr GET expr #Get
    | expr LT expr  #Lt
    | expr LET expr #Let
    | expr EQ expr  #Eq
    | expr NEQ expr #Neq
    | VAR           #Var
    | NUM           #Num
    | LP expr RP    #Parens;

LP: '(';
RP: ')';

SUM: '+';
MIN: '-';
MUL: '*';
DIV: '/';
MOD: '%';

EQ: '==';
NEQ: '!=';
GT: '>';
LT: '<';
GET: '>=';
LET: '<=';

VAR: [a-zA-Z][a-zA-Z0-9]*;
NUM: '-'?[0-9]+('.'[0-9]+)?;

COMMENT: '//' ~[\r\n]* -> skip;

WS: [ \t\r\n]+ -> skip;