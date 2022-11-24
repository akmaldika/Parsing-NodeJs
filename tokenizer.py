import re

stateMachine = 1
#stateMachine 0 = Reject
#stateMachine 1 = Acc
#statemachine 2 = lagi detek stopper beres masuk ke no 3
#statemachine 3 = masuk ke detektor petik atau komen

def readFile(filename):
    #baca file ke string
    f = open(filename, "r")
    testcase = f.read()
    f.close()

    return testcase

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
    operator = ['!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\(', r'\)', r'\{', r'\}', r'\[', r'\]', '#', '%', '--', '\\.', '\\++']

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
        counter += 1
        if '=' in statement and not '==' in statement:
            elmt = re.split(r'[A..z]*(' + '=' + r')[A..z]*', statement)
            for splitted in elmt:
                if splitted != '':
                    temp.append(splitted)
        else:
            temp.append(statement)

    output = temp

    return output


if __name__ == "__main__":
    testcase = readFile("test.js")
    testcase = removeComments(testcase)

    if stateMachine == 1:
        testcase = removeStrings(testcase)

        print("\n\ncheckpoint 1\n")
        print(testcase)
        if stateMachine == 1:
            print(testcase)
            testcase = transformEnters(testcase)
            testcase = splitOperators(testcase)

    print("\n\ncheckpoint 2\n")
    print(testcase)
    if stateMachine != 0:
        print("sukses")
    else:
         print("gagal")
