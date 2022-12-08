
def isVisible(L, ind, jnd):
    get_height = int(L[ind][jnd])
    num = 0
    for i in range(0, len(L)-1):
        if (int(L[i][jnd]) < get_height):
           num += 1
        if (i == ind):
            if (num == (ind-1)):
                return 1 
    for j in range(0, len(L[0])-1):
        if (int(L[ind][j]) < get_height):
            return 1
    return 0


with open('input08.txt') as f:
    lines = f.readlines()
