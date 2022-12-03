def count_calories(input_file):
    with open(input_file) as f:
        max_cal = 0
        cur_cal = 0
        lines = f.readlines()
        for line in lines:
            if line.rstrip(): # line not empty
                cur_cal += int(line)
            else:
                max_cal = max(max_cal, cur_cal)
                cur_cal = 0

    return max_cal


def count_calories2(input_file):
    with open(input_file) as f:
        cals = []
        cur_cal = 0
        lines = f.readlines()
        for line in lines:
            if line.rstrip(): # line not empty
                cur_cal += int(line)
            else:
                cals.append(cur_cal)
                cur_cal = 0

    cals.sort(reverse=True)
    return cals[0] + cals[1] + cals[2]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = count_calories2('day1data.txt')
    print(result)
