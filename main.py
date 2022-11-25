from CFG2CNF import *
from CYK import *
from simplifierFA import *
from tokenizer import *
import sys
import time

path = "test.js"

CNFdict = CFGtoCNF("grammar2.txt")

simplifiedInput, valid = tokenize(path)

startTime = time.time()
if valid:
    print("Tokenizing done!")
    print(simplifiedInput)
    #for k, v in CNFdict.items():
    #    print(k, v)
    if len(simplifiedInput) == 0:
        print("File accepted")
    elif checkCYK(simplifiedInput, CNFdict):
        print("File accepted")
    else:
        print("Syntax Error")
else:
    print("Tokenizing failure")

finishTime = time.time() - startTime
print("Relative length : ", len(simplifiedInput))
print(finishTime)