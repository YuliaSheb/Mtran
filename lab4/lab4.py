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
int_perem = []
float_perem = []
double_perem = []
boolean_perem = []
char_perem = []
string_perem = []
int_p = r'[0-9+]$'
boolean_true_p = r'true$'
boolean_false_p = r'false$'
double_p = r'[0-9]+[.]{1}[0-9]+$$'
float_p = r'[0-9]*[.]{1}[0-9]+[f{1}]$'
char_p = r'\'[a-zA-Z-_*!@#$%^&()>/.,<=+0-9]\'$'
string_p = r'\"[a-zA-Z-_*!@#$%^&()>/.,<=+0-9]+\"$'
dict_perem = {}
f = open('D://java_not_error.txt', 'r')
text = f.read()
one_word = text.split()
print(text)
f.close()
dat = list(text)

line = 0
for words in types:
    for word in text.split("\n"):
        if words in word and word.split()[0] not in loop:
            i = word.index(words)
            if ("int" in words):
                if ("=" in word):
                    line += 1
                    data = list(word)
                    if data[-2]==" ":
                        #isTrue = re.match(int_p, word.split()[k+1])
                        if ((re.match(int_p, data[-3]) is None) and (re.match(double_p, data[-3]) is None)):
                            out_red("input.c:%d:%d : error: Неверное объявление переменной %s " %(line, 3, word))
                            sys.exit()
                    else :
                        # isTrue = re.match(int_p, word.split()[k+1])
                        if ((re.match(int_p, data[-2]) is None) and (re.match(double_p, data[-2]) is None)):
                            out_red("input.c:%d:%d : error: Неверное объявление переменной %s " % (line, 3, word))
                            sys.exit()
                int_perem.append(word.split()[i])
                dict_perem[word.split()[i]] = "int"
            elif ("float" in words):
                if ("=" in word):
                    line += 1
                    data = list(word)
                    #isTrue = re.match(int_p, word.split()[k+1])
                    if ((re.match(int_p, data[-2]) is None) and (re.match(float_p, data[-2]) is None)):
                        out_red("input.c:%d:%d : error: Неверное объявление переменной float %s = %s " %(line, 3, word.split()[i], word.split()[3]))
                        sys.exit()
                float_perem.append(word.split()[i])
                dict_perem[word.split()[i]] = "float"
            elif ("double" in words):
                if ("=" in word):
                    line += 1
                    data = list(word)
                    #isTrue = re.match(int_p, word.split()[k+1])
                    if ((re.match(int_p, word.split()[3]) is None) and (re.match(float_p, word.split()[3]) is None) and (re.match(double_p, word.split()[3]) is None)):
                        out_red("input.c:%d:%d : error: Неверное объявление переменной float %s = %s " %(line, 3, word.split()[i], word.split()[3]))
                        sys.exit()
                double_perem.append(word.split()[i])
                dict_perem[word.split()[i]] = "double"
            elif ("boolean" in words):
                if ("=" in word):
                    line += 1
                    data = list(word)
                    #isTrue = re.match(int_p, word.split()[k+1])
                    if ((re.match(boolean_true_p, word.split()[3]) is None) and (re.match(boolean_false_p, word.split()[3]) is None)):
                        out_red("input.c:%d:%d : error: Неверное объявление переменной boolean %s = %s " %(line, 3, word.split()[i], word.split()[3]))
                        sys.exit()
                boolean_perem.append(word.split()[i])
                dict_perem[word.split()[i]] = "boolean"
            elif ("char" in words):
                if ("=" in word):
                    line += 1
                    data = list(word)
                    #isTrue = re.match(int_p, word.split()[k+1])
                    if (re.match(char_p, data[-2]) is None):
                        out_red("input.c:%d:%d : error: Неверное объявление переменной %s " %(line, 3, word))
                        sys.exit()
                char_perem.append(word.split()[i])
                dict_perem[word.split()[i]] = "char"
            elif ("string" in words):
                if ("=" in word):
                    line += 1
                    data = list(word)
                    #isTrue = re.match(int_p, word.split()[k+1])
                    if (re.match(string_p, d[-2]) is None):
                        out_red("input.c:%d:%d : error: Неверное объявление переменной string %s = %s " %(line, 3, word.split()[i], word.split()[3]))
                        sys.exit()
                string_perem.append(word.split()[i])
                dict_perem[word.split()[i]] = "string"
            continue

line = 0
for word in text.split("\n"):
    line += 1
    if len(word.split()) > 3:
        if word.split()[1] == "=":
            if word.split()[0] in int_perem:
                if len(word.split()) == 4:
                    if word.split()[2] in int_perem:
                        continue
                    else:
                        out_red("input.c:%d:%d : error: Неверное присваивание переменной %s " % (line, 3, word))
                        sys.exit()
                else:
                    for p in range(len(word.split())):
                        print(p)
                        if p in dict_perem.keys():
                            if p % 2 == 0:
                                if word.split()[p] in int_perem:
                                    continue
                                else:
                                    out_red("input.c:%d:%d : error: Неверное присваивание переменной %s " % (line, 3, word))
                                    sys.exit()
                        else:
                            out_red("input.c:%d:%d : error: Нет переменной %s " % (line, 3, p))
                            sys.exit()
            if word.split()[0] in float_perem:
                if len(word.split()) == 4:
                    if ((word.split()[2] in float_perem) or (word.split()[2] in int_perem)):
                        continue
                    else:
                        out_red("input.c:%d:%d : error: Неверное присваивание переменной %s " % (line, 3, word))
                        sys.exit()
                else:
                    for p in range(len(word.split())):
                        if p % 2 == 0:
                            if (word.split()[p] in int_perem) or (word.split()[p] in float_perem):
                                continue
                            else:
                                out_red("input.c:%d:%d : error: Неверное присваивание переменной %s " % (line, 3, word))
                                sys.exit()
            if word.split()[0] in double_perem:
                if len(word.split()) == 4:
                    if ((word.split()[2] in float_perem) or (word.split()[2] in double_perem) or (word.split()[2] in int_perem)):
                        continue
                    else:
                        out_red("input.c:%d:%d : error: Неверное присваивание переменной %s " % (line, 3, word))
                        sys.exit()
                else:
                    for p in range(len(word.split())):
                        if p % 2 == 0:
                            if (word.split()[p] in double_perem) or (word.split()[p] in float_perem) or (word.split()[p] in int_perem):
                                continue
                            else:
                                out_red("input.c:%d:%d : error: Неверное присваивание переменной %s " % (line, 3, word))
                                sys.exit()
            if word.split()[0] in boolean_perem:
                if len(word.split()) == 4:
                    if (word.split()[2] in boolean_perem):
                        continue
                    else:
                        out_red("input.c:%d:%d : error: Неверное присваивание переменной %s " % (line, 3, word))
                        sys.exit()
            if word.split()[0] in char_perem:
                if len(word.split()) == 4:
                    if (word.split()[2] in char_perem):
                        continue
                    else:
                        out_red("input.c:%d:%d : error: Неверное присваивание переменной %s " % (line, 3, word))
                        sys.exit()
            if word.split()[0] in string_perem:
                if len(word.split()) == 4:
                    if (word.split()[2] in string_perem):
                        continue
                    else:
                        out_red("input.c:%d:%d : error: Неверное присваивание переменной %s " % (line, 3, word))
                        sys.exit()

try:
    input_stream = antlr4.InputStream(text)
    lexer = treeLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = treeParser(stream)
    tree = parser.prog()
except Exception:
    sys.exit()
else:
    print(tree.toStringTree(recog=parser))
