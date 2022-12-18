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
                if f == 0:
                    L[i].append([])
                    f = 1
                if (inp[i][j].isnumeric()):
                    if ((j < (len(inp[i])-1))):
                        if (inp[i][j+1].isnumeric()):
                            if (inp[i][j+2].isnumeric()):
                                tmp = (ord(inp[i][j])-48)*100+(ord(inp[i][j+1])-48)*10+(ord(inp[i][j+2])-48)
                                L[i][c].append(tmp)
                                j += 2
                                k = 1
                            else:
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
                    
    def createCave(inp):
        C = []
    print(numbers_list)


if __name__ == '__main__':
    sys.exit(main())