def count_visible_trees(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

        width = len(lines[0])
        height = len(lines)

        count = 2 * width + 2 * height - 4

        tops = []
        bottoms = []
        for i in range(1, width - 1, 1):
            tops.append(list(lines[0][i]))
            bottoms.append(list(lines[j][i] for j in range(2, height, 1)))

        for h in range(1, height - 1, 1):
            line = lines[h]
            for i in range(1, width - 1, 1):
                # visible if greater than max of left, right, top, or bottom nums
                if line[i] > max(line[:i]) or line[i] > max(line[i + 1:]):
                    count += 1
                elif line[i] > max(tops[i-1]) or line[i] > max(bottoms[i-1]):
                    count += 1

                tops[i-1].append(line[i])
                bottoms[i-1] = bottoms[i-1][1:]

        return count


def get_highest_scenic_score(input_file):
    max_score = 0

    with open(input_file) as f:
        lines = f.read().splitlines()

        width = len(lines[0])
        height = len(lines)

        tops = []
        bottoms = []
        for i in range(1, width - 1, 1):
            tops.append(list(lines[0][i]))
            bottoms.append(list(lines[j][i] for j in range(2, height, 1)))

        for h in range(1, height - 1, 1):
            line = lines[h]
            for i in range(1, width - 1, 1):
                left_score = 0
                right_score = 0
                top_score = 0
                bottom_score = 0
                # visible if greater than max of left, right, top, or bottom nums
                top = tops[i-1]
                bottom = bottoms[i-1]

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

                tops[i - 1].append(line[i])
                bottoms[i - 1] = bottoms[i - 1][1:]

    return max_score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = get_highest_scenic_score('day8data.txt')
    print(result)
