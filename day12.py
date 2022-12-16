
def getElevation(A):
    if (A == 'S'):
        return 1
    elif (A == 'E'):
        return 26
    else:
        return ord(A)%96


with open('input11.txt') as f:
    lines = f.readlines()
