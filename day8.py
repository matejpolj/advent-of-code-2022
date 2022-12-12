
def isVisibleTop(L, ind, jnd):
    if (ind == 0):
        return 1
    get_height = int(L[ind][jnd])
    for i in range(0, ind):
        if (int(L[i][jnd]) >= get_height):
            return 0
    return 1


def isVisibleBottom(L, ind, jnd):
    if (ind == (len(L)-1)):
        return 1
    get_height = int(L[ind][jnd])
    for i in range(ind+1, len(L)):
        if (int(L[i][jnd]) >= get_height):
            return 0
    return 1


def isVisibleLeft(L, ind, jnd):
    if (jnd == 0):
        return 1
    get_height = int(L[ind][jnd])
    for j in range(0, jnd):
        if (int(L[ind][j]) >= get_height):
            return 0
    return 1


def isVisibleRight(L, ind, jnd):
    if (jnd == (len(L[0])-2)):
        return 1
    get_height = int(L[ind][jnd])
    for j in range(jnd+1, len(L[0])-1):
        if (int(L[ind][j]) >= get_height):
            return 0
    return 1


def viewingTop(L, ind, jnd):
    if (jnd == 0):
        return 0
    sum = 0
    get_height = int(L[ind][jnd])
    for i in range(ind-1, -1, -1):
        if (int(L[i][jnd]) < get_height):
            sum += 1
        else:
            sum += 1
            break
    return sum


def viewingBottom(L, ind, jnd):
    if (ind == (len(L)-1)):
        return 0
    sum = 0
    get_height = int(L[ind][jnd])
    for i in range(ind+1, len(L)):
        if (int(L[i][jnd]) < get_height):
            sum += 1
        else:
            sum += 1
            break
    return sum


def viewingLeft(L, ind, jnd):
    if (jnd == 0):
        return 0
    sum = 0
    get_height = int(L[ind][jnd])
    for j in range(jnd-1, -1, -1):
        if (int(L[ind][j]) < get_height):
            sum += 1
        else:
            sum += 1
            break
    return sum


def viewingRight(L, ind, jnd):
    if (jnd == (len(L[0])-2)):
        return 0
    sum = 0
    get_height = int(L[ind][jnd])
    for j in range(jnd+1, len(L[0])-1):
        if (int(L[ind][j]) < get_height):
            sum += 1
        else:
            sum += 1
            break
    return sum


with open('input08.txt') as f:
    lines = f.readlines()
    sum = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])-1):
            if (isVisibleTop(lines, i, j) or isVisibleBottom(lines, i, j) or isVisibleLeft(lines, i, j) or isVisibleRight(lines, i, j)):
                sum  += 1
    print("Sum is:", sum)
    max = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])-1):
                prod = viewingTop(lines, i, j) * viewingBottom(lines, i, j) * viewingLeft(lines, i, j) * viewingRight(lines, i, j)
                if (prod > max):
                    max = prod
    print(max)
