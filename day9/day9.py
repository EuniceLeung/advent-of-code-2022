def count_tail_positions(input_file):
    tail_pos_set = set()
    tail_pos_set.add((0, 0)) # use (0,0) to represent start

    with open(input_file) as f:
        lines = f.read().splitlines()
        h_x = 0
        h_y = 0
        t_x = 0
        t_y = 0

        for line in lines:
            direction, moves = line.split()
            moves = int(moves)
            # tail_pos_set.add((t_x, t_y))
            match direction:
                case 'L':
                    # -x
                    for i in range(moves):
                        h_x -= 1
                        if abs(h_x - t_x) > 1:
                            t_x -= 1
                            if h_y > t_y:
                                t_y += 1
                            elif h_y < t_y:
                                t_y -= 1
                            tail_pos_set.add((t_x, t_y))
                case 'R':
                    # +x
                    for i in range(moves):
                        h_x += 1
                        if abs(h_x - t_x) > 1:
                            t_x += 1
                            if h_y > t_y:
                                t_y += 1
                            elif h_y < t_y:
                                t_y -= 1
                            tail_pos_set.add((t_x, t_y))
                case 'U':
                    # -y
                    for i in range(moves):
                        h_y += 1
                        if abs(h_y - t_y) > 1:
                            t_y += 1
                            if h_x > t_x:
                                t_x += 1
                            elif h_x < t_x:
                                t_x -= 1
                            tail_pos_set.add((t_x, t_y))
                case 'D':
                    # +y
                    for i in range(moves):
                        h_y -= 1
                        if abs(h_y - t_y) > 1:
                            t_y -= 1
                            if h_x > t_x:
                                t_x += 1
                            elif h_x < t_x:
                                t_x -= 1
                            tail_pos_set.add((t_x, t_y))
    print(tail_pos_set)
    return len(tail_pos_set)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = count_tail_positions('day9data.txt')
    print(result)
