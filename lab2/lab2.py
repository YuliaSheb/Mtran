import re
import sys


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
print("\n+", "-"*43, "+")
print("|", " "*10, "VARIABLES TABLE", " "*16, "|")
print("+", "-"*43, "+")
for words in types:
    count = 0
    s = []
    for word in text.split("\n"):
        if words in word and word.split()[0] not in loop:
            count = count + 1
            i = word.index(words)
            s.append(word.split()[i+1])
            continue
    if count > 0:
        for i in range(len(s)):
            print("|     %s   |variable of \"%s\" type  "%(s[i], words), " "*7, "|")
print("+", "-"*43, "+")

print("\n+", "-"*43, "+")
print("|", " "*10, "KEY WORDS TABLE", " "*16, "|")
print("+", "-"*43, "+")
for words in keyWords:
    count = 0
    for word in one_word:
        if words == word:
            count = count + 1
    if count > 0:
        print("|   %s    | key word \"%s\"  -- %d             |"%(words, words, count))
print("+", "-"*43, "+")

print("\n+", "-"*43, "+")
print("|", " "*10, "OPERATORS TABLE", " "*16, "|")
print("+", "-"*43, "+")
for words in operators:
    count = 0
    for word in one_word:
        if words == word:
            count = count + 1
            if words == "==":
                n = 2
                test = "is comparison operator"
            elif words == "<=" or words == "++" or words == "--":
                n = 2
                test = "is arithmetic operator"
            else:
                n = 3
                test = "is arithmetic operator"
    if count > 0:
        if words == "==":
            print("|   %s"%(words), " "*n, "|%s  -- %d"%(test, count), " "*5, "|")
        else:
            print("|   %s" % (words), " " * n, "|%s  -- %d" % (test, count), " " * 5, "|")
print("+", "-"*43, "+")

print("\n+", "-"*43, "+")
print("|", " "*10, "CONSTANTS TABLE", " "*16, "|")
print("+", "-"*43, "+")
for words in types:
    count = 0
    s = []
    for word in text.split("\n"):
        if words in word and "=" not in word:
            count = count + 1
            i = word.index(words)
            s.append(word.split()[i+1])
            continue
    if count > 0:
        for i in range(len(s)-1):
            print("|  %s    |const of %s type "%(s[i], words), " "*15, "|")
t = list(set(re.findall(r'\d+', text)))
for i in range(len(t)):
    if len(t[i]) > 1:
        print("|  %s    |int constant  "%(t[i]), " "*20, "|")
    else:
        print("|  %s     |int constant  " % (t[i]), " " * 20, "|")
print("+", "-"*43, "+")

print("\nERROR:")

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
        out_red("input.c:%d:%d : warning: invalid lexical per statement in line :  %s  " % (line, pos, word))
        sys.exit()

line = 0
for word in text.split("\n"):
    line = line+1
    s = word.split()
    if s[-1] != ";" and s[-1] != "{" and s[-1] != "}":
        out_red("input.c:%d:%d : error: expected expression \";\" in line :  %s" % (line, len(s)+1, word.replace(" ", "")))
        sys.exit()

line = 0
pos = 0
for word in text.split("\n"):
    line = line + 1
    pos = 0
    s = word.split()
    for letter in s:
        pos = pos + 1
        if len(letter) >= 2 and letter[0] == "+":
            if letter[1] != "+" or len(letter) != 2:
                out_red("input.c:%d:%d : warning: implicit declaration of \"i++\" in line :  %s  " % (line, pos, word))
                sys.exit()

line = 0
pos = 0
for word in text.split("\n"):
    line = line + 1
    pos = 0
    s = word.split()
    for letter in s:
        pos = pos + 1
        if len(letter) >= 3 and letter[0] == "i":
            if letter[1] != "n" or letter[2] != "t" or len(letter) != 3:
                out_red("input.c:%d:%d : warning: implicit declaration of type \"int\" in line :  %s  " % (line, pos, word))
                sys.exit()
