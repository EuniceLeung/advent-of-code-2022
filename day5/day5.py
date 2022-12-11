def get_top(input_file):
    # initial stacks
    #     [G]         [P]         [M]
    #     [V]     [M] [W] [S]     [Q]
    #     [N]     [N] [G] [H]     [T] [F]
    #     [J]     [W] [V] [Q] [W] [F] [P]
    # [C] [H]     [T] [T] [G] [B] [Z] [B]
    # [S] [W] [S] [L] [F] [B] [P] [C] [H]
    # [G] [M] [Q] [S] [Z] [T] [J] [D] [S]
    # [B] [T] [M] [B] [J] [C] [T] [G] [N]
    #  1   2   3   4   5   6   7   8   9

    with open(input_file) as f:
        lines = f.read().splitlines()
        # count = 0
        stacks = []
        stacks.append(['B', 'G', 'S', 'C'])
        stacks.append(['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G'])
        stacks.append(['M', 'Q', 'S'])
        stacks.append(['B', 'S', 'L', 'T', 'W', 'N', 'M'])
        stacks.append(['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P'])
        stacks.append(['C', 'T', 'B', 'G', 'Q', 'H', 'S'])
        stacks.append(['T', 'J', 'P', 'B', 'W'])
        stacks.append(['G', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M'])
        stacks.append(['N', 'S', 'H', 'B', 'P', 'F'])

        for line in lines[10:]:
            inst = line.split()
            num_move = int(inst[1])
            from_stack = int(inst[3])
            to_stack = int(inst[5])
            for i in range(num_move):
                box = stacks[from_stack-1].pop()
                stacks[to_stack-1].append(box)

        output = ''
        for i in range(9):
            output += stacks[i].pop()

    return output

def get_top2(input_file):

    with open(input_file) as f:
        lines = f.read().splitlines()
        # count = 0
        stacks = []
        stacks.append(['B', 'G', 'S', 'C'])
        stacks.append(['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G'])
        stacks.append(['M', 'Q', 'S'])
        stacks.append(['B', 'S', 'L', 'T', 'W', 'N', 'M'])
        stacks.append(['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P'])
        stacks.append(['C', 'T', 'B', 'G', 'Q', 'H', 'S'])
        stacks.append(['T', 'J', 'P', 'B', 'W'])
        stacks.append(['G', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M'])
        stacks.append(['N', 'S', 'H', 'B', 'P', 'F'])

        for line in lines[10:]:
            inst = line.split()
            num_move = int(inst[1])
            from_stack = int(inst[3])
            to_stack = int(inst[5])
            moves = ''
            for i in range(num_move):
                moves += stacks[from_stack-1].pop()
            for box in moves[::-1]:
                stacks[to_stack-1].append(box)

        output = ''
        for i in range(9):
            output += stacks[i].pop()

    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = get_top2('day5data.txt')
    print(result)
