

def loadCFG(path):
    file = open(path).read()
    
    newProd = []
    simplify = file.replace('\n','').split('~')
    for lines in simplify:
        left = lines.split(' -> ')[0].replace(' ','')
        right = lines.split(' -> ')[1].split(' | ')
        for cases in right:
            newProd.append( (left, cases.split(' ')) )
    
    return newProd


def simple():
    pass

def CFGtoCNF(path):
    prod = loadCFG(path)


if __name__ == "__main__":
    print(loadCFG("temp.txt"))