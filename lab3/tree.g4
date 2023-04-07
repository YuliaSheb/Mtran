grammar tree;

prog:   dec1 | def;

dec1:   funcHeader ';'
    |   type ID ';'
    ;

def :   funcHeader block
    |   type ID ('=' expr)? ';'
    ;

block : '{' stat* '}' ;

stat:  ID ('=' expr)? (simpleOper expr)?';'
    |  'for' '(' type ID ('=' expr)? ' ; ' ID oper expr ' ; ' expr oper (expr)?')' stat
    |  'while' '(' expr ')' stat
    |  type ID (oper expr)? (simpleOper expr)? ';'
    |  'System.out.println' '(' ((vivod)+)? ')' ';'
    |  'return' expr ';'
    |  expr ';'
    |  block
    ;

expr:   '(' expr ')'
    |   ID '(' expr (',' expr)* ')'
    |   ID
    |   INT
    |   CHAR
    ;

type: 'int' | 'char' | 'void' | 'float' | 'double' | 'String' ;

modifier: 'public' | 'protected' | 'private' ;

vivod: ID'+'((quote)+)?(ID)?((quote)+)?('+')? ;

oper: '<=' | '>=' | '<' | '>' | '+=' | '++' | '--' | '-=' | '=' ;

simpleOper: ' + ' | ' - ' | ' * ' | ' / ' | '+' | '-' | '*' | '/';

quote: ' " ' | '"' | ' "' ;

funcHeader : (modifier)? (' static ')? (type) ID '(' args? ')' ;

args: arg (',' arg)*;

arg : type ID ;

COMMENT : '/*' .*? '*/' -> channel (HIDDEN);

WS : [ \t\n\r]+ -> skip ;

ID : [a-zA-Z_]+ [a-zA-Z0-9_]*;

INT : [0-9]+ ;

CHAR : '\' '~'\''+'\'' ;
