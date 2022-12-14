
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
        #print(v, c)
        return v*c
    else:
        return 0

    
def drawPixel(s, c):
    if (((c) == (s)) or ((c) == (s+1)) or ((c) == (s+2))):
        print('#', s, c)
        return '#'
    else:
        print('.', s, c)
        return '.'


def runCPU(L):
    cycle = 0
    X = 2
    sum = 0
    pic = [[]]
    ind = 0
    for i in range(0, len(L)):
        ins, value = decodeValue(L[i])
        if (ins == 1):
            if ((cycle%40) == 0):
                pic.append([])
                ind += 1
            cycle += 1
            sum += neededCycle(cycle, X)
                #print(pic, ind, X)
            #print(ind, pic)
            pic[ind].append(drawPixel(X-1, (cycle%40)))
        elif (ins == 2):
            if ((cycle%40) == 0):
                pic.append([])
                ind += 1
            cycle += 1
            sum += neededCycle(cycle, X)
                #print(pic, ind, X)
            pic[ind].append(drawPixel(X-1, (cycle%40)))
            if ((cycle%40) == 0):
                pic.append([])
                ind += 1
            cycle += 1
            sum += neededCycle(cycle, X)
                #print(pic, ind, X)
            pic[ind].append(drawPixel(X-1, (cycle%40)))
            X += value
    return sum, pic


with open('input10.txt') as f:
    lines = f.readlines()
    sum, pic = runCPU(lines)
    print(sum)
    l = []
    for i in range(0, len(pic)):
        l.append(''.join(pic[i]))
        print(''.join(pic[i]), len(pic[i]))