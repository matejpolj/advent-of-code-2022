
def shiftBuff(L, inp):
    I = []
    for i in range(1, len(L)):
        I.append(L[i])
    I.append(inp)
    return I


def checkComp(L, inp):
    for i in range(1, len(L)):
        if (L[i] == inp):
            return 1
    return 0


def checkInBuf(L):
    for i in range(0, len(L)):
        for j in range(i+1, len(L)):
            if (L[i] == L[j]):
                return 1
    return 0


with open('input06.txt') as f:
    lines = f.readlines()
    lin = lines[0]
    buff = [lin[0], lin[1], lin[2], lin[3], lin[4], lin[5], lin[6], lin[7], lin[8], lin[9], lin[10], lin[11], lin[12], lin[13]]
    tmp = []
    ind = 0
    for i in range(14, len(lin)):
        if ((checkInBuf(buff) == 0)):
           ind = i
           break
        else:
            tmp = shiftBuff(buff, lin[i]) 
            buff = tmp
    print(ind)
