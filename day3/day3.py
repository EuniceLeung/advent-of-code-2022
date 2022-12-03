import math


def sum_priorities(input_file):
    with open(input_file) as f:
        lines = f.readlines()
        total = 0

        for line in lines:
            m = math.floor(len(line)/2) # len(line)//2
            first_half, second_half = line[:m], line[m:]
            first_set = set(first_half)
            second_set = set(second_half)
            diff = first_set.intersection(second_set).pop()

            # A = 65 -> 27, a = 97 -> 1
            if diff == diff.lower():
                total += ord(diff) - 96
            else:
                total += ord(diff) - 38

    return total


def sum_priorities2(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
        total = 0

        for i in range(0, len(lines), 3):
            elf1, elf2, elf3 = lines[i], lines[i+1], lines[i+2]

            set1 = set(elf1)
            set2 = set(elf2)
            set3 = set(elf3)
            same12 = set1.intersection(set2)
            same = same12.intersection(set3).pop()

            # A = 65 -> 27, a = 97 -> 1
            if same == same.lower():
                total += ord(same) - 96
            else:
                total += ord(same) - 38

    return total


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = sum_priorities2('day3data.txt')
    print(result)
