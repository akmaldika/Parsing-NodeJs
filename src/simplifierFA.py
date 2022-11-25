import re
import traceback



## stateMachine = 1

## General state
#0: Reject
#1 : Acc

## State buat remove string/comment
#2 : lagi detek stopper beres masuk ke no 3
#3 : masuk ke detektor petik atau komen

## State buat deteksi identifier
#4 : huruf pertama identifier
#5 : deteksi huruf selanjutnya

## State buat deteksi numbers
#6 : detektor angka

def removeComments(testcase):
    #return yang udah dihilangin komennya
    global stateMachine

    #single line
    output = ""
    stateMachine = 3
    while stateMachine > 1 and stateMachine < 4:
        try:
            stateMachine = 2
            index = testcase.index("//")
            output += testcase[0:index]
            testcase = testcase[index:]
            try:
                index = testcase.index("\n")
                testcase = testcase[index:]
            except:
                pass
        except:
            if stateMachine == 3:
                output = testcase
            else:
                output += testcase
            stateMachine = 1

    #multi line
    output2 = ""
    if stateMachine != 0:
        stateMachine = 3
    while stateMachine > 1 and stateMachine < 4:
        try:
            stateMachine = 2
            index = output.index("/*")
            output2 += output[0:index]
            output = output[index:]
            try:
                index = output.index("*/")
                output = output[index+2:]
            except:
                stateMachine = 0
                break
        except:
            if stateMachine == 3:
                output2 = output
            else:
                output2 += output
            stateMachine = 1

    return output2, stateMachine


def removeStrings(testcase):
    #return semua string diganti jadi string kosong
    global stateMachine
    
    elmt = re.split(r'(' + '\\\\"' + r')', testcase)
    
    output = []
    for i in elmt:
        if '"' in i and not '\\"' in i:
            temp2 = re.split(r'(' + '"' + r')', i)
            for j in temp2:
                if j != '':
                    output.append(j)
        else:
            if i != '':
                output.append(i)

    temp = []
    for i in output:
        if '\\\'' in i:
            temp2 = re.split(r'(' + '\\\\\'' + r')', i)
            for j in temp2:
                if j != '':
                    temp.append(j)
        else:
            if i != '':
                temp.append(i)
    output = temp

    temp = []
    for i in output:
        if '\'' in i and not '\\\'' in i:
            temp2 = re.split(r'(' + '\'' + r')', i)
            for j in temp2:
                if j != '':
                    temp.append(j)
        else:
            if i != '':
                temp.append(i)    
    output = temp

    temp = []
    for i in output:
        if '\'' in i and not '\\\'' in i:
            temp2 = re.split(r'(' + '\'' + r')', i)
            for j in temp2:
                if j != '':
                    temp.append(j)
        else:
            if i != '':
                temp.append(i)    
    output = temp

    temp = []
    for i in output:
        j = i.replace('\n', 'NEWLINE')
        temp.append(j)
    output = temp

    temp = []
    for i in output:
        if '\\NEWLINE' in i:
            temp2 = re.split(r'(' + '\\\\NEWLINE' + r')', i)
            for j in temp2:
                if j != '':
                    temp.append(j)
        else:
            if i != '':
                temp.append(i)    
    output = temp

    temp = []
    for i in output:
        if 'NEWLINE' in i and not '\\NEWLINE' in i:
            temp2 = re.split(r'(' + 'NEWLINE' + r')', i)
            for j in temp2:
                if j != '':
                    temp.append(j)
        else:
            if i != '':
                temp.append(i)    
    output = temp

    outputString = ''
    idx = 0
    while idx < len(output):
        if output[idx] == '"':
            outputString += output[idx]
            if idx+1 < len(output):
                idx += 1
                while idx < len(output):
                    if output[idx] == '"':
                        outputString += ' ' + output[idx] + ' '
                        idx += 1
                        break
                    elif idx == len(output)-1 or output[idx] == 'NEWLINE':
                        stateMachine = 0
                        idx = len(output)
                        break
                    else:
                        idx += 1
            else:
                stateMachine = 0
                break

        elif output[idx] == '\'':
            outputString += output[idx]
            if idx+1 < len(output):
                idx += 1
                while idx < len(output):
                    if output[idx] == '\'':
                        outputString += ' ' + output[idx] + ' '
                        idx += 1
                        break
                    elif idx == len(output)-1 or output[idx] == 'NEWLINE':
                        stateMachine = 0
                        idx = len(output)
                        break
                    else:
                        idx += 1
            else:
                stateMachine = 0
                break
        else:
            if output[idx] == 'NEWLINE':
                outputString += '\n'
            else:
                outputString += output[idx]
            idx += 1
    
    outputString += '\n'
    return outputString, stateMachine

##Simplify identifier sama angka
def identifierFirst(char):
    global stateMachine

    if(ord(char) >= 65 and ord(char) <= 90): #huruf besar/underscore/dollarsign
        stateMachine = 5
    elif(ord(char) >= 97 and ord(char) <= 122): #huruf kecil
        stateMachine = 5
    elif(ord(char) == 95): #underscore
        stateMachine = 5
    elif(ord(char) == 36): #dollarsign
        stateMachine = 5
    else:
        stateMachine = 0

    return stateMachine

def identifierBody(char):
    global stateMachine

    if(ord(char) >= 65 and ord(char) <= 90): #huruf besar/underscore/dollarsign
        stateMachine = 5
    elif(ord(char) >= 97 and ord(char) <= 122): #huruf kecil
        stateMachine = 5
    elif(ord(char) == 95): #underscore
        stateMachine = 5
    elif(ord(char) == 36): #dollarsign
        stateMachine = 5
    elif(ord(char) >= 48 and ord(char) <= 57): #angka
        stateMachine = 5
    else:
        stateMachine = 0

    return stateMachine

def identifier(string):
    global stateMachine

    stateMachine = 4
    for char in string:
        if stateMachine == 4:
            stateMachine = identifierFirst(char)
        elif stateMachine == 5:
            stateMachine = identifierBody(char)
        elif stateMachine == 0:
            break

    if stateMachine != 0:
        stateMachine = 1
        return True, stateMachine
    else:
        return False, stateMachine

def numberBody(char):
    global stateMachine

    if(ord(char) >= 48 and ord(char) <= 57): #angka
        stateMachine = 6
    else:
        stateMachine = 0
    
    return stateMachine

def number(string):
    global stateMachine

    stateMachine = 6
    for char in string:
        if stateMachine == 6:
            stateMachine = numberBody(char)
        elif stateMachine == 0:
            break
        
    if stateMachine != 0:
        stateMachine = 1
        return True, stateMachine
    else:
        return False, stateMachine