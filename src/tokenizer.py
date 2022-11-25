import re
from src.simplifierFA import *


def readFile(filename):
    # I.S. Menerima alamat dari test file
    # F.S. Mengembalikan string dari test file yang diterima
    f = open(filename, "r")
    testcase = f.read()
    f.close()

    return testcase

def transformEnters(testcase):
    # I.S. Menerima string dari file
    # F.S. Mengembalikan string dengan karakter 'pindah baris' diubah menjadi terminal yang terdapat pada grammar
    testcase = testcase.replace("\n", " newline ")
    return testcase

def splitOperators(testcase):
    # I.S. Menerima string dari file
    # F.S. Mengembalikan array token dengan membagi komponen command serta operator yang terdapat pada string menjadi komponen tersendiri
    output = []
    testcaseArr = testcase.split(" ")
    for member in testcaseArr:
        if member != '':
            output.append(member)

    AssignSwap = ['\\+=', '\\-=', '\\*\\*=', '\\*=', '\\/=', '\\%=', '\\&\\&=', '\\&=', '\\^=', '\\|\\|='
                    ,'\\|=', '\\>\\>\\>=', '\\<\\<=', '\\>\\>=']

    Assigner = ['+=', '-=', '**=', '*=', '/=', '%=', '&&=', '&=', '^=', '||='
                    ,'|=', '>>>=', '<<=', '>>=']

    OpSwap = ['\\>=', '\\<=', '===', '\\!==', '\\!=', '==', '\\>\\>\\>', '\\>\\>', '\\<\\<', '\\^', '\\!',
            '\\+', '\\-', '\\*\\*', '\\*', '\\/', '\\%', '\\<', '\\>', '\\&\\&', '\\&', '\\|\\|', '\\|', '\\=']

    Op = ['>=', '<=', '===', '!==', '!=', '==', '>>>', '>>', '<<', '^', '\\!',
         '**', '*', '/', '%', '<', '>', '&&', '&', '||', '|']

    others = [':', ',','\\.', '\\(', '\\)','\\{', '\\}', '\\[', '\\]','--','\\+\\+', ';', '\\?']

    #split others
    for oper in others:
        temp = []
        for statement in output:
            elmt = re.split(r'(' + oper + r')', statement)
            for splitted in elmt:                
                if splitted != '':
                    temp.append(splitted)
        output = temp

    #split & simplify assign
    for oper in AssignSwap:
        temp = []
        for statement in output:
            elmt = re.split(r'(' + oper + r')', statement)
            for splitted in elmt:           
                if splitted != '':
                    if splitted in Assigner:
                        temp.append('=')
                    else:
                        temp.append(splitted)
        output = temp


    #split & simplify operators
    for oper in OpSwap:
        temp = []
        for statement in output:
            if statement != '++' and statement != '--':
                elmt = re.split(r'(' + oper + r')', statement)
                for splitted in elmt:           
                    if splitted != '':
                        if splitted in Op:
                            temp.append('*')
                        else:
                            temp.append(splitted)
            else:
                temp.append(statement)

        output = temp

    return output

def simplifyIdNNum(testcase):
    # I.S. Menerima array token yang sudah dibagi untuk tiap operator dan command
    # F.S. Mengembalikan array token dengan angka dan identifier diubah menjadi terminal yang terdapat pada grammar
    global stateMachine

    commands = ['+', '-', '*', '$', '.', '(', ')', '{', '}', '[',
                ']', ',', ';', ':', 'NaN', '=', '?', '\"', '\'',
                'function', '++', '--', 'debugger', 'obj',
                'undefined', 'null', 'return','const', 'var', 'let', 'for',
                'true', 'false', 'if', 'else', 'throw', 'try', 'catch',
                'finally', 'while', 'do', 'in', 'of', 'switch', 'case',
                'default', 'break', 'continue', 'delete', 'newline']
    

    output = []
    stateMachine = 1
    for statement in testcase:
        if statement in commands:
            stateMachine = 1
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
    # I.S. Menerima alamat dari test file
    # F.S. Mengembalikan array token dengan komponennya diubah menjadi terminal yang terdapat pada grammar
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

