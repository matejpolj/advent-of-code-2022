
def findValue(A):
    if (A == 'a'):
        return 1
    elif (A == 'b'):
        return 2
    elif (A == 'c'):
        return 3
    elif (A == 'd'):
        return 4
    elif (A == 'e'):
        return 5
    elif (A == 'f'):
        return 6
    elif (A == 'g'):
        return 7
    elif (A == 'h'):
        return 8
    elif (A == 'i'):
        return 9
    elif (A == 'j'):
        return 10
    elif (A == 'k'):
        return 11
    elif (A == 'l'):
        return 12
    elif (A == 'm'):
        return 13
    elif (A == 'n'):
        return 14
    elif (A == 'o'):
        return 15
    elif (A == 'p'):
        return 16
    elif (A == 'q'):
        return 17
    elif (A == 'r'):
        return 18
    elif (A == 's'):
        return 19
    elif (A == 't'):
        return 20
    elif (A == 'u'):
        return 21
    elif (A == 'v'):
        return 22
    elif (A == 'w'):
        return 23
    elif (A == 'x'):
        return 24
    elif (A == 'y'):
        return 25
    elif (A == 'z'):
        return 26   
    elif (A == 'A'):
        return 1+26
    elif (A == 'B'):
        return 2+26
    elif (A == 'C'):
        return 3+26
    elif (A == 'D'):
        return 4+26
    elif (A == 'E'):
        return 5+26
    elif (A == 'F'):
        return 6+26
    elif (A == 'G'):
        return 7+26
    elif (A == 'H'):
        return 8+26
    elif (A == 'I'):
        return 9+26
    elif (A == 'J'):
        return 10+26
    elif (A == 'K'):
        return 11+26
    elif (A == 'L'):
        return 12+26
    elif (A == 'M'):
        return 13+26
    elif (A == 'N'):
        return 14+26
    elif (A == 'O'):
        return 15+26
    elif (A == 'P'):
        return 16+26
    elif (A == 'Q'):
        return 17+26
    elif (A == 'R'):
        return 18+26
    elif (A == 'S'):
        return 19+26
    elif (A == 'T'):
        return 20+26
    elif (A == 'U'):
        return 21+26
    elif (A == 'V'):
        return 22+26
    elif (A == 'W'):
        return 23+26
    elif (A == 'X'):
        return 24+26
    elif (A == 'Y'):
        return 25+26
    elif (A == 'Z'):
        return 26+26
    else:
        return 0


with open('input03.txt') as f:
    lines = f.readlines()
    sum = 0
    i = 0
    #for i in range(0, len(lines)):
    while (i < len(lines)):
        letter = '0'
        flag = 0
#        for j in range(0, int((len(lines[i]))/2)):
#            comp = lines[i][j]
#            for k in range(0, int((len(lines[i]))/2)):
#                if (comp == lines[i][k+int((len(lines[i]))/2)]):
#                    letter = comp
#                    break
        for j in range(0, len(lines[i])):
            letter = lines[i][j]
            if (flag == 1):
                break
            for k in range(0, len(lines[i+1])):
                if (flag == 1):
                    break
                if (letter == lines[i+1][k]):
                    for l in range(0, len(lines[i+2])):
                        if (letter == lines[i+2][l]):
                            flag = 1
                            sum += findValue(letter)
                            break
#        sum += findValue(letter)
        i += 3
    print(sum)    
        