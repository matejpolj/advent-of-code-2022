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


def getSum(L):
    start_ind = L[0][0]
    sum = L[0][1]
    for i in range(1, len(L)):
        if (L[i][0]<= start_ind):
            return sum
        else:
            sum += L[i][1]
    return sum


def getBiggerThan(L, value):
    tmp = 0
    index = 0
    for i in range(0, len(L)):
        tmp = getSum(L[i:len(L)])
        if (tmp > value):
            continue
        else:
            index += tmp
    return index


def deleteBiggest(L, full, requ):
    total = full - getSum(L)
    cur_max = getSum(L)
    need = requ - total
    print(total, need, getSum(L))
    for i in range(1, len(L)):
        tmp = getSum(L[i:len(L)])
        print(tmp)
        if (tmp < need):
            continue
        else:
            if ((need - tmp) > (need - cur_max)):
                cur_max = tmp
            else:
                continue
    return cur_max


with open('input07.txt') as f:
    lines = f.readlines()
    t = createStructure(lines)
    #i = getBiggerThan(t, 100000)
    i = deleteBiggest(t, 70000000, 30000000)
    #print(t, i)
    print(i)
    
