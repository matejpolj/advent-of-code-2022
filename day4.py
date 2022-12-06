
def findSet(A):
    for i in range(0, len(A)):
        if (A[i] == ','):
            return i


def findDash(A):
    for i in range(0, len(A)):
        if (A[i] == '-'):
            return i


def getRange(A):
    rang = findSet(A)
    dif1 = findDash(A[0:(rang-1)])
    dif2 = findDash(A[(rang): len(A)])
    num1 = int(A[0: (dif1)])
    num2 = int(A[dif1+1: (rang)])
    num3 = int(A[rang+1: (dif2+rang)])
    num4 = int(A[dif2+rang+1: len(A)])
    return num1, num2, num3, num4


def compareEnclosement(num1, num2, num3, num4):
    if (((num1 <= num3) and (num2 >= num4)) or ((num1 >= num3) and (num2 <= num4))):
        return 1
    else:
        return 0


def compareOverlapp(num1, num2, num3, num4):
    if (((num1 <= num3) and (num2 >= num4)) or ((num1 >= num3) and (num2 <= num4)) or ((num1 <= num3) and (num2 >= num3)) or ((num1 >= num3) and (num1 <= num4))):
        return 1
    else:
        return 0
        

with open('input04.txt') as f:
    lines = f.readlines()
    sum = 0
    for i in range(0, len(lines)):
        num1, num2, num3, num4 = getRange(lines[i])
#        sum += compareEnclosement(num1, num2, num3, num4)
        sum += compareOverlapp(num1, num2, num3, num4)
    print(sum)
