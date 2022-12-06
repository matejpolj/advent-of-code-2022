
def getNumOfCols(L):
    last_char = L[0][0]
    phase = 0
    for i in range(0, len(L)):
        if (phase == 0):
            if (L[i][0] == '['):
                phase = 1
        elif (phase == 1):
            if (L[i][0] == ' '):
                return (int(len(L[i])/4))
        else:
            return 0


def getStart(L):
    last_char = L[0][0]
    phase = 0
    for i in range(0, len(L)):
        if (phase == 0):
            if (L[i][0] == '['):
                phase = 1
        elif (phase == 1):
            if (L[i][0] == ' '):
                return i
        else:
            return 0


def convertToLists(L, num):
    lis = []
    lis_out = []
    for i in range(0, num):
        lis.append([])
        lis_out.append([])
    for i in range(getStart(L)-1, -1, -1):
        for j in range(0, num):
            if (L[i][(j*4)-3] != ' '):
                lis[j].append(L[i][(j*4)-3])
    lis_out[num-1] = lis[0]
    for i in range(0, num-1):
        lis_out[i] = lis[i+1]
    return lis_out


def moveStuff(I, L):
    ind = I.split()
    for i in range(0, int(ind[1])):
        tmp = L[int(ind[3])-1].pop()
        L[int(ind[5])-1].append(tmp)


def moveStuff1(I, L):
    ind = I.split()
    temp = []
    for i in range(0, int(ind[1])):
        tmp = L[int(ind[3])-1].pop()
        temp.append(tmp)
    for i in range(0, int(ind[1])):
        tmp = temp.pop()
        L[int(ind[5])-1].append(tmp)


with open('input05.txt') as f:
    lines = f.readlines()
    stacks = convertToLists(lines, getNumOfCols(lines))
    for i in range(getStart(lines)+2, len(lines)):
#        moveStuff(lines[i], stacks)
        moveStuff1(lines[i], stacks)
    last = []
    for i in range(0, getNumOfCols(lines)):
        last.append(stacks[i][len(stacks[i])-1])
    print("".join(last))

