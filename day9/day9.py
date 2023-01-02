class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def count_tail_positions(input_file):
    tail_pos_set = set()
    tail_pos_set.add((0, 0))  # use (0,0) to represent start

    with open(input_file) as f:
        lines = f.read().splitlines()
        h_x = 0
        h_y = 0
        t_x = 0
        t_y = 0

        for line in lines:
            direction, moves = line.split()
            moves = int(moves)

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

    return len(tail_pos_set)


def count_tail_positions2(input_file):
    head = Point(0, 0)
    tail_pos_set = set()
    tail_pos_set.add((0, 0))  # use (0,0) to represent start

    n = 9
    tail = []
    for i in range(n):
        tail.append(Point(0, 0))

    with open(input_file) as f:
        lines = f.read().splitlines()

        for line in lines:
            direction, moves = line.split()
            moves = int(moves)

            for i in range(moves):
                move_head(head, direction)
                prev_tail = head
                for j in range(n):
                    move_tail(prev_tail, tail[j])
                    prev_tail = tail[j]
                tail_pos_set.add((prev_tail.x, prev_tail.y))

    return len(tail_pos_set)


def move_head(head, direction):
    match direction:
        case 'L':
            # -x
            head.x -= 1
        case 'R':
            # +x
            head.x += 1
        case 'U':
            # -y
            head.y += 1
        case 'D':
            # +y
            head.y -= 1


def move_tail(head, tail):
    if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
        if head.x > tail.x:
            tail.x += 1
        elif head.x < tail.x:
            tail.x -= 1
        if head.y > tail.y:
            tail.y += 1
        elif head.y < tail.y:
            tail.y -= 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = count_tail_positions2('day9data.txt')
    print(result)
