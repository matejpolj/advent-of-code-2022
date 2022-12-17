import sys


def main():
    input_text = [list(r) for r in open("input12.txt", 'r').read().splitlines()]
    sum = 0
    for i in (len(input_text)//3):
        for j in range(max(len(input_text), len(input_text[i+1]))):
            if ((int(input_text[i][j])) and (input_text))

if __name__ == '__main__':
    sys.exit(main())