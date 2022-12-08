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
    V = [[level, data]]
    for i in range(0, len(L)):
        value = getSplits(L[i])
        if ((value == 1) or (value == 3) or (value == 4)):
            continue
        elif (value == 0):
            V[-1][1] += data
            data = 0
            level -= 1
        elif (value == 2):
            level += 1
            tmp = [level, data]
            V.append(tmp)
            data = 0
        else:
            V[-1][1] += value
    return V


def getBiggerThan(L, value):
    tmp = 0
    index = 0
    for i in range(0, len(L)):
        tmp = 0
        for j in range(i, len(L)):
            if (L[j][0] > L[i][0]):
                tmp += L[j][1]
            if ((tmp + L[j][1]) > value):
                print(tmp, 'o')
                index += 
                tmp = 0
                break
            print(tmp)
        print(index, i)
    return index


with open('input07.txt') as f:
    lines = f.readlines()
    t = createStructure(lines)
    i = getBiggerThan(t, 100000)
    print(t, i)
    
