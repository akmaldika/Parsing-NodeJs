#algoritma cyk
def checkCYK(testCase, CNFdict):
    #return true kalo STARTSYMBOL ada di paling atas
    #return false kalo engga

    inputLength = len(testCase)
    CYKTable = [[set([]) for i in range(inputLength)] for j in range(inputLength)]

    #https://en.wikipedia.org/wiki/CYK_algorithm
    for i in range(inputLength):
        for rules in CNFdict.items():
            for terminal in rules[1]:
                if len(terminal) == 1 and terminal[0] == testCase[i]:
                    CYKTable[i][i].add(rules[0])
    
    for width in range(2, inputLength + 1):
        for i in range(0, inputLength - width + 1):
            j = i + width - 1
            for start in range(i,j):
                for rules in CNFdict.items():
                    for production in rules[1]:
                        if len(production) == 2:
                            if (production[0] in CYKTable[i][start]) and (production[1] in CYKTable[start+1][j]):
                                CYKTable[i][j].add(rules[0])
    '''
    counter = 1
    for i in CYKTable:
        print(counter)
        for j in i:
            print(j)
        counter += 1
    '''
    
    if 'SS' in CYKTable[0][inputLength-1]:
        return True
    else:
        return False