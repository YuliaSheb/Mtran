import re
import sys
import subprocess

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
f = open('D://java.txt', 'r')
text = f.read()
one_word = text.split()
print(text)
f.close()

for words in types:
    count = 0
    s = []
    for word in text.split("\n"):
        if words in word and word.split()[0] not in loop:
            count = count + 1
            i = word.index(words)
            continue

for words in keyWords:
    count = 0
    for word in one_word:
        if words == word:
            count = count + 1

for words in types:
    count = 0
    s = []
    for word in text.split("\n"):
        if words in word and "=" not in word:
            count = count + 1
            i = word.index(words)
            continue

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

line = 0
for words in types:
    for word in text.split("\n"):
        if words in word and word.split()[0] not in loop:
            i = word.index(words)
            if ("int" in words):
                if ("=" in word):
                    line += 1
                    isTrue = re.match(int_p, word.split()[k+1])
                    if ((re.match(int_p, word.split()[3]) is None) and (re.match(double_p, word.split()[3]) is None)):
                        out_red("input.c:%d:%d : error: Неверное объявление переменной int %s = %s " %(line, 3, word.split()[i], word.split()[3]))
                        sys.exit()
                int_perem.append(word.split()[i])
                dict_perem[word.split()[i]] = "int"
            elif ("float" in words):
                if ("=" in word):
                    line += 1
                    #isTrue = re.match(int_p, word.split()[k+1])
                    if ((re.match(int_p, word.split()[3]) is None) and (re.match(float_p, word.split()[3]) is None)):
                        out_red("input.c:%d:%d : error: Неверное объявление переменной float %s = %s " %(line, 3, word.split()[i], word.split()[3]))
                        sys.exit()
                float_perem.append(word.split()[i])
                dict_perem[word.split()[i]] = "float"
            elif ("double" in words):
                if ("=" in word):
                    line += 1
                    #isTrue = re.match(int_p, word.split()[k+1])
                    if ((re.match(int_p, word.split()[3]) is None) and (re.match(float_p, word.split()[3]) is None) and (re.match(double_p, word.split()[3]) is None)):
                        out_red("input.c:%d:%d : error: Неверное объявление переменной float %s = %s " %(line, 3, word.split()[i], word.split()[3]))
                        sys.exit()
                double_perem.append(word.split()[i])
                dict_perem[word.split()[i]] = "double"
            elif ("boolean" in words):
                if ("=" in word):
                    line += 1
                    isTrue = re.match(int_p, word.split()[k+1])
                    if ((re.match(boolean_true_p, word.split()[3]) is None) and (re.match(boolean_false_p, word.split()[3]) is None)):
                        out_red("input.c:%d:%d : error: Неверное объявление переменной boolean %s = %s " %(line, 3, word.split()[i], word.split()[3]))
                        sys.exit()
                boolean_perem.append(word.split()[i])
                dict_perem[word.split()[i]] = "boolean"
            elif ("char" in words):
                if ("=" in word):
                    line += 1
                    isTrue = re.match(int_p, word.split()[k+1])
                    if (re.match(char_p, word.split()[3]) is None):
                        out_red("input.c:%d:%d : error: Неверное объявление переменной char %s = %s " %(line, 3, word.split()[i], word.split()[3]))
                        sys.exit()
                char_perem.append(word.split()[i])
                dict_perem[word.split()[i]] = "char"
            elif ("string" in words):
                if ("=" in word):
                    line += 1
                    isTrue = re.match(int_p, word.split()[k+1])
                    if (re.match(string_p, word.split()[3]) is None):
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
                        if p % 2 == 0:
                            if word.split()[p] in int_perem:
                                continue
                            else:
                                out_red("input.c:%d:%d : error: Неверное присваивание переменной %s " % (line, 3, word))
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

with open("Main.java", "w") as f:
    f.write(text)

print("\nCompiler :\n")

subprocess.call(['javac', 'Main.java'])
subprocess.call(['java', 'Main'])

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
