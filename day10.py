
def decodeValue(L):
    ins = 0
    value = 0
    if (L[0:4] == "noop"):
        ins = 1
    elif (L[0:4] == "addx"):
        ins = 2
        value = int(L[4:len(L)])
    return ins, value


def neededCycle(c, v):
    if ((c == 20) or (c == 60) or (c == 100) or (c == 140) or (c == 180) or (c == 220)):
        print(v, c)
        return v*c
    else:
        return 0


def runCPU(L):
    cycle = 0
    X = 1
    sum = 0
    for i in range(0, len(L)):
        ins, value = decodeValue(L[i])
        if (ins == 1):
            cycle += 1
            sum += neededCycle(cycle, X)
        elif (ins == 2):
            cycle += 1
            sum += neededCycle(cycle, X)
            cycle += 1
            sum += neededCycle(cycle, X)
            X += value
    return sum

            


with open('input10.txt') as f:
    lines = f.readlines()
    sum = runCPU(lines)
    print(sum)
