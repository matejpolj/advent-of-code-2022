
def isVisibleTop(L, ind, jnd):
    if (ind == 0):
        return 1
    get_height = int(L[ind][jnd])
    for i in range(0, ind):
        if (int(L[i][jnd]) >= get_height):
            return 0
    print("vt", ind, jnd)
    return 1


def isVisibleBottom(L, ind, jnd):
    if (ind == (len(L)-1)):
        return 1
    get_height = int(L[ind][jnd])
    for i in range(ind+1, len(L)):
        if (int(L[i][jnd]) >= get_height):
            return 0
    print("vb", ind, jnd)
    return 1


def isVisibleLeft(L, ind, jnd):
    if (jnd == 0):
        return 1
    get_height = int(L[ind][jnd])
    for j in range(0, jnd):
        if (int(L[ind][j]) >= get_height):
            return 0
    print("vl", ind, jnd)
    return 1


def isVisibleRight(L, ind, jnd):
    if (jnd == (len(L[0])-2)):
        return 1
    get_height = int(L[ind][jnd])
    for j in range(jnd+1, len(L[0])-1):
        if (int(L[ind][j]) >= get_height):
            return 0
    print("vr", ind, jnd)
    return 1

with open('input08.txt') as f:
    lines = f.readlines()
    sum = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])-1):
            if (isVisibleTop(lines, i, j) or isVisibleBottom(lines, i, j) or isVisibleLeft(lines, i, j) or isVisibleRight(lines, i, j)):
                sum  += 1
    print(sum)
