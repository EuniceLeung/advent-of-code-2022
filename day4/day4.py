def count_full_overlap(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
        count = 0

        for line in lines:
            elf1, elf2 = line.split(sep=',')
            start1, end1 = elf1.split(sep='-')
            start2, end2 = elf2.split(sep='-')

            start1 = int(start1)
            end1 = int(end1)
            start2 = int(start2)
            end2 = int(end2)

            if (start1 <= start2 and end1 >= end2) or (start1 >= start2 and end1 <= end2):
                count += 1

    return count


def count_full_overlap2(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
        count = 0

        for line in lines:
            elf1, elf2 = line.split(sep=',')
            start1, end1 = elf1.split(sep='-')
            start2, end2 = elf2.split(sep='-')

            start1 = int(start1)
            end1 = int(end1)
            start2 = int(start2)
            end2 = int(end2)

            if (start1 <= start2 <= end1) or (start1 <= end2 <= end1) \
                    or (start2 <= start1 <= end2) or (start2 <= end1 <= end2):
                count += 1

    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = count_full_overlap2('day4data.txt')
    print(result)
