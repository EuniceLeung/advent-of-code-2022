def get_last_four(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
        line = lines[0]
        n = len(line)
        i = 4
        while i < n:
            last_four = line[i-4:i]
            if len(last_four) == len(set(last_four)):
                return i
            i += 1

    return 0


def get_last_fourteen(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
        line = lines[0]
        n = len(line)
        i = 14
        while i < n:
            last_fourteen = line[i-14:i]
            if len(last_fourteen) == len(set(last_fourteen)):
                return i
            i += 1

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = get_last_fourteen('day6data.txt')
    print(result)
