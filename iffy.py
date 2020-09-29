"""Project name :  If statement training
    File name : iffy.py
    Programmer : Colin B. Chin Choy
"""

param1 = "5"
param2 = 6
param3 = 5
valid = False

def checker (a,b,c):
    if int(a) == int(b) :
        valid = True
        print("param1 and param2 are equal")
        return
    elif int(a) == int(c) :
        valid = True
        print("param1 and param3 are equal")
        return
    elif int(b) == int(c) :
        valid = True
        print("param2 and param3 are equal")
        return


checker(param1, param2, param3)

