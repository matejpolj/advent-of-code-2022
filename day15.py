import sys


def main():
    input_text = [r for r in open("input15.txt", 'r').read().splitlines()]
    fixed_text = []
    for i in range(len(input_text)):
        fixed_text.append(input_text[i].split(" "))
    clean_numbers = []
    for i in range(len(fixed_text)):
        clean_numbers.append([])
        clean_numbers[i].append(int(fixed_text[i][2][2:len(fixed_text[i][2])-1]))
        clean_numbers[i].append(int(fixed_text[i][3][2:len(fixed_text[i][3])-1]))
        clean_numbers[i].append(int(fixed_text[i][8][2:len(fixed_text[i][8])-1]))
        clean_numbers[i].append(int(fixed_text[i][9][2:len(fixed_text[i][9])]))
    num = []
    for i in range(len(clean_numbers)):
        dif = abs(clean_numbers[i][0] - clean_numbers[i][2]) + abs(clean_numbers[i][1] - clean_numbers[i][3])
        rem = dif - abs(clean_numbers[i][1]-10)
        if (rem > 0):
            for j in range(-rem, rem, 1):  
                #print(i, j, rem, dif, clean_numbers[i])
                print(i)
                if (num.count(j+clean_numbers[i][0]) == 0):
                    num.append(j+clean_numbers[i][0])
    print(input_text, fixed_text, clean_numbers, len(num), num)


if __name__ == '__main__':
    sys.exit(main())