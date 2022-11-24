from CFG2CNF import *
from CYK import *
from simplifierFA import *
from tokenizer import *
import sys

path = "declaretest.js"

terminals, variables, productions = loadCFG("temp.txt")
CNFdict = CFGtoCNF("temp.txt")

simplifiedInput, valid = tokenize(path)

if valid:
    print("Tokenizing done!")
    print(simplifiedInput)
    #for k, v in CNFdict.items():
    #    print(k, v)
    if checkCYK(simplifiedInput, CNFdict):
        print("File accepted")
    else:
        print("Syntax Error")
else:
    print("Tokenizing failure")