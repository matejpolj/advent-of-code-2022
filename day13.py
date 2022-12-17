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
    def compareElement(a, b):
        if (a.isnumeric() and b.isnumeric()):
            return 1
        elif (a == '[' and b == '['):
            return 2
        el
    print(orig_list)

if __name__ == '__main__':
    sys.exit(main())