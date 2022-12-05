with open('input01.txt') as f:
    lines = f.readlines()
    max_cals = [0, 0, 0]
    cur_cals = 0
    for i in range(0, len(lines)):
        if (lines[i] == '\n'):
            if (cur_cals > max_cals[0]):
                max_cals[2] = max_cals[1]
                max_cals[1] = max_cals[0]
                max_cals[0] = cur_cals
            elif (cur_cals > max_cals[1]):
                max_cals[2] = max_cals[1]
                max_cals[1] = cur_cals
            elif (cur_cals > max_cals[2]):
                max_cals[2] = cur_cals
            cur_cals = 0
        else:
            cur_cals += int(lines[i])
    sum_cal = 0
    for i in range(0, len(max_cals)):
        sum_cal += max_cals[i]
    print(sum_cal)
        
