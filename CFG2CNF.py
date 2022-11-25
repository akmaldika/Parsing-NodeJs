newVars = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","B1","B2","B3","B4","B5","B6","B7","B8","B9",
            "C1","C2","C3","C4","C5","C6","C7","C8","C9","D1","D2","D3","D4","D5","D6","D7","D8","D9",
            "E1","E2","E3","E4","E5","E6","E7","E8","E9","F1","F2","F3","F4","F5","F6","F7","F8","F9",
            "G1","G2","G3","G4","G5","G6","G7","G8","G9","H1","H2","H3","H4","H5","H6","H7","H8","H9",
            "I1","I2","I3","I4","I5","I6","I7","I8","I9","J1","J2","J3","J4","J5","J6","J7","J8","J9",
            "K1","K2","K3","K4","K5","K6","K7","K8","K9","L1","L2","L3","L4","L5","L6","L7","L8","L9",
            "M1","M2","M3","M4","M5","M6","M7","M8","M9","N1","N2","N3","N4","N5","N6","N7","N8","N9",
            "O1","O2","O3","O4","O5","O6","O7","O8","O9","P1","P2","P3","P4","P5","P6","P7","P8","P9",
            "Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","R1","R2","R3","R4","R5","R6","R7","R8","R9",
            "S1","S2","S3","S4","S5","S6","S7","S8","S9","T1","T2","T3","T4","T5","T6","T7","T8","T9",
            "U1","U2","U3","U4","U5","U6","U7","U8","U9","V1","V2","V3","V4","V5","V6","V7","V8","V9",
            "W1","W2","W3","W4","W5","W6","W7","W8","W9","X1","X2","X3","X4","X5","X6","X7","X8","X9",
            "Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9","Z1","Z2","Z3","Z4","Z5","Z6","Z7","Z8","Z9"]


def loadCFG(path):
    # I.S. File berbentuk txt dengan format CFG dan mark '~'
    # F.S. tiga array yaitu array yang berisi terminal, variabel, dan production rule yang sudah terpisah untuk tiap or
    file = open(path).read()
    
    productions = []
    variables = []

    tempTerminals = (file.split("\nProductions:\n")[0].replace("Terminals:\n","").replace('\n',' '))
    terminals = tempTerminals.split(" ")
    
    simplify = file.split("\nProductions:\n")[1].replace('\n','').split('~')
    for lines in simplify:
        left = lines.split(' -> ')[0].replace(' ','')
        right = lines.split(' -> ')[1].split(' | ')

        variables.append(left)

        for cases in right:
            productions.append( (left, cases.split(' ')) )
    
    return terminals, variables, productions

def simple(terminals, production):
    # I.S. Menerima array terminal, variabel, dan SATU rule production
    # F.S. Mengembalikan true jika production sudah berbentuk satu terminal saja
    if len(production[1]) == 1 and production[1][0] in terminals:
        return True
    else:
        return False

def unitable(variables, production):
    # I.S. Menerima array terminal, variabel, dan SATU rule production
    # F.S. Mengembalikan true jika production sudah berbentuk satu variable saja
    if len(production[1]) == 1 and production[1][0] in variables:
        return True
    else:
        return False

def unite(variables, productions):
    # I.S. Menerima array variabel dan productions
    # F.S. Mengembalikan array production baru dengan production yang unitable digabungkan
    unitables = []
    newProd = []

    for production in productions:
        if unitable(variables, production):
            unitables.append((production[0], production[1][0]))
        else:
            newProd.append(production)

    for unitabl in unitables:
        for production in productions:
            if unitabl[1] == production[0] and unitabl[0] != production[0]:
                newProd.append( (unitabl[0],production[1]) )

    return newProd

def prodToDict(productions):
    # I.S. Menerima array productions
    # F.S. Mengembalikan dictionary dari array production
    dictionary = {}
    for production in productions:
        if (production[0] in dictionary.keys()):
            dictionary[production[0]].append(production[1])
        else:
            dictionary[production[0]] = []
            dictionary[production[0]].append(production[1])

    return dictionary


def CFGtoCNF(path):
    # I.S. Menerima alamat file grammar yang telah dibuat
    # F.S. Mengembalikan dictionary dari grammar yang telah dibuat dalam bentuk CNF
    global newVars
    # ini fungsi utamanya
    terminals, variables, productions = loadCFG(path)
    additionalVar = newVars

    productions = [('SS', ['MAIN'])] + productions
	

    newProd = []
    for production in productions:
        newProd.append(production)

        #kode di bawah dipake kalo ada terminal nyatu sama non terminal
        #kebetulan grammar rancangan kita dibentuk udah pake konvensi biar gak ada yang campur
        #jadi bisa diskip full
        """
        if simple(terminals, production):
            newProd.append(production)
        else:
            for terminal in terminals:
                for idx, val in enumerate(production[1]):
                    if terminal == val and not (terminal in dictionary):
                        dictionary[terminal] = additionalVar.pop()
                        variables.append(dictionary[terminal])
                        
                        newProd.append( (dictionary[terminal], terminal) )
                        production[1][idx] = dictionary[terminal]
                    elif terminal == val:
                        production[1][idx] = dictionary[terminal]
            newProd.append( (production[0], production[1]) )
        """

    productions = newProd

    #solve yang kanannya banyak non terminal
    newProd2 = []
    for production in productions:
        branching = len(production[1])
        if branching <= 2:
            newProd2.append(production)
        else:
            #branching > 2, ngurangin branching
            newVar = additionalVar.pop(0)
            variables.append(newVar+'1')
            newProd2.append( (production[0], [production[1][0]]+[newVar+'1']) )

            #branching > 3 nyabangin buat tiap varnya
            for i in range(1, branching-2):
                newVar2 = newVar + str(i)
                newVar3 = newVar + str(i+1)
                newProd2.append( (newVar2, [production[1][i], newVar3]) )
            newProd2.append( (newVar + str(branching-2), production[1][branching-2:branching]) )

    productions = newProd2

    #solve yang kanannya cuman single non terminal
    productions = unite(variables, productions)
    done = False
    while not done:
        done = True
        for production in productions:
            if unitable(variables, production):
                productions = unite(variables, productions)
                done = False
                break
    
    dictionary = prodToDict(productions)

    return dictionary

if __name__ == "__main__":
    f = open("cnftest.txt", "w")
    f.write(str(CFGtoCNF("grammar2.txt")).replace(')', '\n'))
