
def getSplits(L):
    x = L.split()
    if (x[0] == '$'):
        if (x[1] == "cd"):
            if (x[2] == ".."):
                return 0
            elif (x[2] == "/"):
                return 1
            else:
                return 2
        elif (x[1] == "ls"):
            # list stuff
            return 3
    elif (x[0] == dir):
        # add subdirectory
        return 3
    else:
        return int(x[0])
    

def createDirectory(L):
    I = []
    level = 0
    dire = 0
    for i in range(0, len(L)):
        ind = getSplits(L[i])
        if (ind == 1):
            level = 0
        elif (ind == 0):
            level -= 0
        elif (ind == 2):
            level += 1
        elif (ind == 3):



with open('input07.txt') as f:
    lines = f.readlines()
    
