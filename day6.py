
def shiftBuff(L, inp):
    I = []
    print(L, len(L), inp)
    for i in range(1, len(L)):
        I.append(L[i])
    I.append(inp)
    return I


def checkComp(L, inp):
    for i in range(1, len(L)):
        if (L[i] == inp):
            print(len(L)-1-i)
            return (len(L)-i)
    return 0


with open('input06.txt') as f:
    lines = f.readlines()
    lin = lines[0]
    buff = ['', '', '',lin[0]]
    tmp = []
    ind = 0
    i = 1
    while (i < len(lin)):
        print(buff, lin[i], '\n', i)
        ints = checkComp(buff, lin[i])
        print(ints)
        if ((ints == 0) and (i > 3)):
           ind = i
           break
        else:
            tmp = shiftBuff(buff, lin[i]) 
            buff = tmp
            if(i > 0):
                i += ints - 1
        i += 1
        print(i, 'a')
    print(ind)