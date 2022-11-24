import re
from simplifierFA import *

def readFile(filename):
    #baca file ke string
    f = open(filename, "r")
    testcase = f.read()
    f.close()

    return testcase

def transformEnters(testcase):
    #ngubah enter jadi newline biar bisa dibaca sama parser
    testcase = testcase.replace("\n", " newline ")
    return testcase

def splitOperators(testcase):
    #split tiap test case jadi ke bentuk array token
    output = []
    testcaseArr = testcase.split(" ")
    for member in testcaseArr:
        if member != '':
            output.append(member)

    #split buat operator
    operator = ['!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\(',
                 r'\)',r'\{', r'\}', r'\[', r'\]', '%', '--', '\\.', '\\++',
                 '\\!', '\\^', '\\&\\&' , '\\|\\|', '\\*\\*']

    counter = 0
    for oper in operator:
        temp = []
        for statement in output:
            elmt = re.split(r'[A..z]*(' + oper + r')[A..z]*', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        output = temp
    
    #split buat sama dengan yang satu dipisahin khusus
    temp = []
    for statement in output:
        if '=' in statement and not '==' in statement:
            elmt = re.split(r'[A..z]*(' + '=' + r')[A..z]*', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)
    output = temp

    #split or yang satu dipisahin khusus
    temp = []
    for statement in output:
        if '|' in statement and not '||' in statement:
            elmt = re.split(r'[A..z]*(' + '\\|' + r')[A..z]*', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)
    output = temp

    #split and yang satu dipisahin khusus
    temp = []
    for statement in output:
        if '&' in statement and not '&&' in statement:
            elmt = re.split(r'[A..z]*(' + '\\&' + r')[A..z]*', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)    
    output = temp

    return output

def simplifyIdNNum(testcase):
    global stateMachine

    commands = ['=','!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-',
                 '(', ')', '{', '}', '[', ']', '%', '--', '+', '*', '**',
                 '\'', '\"',
                 '.', '++','!', '^', '&', '&&' , '|', '||','function',
                 'undefined', 'null', 'return','const', 'var', 'let', 'for',
                 'true', 'false', 'if', 'else', 'throw', 'try', 'catch',
                 'finally', 'while', 'do', 'in', 'of', 'switch', 'case',
                 'default', 'break', 'newline']

    output = []
    for statement in testcase:
        print("\n\nstatement :", statement)
        if statement in commands:
            print("yang masuk:", statement)
            output.append(statement)
        else:
            if number(statement):
                output.append('1')
            elif identifier(statement):
                output.append('a')
            else:
                stateMachine = 0
                break
    return output



if __name__ == "__main__":
    testcase = readFile("test.js")
    testcase = removeComments(testcase)

    if stateMachine == 1:
        testcase = removeStrings(testcase)

        
        if stateMachine == 1:
            testcase = transformEnters(testcase)
            testcase = splitOperators(testcase)

            print("state =", stateMachine)
            testcase = simplifyIdNNum(testcase)
            

    print("\n\ncheckpoint 2\n")
    print(testcase)
    if stateMachine != 0:
        print("sukses")
    else:
         print("gagal")
