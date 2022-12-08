
def isVisible(L, ind, jnd):
    if ((ind == 0) or (jnd == 0) or (ind == (len(L)-1)) or (jnd == (len(L[0])-1))):
        return 1
    get_height = int(L[ind][jnd])
    num = 0
    for i in range(0, len(L)-1):
        if (int(L[i][jnd]) < get_height):
           num += 1
        if (i == ind):
            if (num == (ind-1)):
                return 1
            num = 0 
    if (num == (len(L)-ind)):
        return 1
    num = 0
    for j in range(0, len(L[0])-1):
        if (int(L[ind][j]) < get_height):
            num += 1
        if (j == jnd):
            if (num == (jnd-1)) :
                return 1
            num = 0
    if (num == (len(L[0])-jnd)):
        return 1
    return 0


with open('input08.txt') as f:
    lines = f.readlines()
    sum = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])-1):
            print(isVisible(lines, i, j), i, j)
            sum  += isVisible(lines, i, j)
    print(sum)
