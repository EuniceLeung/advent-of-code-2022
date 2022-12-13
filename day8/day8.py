def count_visible_trees(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

        width = len(lines[0])
        height = len(lines)

        count = 2 * width + 2 * height - 4

        for h in range(1, height - 1, 1):
            line = lines[h]
            for i in range(1, width - 1, 1):
                # visible if greater than max of left, right, top, or bottom nums
                if line[i] > max(line[:i]) or line[i] > max(line[i + 1:]):
                    count += 1
                else:
                    top = list(lines[j][i] for j in range(h))
                    bottom = list(lines[j][i] for j in range(h + 1, height, 1))
                    if line[i] > max(top) or line[i] > max(bottom):
                        count += 1

        return count


def get_highest_scenic_score(input_file):
    max_score = 0

    with open(input_file) as f:
        lines = f.read().splitlines()

        width = len(lines[0])
        height = len(lines)

        for h in range(1, height - 1, 1):
            line = lines[h]
            for i in range(1, width - 1, 1):
                elem = line[i]

                left_score = 0
                right_score = 0
                top_score = 0
                bottom_score = 0
                # visible if greater than max of left, right, top, or bottom nums
                top = list(lines[j][i] for j in range(h))
                bottom = list(lines[j][i] for j in range(h + 1, height, 1))

                if line[i] > max(line[:i]):
                    # left
                    left_score = i
                else:
                    # count how many trees until blocked
                    for j in range(i-1, -1, -1):
                        if line[i] > line[j]:
                            left_score += 1
                        else:
                            left_score += 1
                            break

                if line[i] > max(line[i + 1:]):
                    # right
                    right_score = width - 1 - i
                else:
                    # count how many trees until blocked
                    for j in range(i+1, width, 1):
                        if line[i] > line[j]:
                            right_score += 1
                        else:
                            right_score += 1
                            break

                if line[i] > max(top):
                    # top
                    top_score = h
                else:
                    for j in range(h-1, -1, -1):
                        if line[i] > top[j]:
                            top_score += 1
                        else:
                            top_score += 1
                            break

                if line[i] > max(bottom):
                    # bottom
                    bottom_score = width - 1 - h
                else:
                    for j in range(len(bottom)):
                        if line[i] > bottom[j]:
                            bottom_score += 1
                        else:
                            bottom_score += 1
                            break

                score = left_score * right_score * top_score * bottom_score
                max_score = max(score, max_score)

    return max_score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = get_highest_scenic_score('day8data.txt')
    print(result)
