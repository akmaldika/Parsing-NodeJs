stateMachine = 1

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

    return output2

def removeStrings(testcase):
    #return semua string diganti jadi string kosong
    global stateMachine

    #petik dua
    output = ""
    if stateMachine != 0:
        stateMachine = 3
    while stateMachine > 1 and stateMachine < 4:
        try:
            stateMachine = 2
            index = testcase.index("\"")
            output += testcase[0:index] + " \" "
            testcase = testcase[index+1:]
            try:
                stateMachine = 4
                while stateMachine == 4:
                    index = testcase.index("\"")
                    try:
                        indexEnter = testcase.index("\n")
                        if indexEnter < index:
                            stateMachine = 0
                            break
                    except:
                        pass
                    if testcase[index-1] == "\\":
                        testcase = testcase[index+1:]
                    else:
                        stateMachine = 2
                testcase = testcase[index+1:]
                output += " \" "
            except:
                stateMachine = 0
                break
        except:
            if stateMachine == 3:
                output = testcase
            else:
                output += testcase
            stateMachine = 1

    #petik satu
    output2 = ""
    if stateMachine != 0:
        stateMachine = 3
    while stateMachine > 1 and stateMachine < 4:
        try:
            stateMachine = 2
            index = output.index("'")
            output2 += output[0:index] + " ' "
            output = output[index+1:]
            try:
                stateMachine = 4
                while stateMachine == 4:
                    index = output.index("'")
                    try:
                        indexEnter = output.index("\n")
                        if indexEnter < index:
                            stateMachine = 0
                            break
                    except:
                        pass
                    if output[index-1] == "\\":
                        stateMachine = 4
                        output = output[index+1:]
                    else:
                        stateMachine = 2
                output = output[index+1:]
                output2 += " ' "
            except:
                stateMachine = 0
                break
        except:
            if stateMachine == 3:
                output2 = output
            else:
                output2 += output
            stateMachine = 1
    
    return output2

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

def identifier(string):
    global stateMachine

    stateMachine = 4
    for char in string:
        if stateMachine == 4:
            identifierFirst(char)
        elif stateMachine == 5:
            identifierBody(char)
        elif stateMachine == 0:
            break

    if stateMachine != 0:
        stateMachine = 1
        return True
    else:
        return False

def numberBody(char):
    global stateMachine

    if(ord(char) >= 48 and ord(char) <= 57): #angka
        stateMachine = 6
    else:
        stateMachine = 0

def number(string):
    global stateMachine

    stateMachine = 6
    for char in string:
        if stateMachine == 6:
            numberBody(char)
        elif stateMachine == 0:
            break
        
    if stateMachine != 0:
        stateMachine = 1
        return True
    else:
        return False