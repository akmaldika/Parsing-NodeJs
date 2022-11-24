
stateMachine = 1 #Kalo statemachine 0 berarti gak valid



def readFile(filename):
    #baca file ke string
    f = open(filename, "r")
    testcase = f.read()
    f.close()

    return testcase

def removeComments(testcase):
    #return yang udah dihilangin komennya
    global stateMachine

    output = ""
    adaKomen = True
    gaadaKomen = True
    while adaKomen:
        try:
            gaadaKomen = False
            index = testcase.index("//")
            output += testcase[0:index]
            testcase = testcase[index:]
            try:
                index = testcase.index("\n")
                testcase = testcase[index:]
            except:
                adaKomen = False
        except:
            if gaadaKomen:
                output = testcase
            else:
                output += testcase
            adaKomen = False

    output2 = ""
    adaKomen = True
    gaadaKomen = True
    while adaKomen:
        try:
            gaadaKomen = False
            index = output.index("/*")
            output2 += output[0:index]
            output = output[index:]
            try:
                index = output.index("*/")
                output = output[index+2:]
            except:
                adaKomen = False
                stateMachine = 0
                break
        except:
            if gaadaKomen:
                output2 = output
            else:
                output2 += output
            adaKomen = False

    return output2

def removeStrings(testcase):
    #return semua string diganti jadi string kosong
    global stateMachine

    output = ""
    adaKomen = True
    gaadaKomen = True
    while adaKomen:
        try:
            gaadaKomen = False
            index = testcase.index("\"")
            output += testcase[0:index] + " \" "
            testcase = testcase[index+1:]
            
            try:
                valid = True
                while valid:
                    index = testcase.index("\"")
                    try:
                        indexEnter = testcase.index("\n")
                        
                        if indexEnter < index:
                            adaKomen = False
                            stateMachine = 0
                            break
                        
                    except:
                        pass

                    if testcase[index-1] == "\\":
                        valid = True
                        testcase = testcase[index+1:]
                    else:
                        valid = False

                testcase = testcase[index+1:]
                output += " \" "
            except:
                adaKomen = False
                stateMachine = 0
        except:
            if gaadaKomen:
                output = testcase
            else:
                output += testcase
            adaKomen = False

    output2 = ""
    adaKomen = True
    gaadaKomen = True
    while adaKomen:
        try:
            gaadaKomen = False
            index = output.index("'")
            output2 += output[0:index] + " ' "
            output = output[index+1:]
            
            try:
                valid = True
                while valid:
                    index = output.index("'")
                    try:
                        indexEnter = output.index("\n")
                        
                        if indexEnter < index:
                            adaKomen = False
                            stateMachine = 0
                            break
                        
                    except:
                        pass

                    if output[index-1] == "\\":
                        valid = True
                        output = output[index+1:]
                    else:
                        valid = False

                output = output[index+1:]
                output2 += " ' "
            except:
                adaKomen = False
                stateMachine = 0
        except:
            if gaadaKomen:
                output2 = output
            else:
                output2 += output
            adaKomen = False

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
