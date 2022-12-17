import sys


def main():
    input_text = [list(r) for r in open("input13.txt", 'r').read().splitlines()]
    sum = 0
    def convertToList(inp):
        L = []
        for i in range(len(inp)):
            L.append(list(inp[i]))
        return L
    orig_list = convertToList(input_text)
    def cleanList(inp):
        L = []
        i = 0
        while (i < len(inp)):
            L.append([])
            j = 0
            while (j < len(inp[i])):
                if (inp[i][j] == '[' or inp[i][j] == ']'):
                    L[i].append(inp[i][j])
                elif (inp[i][j].isnumeric()):
                    x = ord(inp[i][j]) - 48
                    if (inp[i][j+1].isnumeric()):
                        x *= 10
                        x += ord(inp[i][j+1]) - 48
                        j += 1
                    L[i].append(x)
                j += 1
            i += 1
        N = [x for x in L if x]
        return N
    clean_list = cleanList(orig_list)
    def addPadding(inp):
        L = inp.copy()
        i = 0
        while (i < len(L)):
            j = 0
            while (j < min(len(L[i]), len(L[i+1]))):
                if (L[i+1][j] == '[' and (type(L[i][j]) == int or L[i][j] == ']')):
                    L[i].insert(j, '[')
                    L[i].insert(j+2, ']')
                elif ((type(L[i+1][j]) == int or L[i+1][j] == ']') and L[i][j] == '['):
                    L[i+1].insert(j, '[')
                    L[i+1].insert(j+2, ']')
                j += 1
            i += 2
        return L
    fitted_list = addPadding(clean_list)
    def compareElement(a, b):
        if (type(a) == int and type(b) == int):
            if (a > b):
                return 1
            elif (a < b):
                return 2
            else:
                return 3
        elif (a == '[' and b == '['):
            return 0
        elif (type(a) == int and b == ']'):
            return 1
        elif (a == ']' and type(b) == int):
            return 2
        return 4
    def checkCorrect(inp):
        n = 0
        print( '\n')
        for i in range(0, len(inp), 2):
            up = 0
            down = 0
            for j in range(min(len(inp[i]), len(inp[i+1]))):
                if (inp[i][j] == '['):
                    up += 1
                if (inp[i+1][j] == '['):
                    down += 1
                if (inp[i][j] == ']'):
                    up -= 1
                if (inp[i+1][j] == ']'):
                    down -= 1
                tmp = compareElement(inp[i][j], inp[i+1][j])
                if (inp[i][j] == '[' and inp[i][j+1] == ']' and inp[i+1][j] == '[' and inp[i+1][j+1] == ']'):
                    if (down > up):
                        n += i//2 + 1
                        break
                if (tmp == 1):
                    break
                elif (tmp == 2):
                    n += i//2 + 1
                    break
                else:
                    continue
        return n
    sum = checkCorrect(fitted_list)
    print(sum)

if __name__ == '__main__':
    sys.exit(main())