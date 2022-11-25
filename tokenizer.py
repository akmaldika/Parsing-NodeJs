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
    operator = ['!==', '===', '>=', '<=', ':', ',', '/', '\\.', '\\(',
                 '\\)','\\{', '\\}', '\\[', '\\]', '%', '--', '\\.', '\\++',
                 '\\!', '\\^', '\\&\\&' , '\\|\\|', '\\*\\*', ';', '\\?',
                 '\\>\\>\\>', '\\<\\<']

    for oper in operator:
        temp = []
        for statement in output:
            elmt = re.split(r'(' + oper + r')', statement)
            for splitted in elmt:                
                if splitted != '':
                    temp.append(splitted)
        output = temp

    #split buat sama dengan yang dua dipisahin khusus
    temp = []
    for statement in output:
        if '==' in statement and not '===' in statement and not '!==' in statement:
            elmt = re.split(r'(' + '==' + r')', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)
    output = temp

    #split buat tidak sama dengan satu dipisahin khusus
    temp = []
    for statement in output:
        if '!=' in statement and not '==' in statement:
            elmt = re.split(r'(' + '!=' + r')', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)
    output = temp

    #split buat sama dengan yang satu dipisahin khusus
    temp = []
    for statement in output:
        if '=' in statement and not '==' in statement and not '!=' in statement and not '>=' in statement and not '<=' in statement:
            elmt = re.split(r'(' + '=' + r')', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)
    output = temp

    #split lebih besar dipisahin khusus
    temp = []
    for statement in output:
        if '>>' in statement and not '>>>' in statement:
            elmt = re.split(r'(' + '\\>\\>' + r')', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)
    output = temp

    #split lebih besar dipisahin khusus
    temp = []
    for statement in output:
        if '>' in statement and not '>=' in statement and not '>>' in statement:
            elmt = re.split(r'(' + '\\>' + r')', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)
    output = temp

    #split lebih kecil dipisahin khusus
    temp = []
    for statement in output:
        if '<' in statement and not '<=' in statement and not '<<' in statement:
            elmt = re.split(r'(' + '\\<' + r')', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)
    output = temp

    #split kali dipisahin khusus
    temp = []
    for statement in output:
        if '*' in statement and not '**' in statement:
            elmt = re.split(r'(' + '\\*' + r')', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)
    output = temp

    #split tambah dipisahin khusus
    temp = []
    for statement in output:
        if '+' in statement and not '+' in statement:
            elmt = re.split(r'(' + '\\*' + r')', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)
    output = temp

    #split kurang dipisahin khusus
    temp = []
    for statement in output:
        if '-' in statement and not '-' in statement:
            elmt = re.split(r'(' + '\\-' + r')', statement)
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
            elmt = re.split(r'(' + '\\|' + r')', statement)
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
            elmt = re.split(r'(' + '\\&' + r')', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)    
    output = temp

    return output

def simplifyIdNNum(testcase):
    #ngubah identifier sama angka jadi a sama 1 doang
    global stateMachine

    commands = ['+', '-', '*', '**', '/', '%', '<', '<=', '>', '>=', '==',
                '&', '&&', '|', '||', '$', '.', '!', '(', ')', '{', '}', '[',
                ']', ',', ';', ':', 'NaN', '=', '?', '===', '!==', '\"', '\'',
                'function', '++', '--', 'debugger', 'obj', '<<', '>>>', '>>'
                'undefined', 'null', 'return','const', 'var', 'let', 'for',
                'true', 'false', 'if', 'else', 'throw', 'try', 'catch',
                'finally', 'while', 'do', 'in', 'of', 'switch', 'case',
                'default', 'break', 'continue', 'delete', 'newline']
    

    output = []
    stateMachine = 1
    for statement in testcase:
        #buat debugging pake print ini oke bet
        ###print("\n\nstatement :", statement)
        if statement in commands:
            output.append(statement)
        else:
            if number(statement)[0]:
                stateMachine = number(statement)[1]
                output.append('1')
            elif identifier(statement)[0]:
                stateMachine = identifier(statement)[1]
                output.append('a')
            else:
                stateMachine = 0
                break
    return output, stateMachine


def tokenize(path):
    testcase = readFile(path)
    testcase, stateMachine = removeComments(testcase)
    if stateMachine == 1:
        testcase, stateMachine = removeStrings(testcase)
        if stateMachine == 1:
            testcase = transformEnters(testcase)
            testcase = splitOperators(testcase)
            testcase, stateMachine = simplifyIdNNum(testcase)
    if stateMachine != 0:
        return testcase, True
    else:
        return testcase, False


if __name__ == "__main__":
    testcase = readFile("test.js")
    testcase, stateMachine = removeComments(testcase)

    if stateMachine == 1:
    
        testcase, stateMachine = removeStrings(testcase)
        print(stateMachine)

        if stateMachine == 10000:
            testcase = transformEnters(testcase)
            testcase = splitOperators(testcase)
            testcase = simplifyIdNNum(testcase)
            print(testcase)
            

    print("\n\ncheckpoint\n")
    
    if stateMachine != 0:
        print("sukses")
    else:
         print("gagal")
