import csv

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
    elif (x[0] == "dir"):
        # add subdirectory
        return 4
    else:
        return int(x[0])


def createStructure(L):
    level = 0
    data = 0
    tmp_data = []
    V = []
    for i in range(0, len(L)):
        value = getSplits(L[i])
        if ((value == 1) or (value == 3) or (value == 4)):
            continue
        elif (value == 0):
            level -= 1
        elif (value == 2):
            level += 1
        else:
            tmp = [level, value]
            V.append(tmp)
    return V


def reduceStructure(L):
    for i in range(1, len(L)):
        if (L[i-1][0] == L[i][0]):
            tmp = L[i].pop()
            print(tmp, L[i-1], i)
            L[i-1][1] += tmp


with open('input07.txt') as f:
    lines = f.readlines()
    t = createStructure(lines)
    print(t, t[4])
    reduceStructure(t)
    print(t)
    
