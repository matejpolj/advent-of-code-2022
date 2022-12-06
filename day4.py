
def findSet(A):
    for i in range(0, len(A)):
        if (A[i] == ','):
            return i


def findDash(A):
    for i in range(0, len(A)):
        if (A[i] == '-'):
            return i


def getRange(A):
    range = findSet(A)
    dif1 = findDash(A[0:range-1])
    dif2 = findDash(A[range-1, len(A)])
    num1 = int(A[0: dif1-1])
    num2 = int(A[dif1: range-1])
    num3 = int(A[range: dif2-1])
    num4 = int(A[dif2: len(A)])
    print(num1, num2, num3, num4)
    return num1, num2, num3, num4


with open('input03.txt') as f:
    lines = f.readlines()
    
