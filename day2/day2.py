def calculate_score(input_file):
    with open(input_file) as f:
        lines = f.readlines()

        score = 0

        move_points = {'X': 1, 'Y': 2, 'Z': 3}
        moves = {'X': 'A', 'Y': 'B', 'Z': 'C'}
        win_moves = {'X': 'C', 'Y': 'A', 'Z': 'B'}

        for line in lines:
            op_move, my_move = line.split()
            move_point = move_points[my_move]
            game_point = 0
            if op_move == moves[my_move]:
                game_point = 3
            elif op_move == win_moves[my_move]:
                game_point = 6

            score += move_point + game_point

    return score


def calculate_score2(input_file):
    with open(input_file) as f:
        lines = f.readlines()

        score = 0

        game_points = {'X': 0, 'Y': 3, 'Z': 6}
        lose_moves = {'A': 3, 'B': 1, 'C': 2}
        tie_moves = {'A': 1, 'B': 2, 'C': 3}
        win_moves = {'A': 2, 'B': 3, 'C': 1}

        for line in lines:
            op_move, my_res = line.split()
            game_point = game_points[my_res]
            move_point = 0
            if my_res == 'Y': # tie
                move_point = tie_moves[op_move]
            elif my_res == 'X': # lose
                move_point = lose_moves[op_move]
            else:
                move_point = win_moves[op_move]

            score += move_point + game_point

    return score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = calculate_score2('day2data.txt')
    print(result)
