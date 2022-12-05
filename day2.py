
def getWinner(A, B):
    if ((A == 'A') and (B == 'X')) or ((A == 'B') and (B == 'Y')) or ((A == 'C') and (B == 'Z')):
        return 3
    elif ((A == 'A') and (B == 'Y')) or ((A == 'B') and (B == 'Z')) or ((A == 'C') and (B == 'X')):
        return 6
    else:
        return 0


def getValue(A):
    if (A == 'X'):
        return 1
    elif (A == 'Y'):
        return 2
    elif (A == 'Z'):
        return 3
    else:
        return 0
    

def ultimateWictory(A, B):
    if (B == 'Y'):
        if (A == 'A'):
            return 4
        elif (A == 'B'):
            return 5
        else:
            return 6
    elif (B == 'X'):
        if (A == 'A'):
            return 3
        elif (A == 'B'):
            return 1
        else:
            return 2
    else:
        if (A == 'A'):
            return 8
        elif (A == 'B'):
            return 9
        else:
            return 7


with open('input02.txt') as f:
    lines = f.readlines()
    value = 0
    for i in range(0, len(lines)):
        #value += getValue(lines[i][2]) + getWinner(lines[i][0], lines[i][2])
        value += ultimateWictory(lines[i][0], lines[i][2])
    print(value)