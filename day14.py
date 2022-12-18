import sys


def main():
    input_text = [list(r) for r in open("input14.txt", 'r').read().splitlines()]
    def combineNumbers(inp):
        L = []
        for i in range(len(inp)):
            L.append([])
            c = 0
            f = 0
            j = 0
            while (j < len(inp[i])):
                k = 0
                l = 0
                if f == 0:
                    L[i].append([])
                    f = 1
                if (inp[i][j].isnumeric()):
                    if ((j < (len(inp[i])-1))):
                        if (inp[i][j+1].isnumeric()):
                            if ((j < (len(inp[i])-2))):
                                if (inp[i][j+2].isnumeric()):
                                    tmp = (ord(inp[i][j])-48)*100+(ord(inp[i][j+1])-48)*10+(ord(inp[i][j+2])-48)
                                    L[i][c].append(tmp)
                                    j += 2
                                    k = 1
                                    l = 1
                            if l == 0:
                                tmp = (ord(inp[i][j])-48)*10+(ord(inp[i][j+1])-48)
                                L[i][c].append(tmp)
                                j += 1
                                k = 1
                    if k == 0:
                        tmp = (ord(inp[i][j])-48)
                        L[i][c].append(tmp)
                elif (inp[i][j] == '-' and inp[i][j+1] == '>'):
                    f = 0
                    c += 1
                j += 1
        return L
    numbers_list = combineNumbers(input_text)
    def findBoundaries(inp):
        x, y, a, b = 2**10, 0, 2**10, 0
        for i in range(len(inp)):
            for j in range(len(inp[i])):
                if (inp[i][j][0] < x):
                    x = inp[i][j][0]
                elif (inp[i][j][0] > y):
                    y = inp[i][j][0]
                if (inp[i][j][1] < a):
                    a = inp[i][j][1]
                elif (inp[i][j][1] > b):
                    b = inp[i][j][1]
        return x, y, a, b
    xmin, xmax, ymin, ymax = findBoundaries(numbers_list)
    def createCave(inp, x, y, a, b):
        C = []
        for i in range(b+1):
            C.append([])
            for j in range(x-1, y):
                C[i].append('.')
        for i in range(len(inp)):
            for j in range(len(inp[i])-1):
                startx, starty = inp[i][j][0], inp[i][j][1]
                endx, endy = inp[i][j+1][0], inp[i][j+1][1]
                if (startx == endx):
                    ind = startx%x
                    for k in range(starty, endy+1):
                        C[k][ind] = '#'
                elif (starty == endy):
                    ind = starty
                    for k in range(min(startx%x, endx%x), max(startx%x, endx%x)+1):
                        C[ind][k] = '#'
        return C
    def checkPlacement(a, b):
            if ((a > 20 and a < 40) and (b > 20 and b < 40)):
                print('a')
    def fillCaveSystem(inp, x):
        L = inp.copy()
        count = 0
        f = True
        startx = 500%x
        while(f):
            count += 1
            sx, sy = startx, 0
            while(1):
                if (sy == len(L)-1):
                    f = False
                    break
                elif (L[sy+1][sx] == '.'):
                    sy += 1
                elif (sx == 0):
                    f = False
                    break
                elif (L[sy+1][sx-1] == '.'):
                    sx -= 1
                    sy += 1
                elif (sx == (len(L[0])-1)):
                    f = False
                    break
                elif(L[sy+1][sx+1] == '.'):
                    sx += 1
                    sy += 1
                else:
                    L[sy][sx] = 'o'
                    checkPlacement(sy, sx)
                    break
        for i in range(20, 41):
            print(''.join(L[i][0:31]), '\n')
        return count-1
    cave_system = createCave(numbers_list, xmin, xmax, ymin, ymax)
    for i in range(len(cave_system)):
        print(''.join(cave_system[i]), '\n')
    count = fillCaveSystem(cave_system, xmin)
    print(count)


if __name__ == '__main__':
    sys.exit(main())