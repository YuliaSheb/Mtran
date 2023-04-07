import re
import sys
import antlr4
from antlr4 import *
from gen import *
from gen.treeLexer import treeLexer
from gen.treeParser import treeParser
from gen.treeListener import treeListener

def out_red(text):
    print("\033[31m {}" .format(text))


keyWords = {"while", "for", "if", "else", "int",
            "float", "break", "continue", "double",
            "array", "false", "true"}
loop = {"while", "for"}
operators = {"+", "-", "*", "/", "%",
             "=", ">", "<", ">=", "<=", "==", "!=",
             "++", "--", "+=", "-=", "*=", "/="}
types = {"int ", "float ", "double ", "boolean ", "char ", "string "}
par = {"(", ")", "{", "}"}
prints = {"System.out.println"}
comment = {"//"}
f = open('D://java_not_error.txt', 'r')
text = f.read()
one_word = text.split()
print(text)
f.close()

line = 0
for word in text.split("\n"):
    line = line+1
    s = word.split()
    if s[-1] != ";" and s[-1] != "{" and s[-1] != "}":
        out_red("input.c:%d:%d : error: expected expression in line :  %s" % (line, len(s)+1, word))
        sys.exit()

line = 0
pos = 0
for word in text.split("\n"):
    line += 1
    pos += 1
    s = word.split()
    if s[0] == "for":
        count = 0
        for x in range(len(s)):
            pos += 1
            if s[x] == ';':
                count += 1
        if count != 2:
            out_red("input.c:%d:%d : error: expected expression \";\" in loop for :  %s" % (line, pos, word))
            sys.exit()

line = 0
pos = 0
for word in text.split("\n"):
    line += 1
    pos = 0
    s = list(word)
    count = 0
    for x in range(len(s)):
        pos += 1
        if s[x] == '\"':
            count += 1
    if count % 2 != 0:
        out_red("input.c:%d:%d : error: expected expression \" in line :  %s" % (line, pos, word))
        sys.exit()

line = 0
pos = 0
rpar = "("
lpar = ")"
count = 0
for word in text.split("\n"):
    line = line + 1
    pos = 0
    count = 0
    s = word.split()
    for letter in s:
        pos = pos + 1
        if letter == rpar:
            count = count + 1
        if letter == lpar:
            count = count - 1
    if count != 0:
        out_red("input.c:%d:%d : warning: invalid syntactic per statement in line :  %s  " % (line, pos, word))
        sys.exit()

input_stream = antlr4.InputStream(text)
lexer = treeLexer(input_stream)
stream = antlr4.CommonTokenStream(lexer)
parser = treeParser(stream)
tree = parser.prog()
print(tree.toStringTree(recog=parser))
