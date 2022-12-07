
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
    I = [[]]
    level = 0
    dire = 0
    


with open('input07.txt') as f:
    lines = f.readlines()
    
