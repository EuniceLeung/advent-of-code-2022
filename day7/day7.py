def get_directories(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

        path = []
        dir_sizes = {'/': 0}

        for line in lines:
            inst = line.split()
            if inst[0] == '$':  # command
                if inst[1] == 'cd':
                    if inst[2] == '..':
                        path.pop()
                    else:
                        path.append(inst[2])

            elif inst[0] == 'dir':
                # directory
                path_key = ''.join(path) + inst[1]
                dir_sizes[path_key] = 0

            else:
                # file
                for i in range(len(path)):
                    dir_path = ''.join(path[0:i+1])
                    dir_sizes[dir_path] += int(inst[0])

        total = 0
        for directory in dir_sizes:
            size = dir_sizes[directory]
            if size <= 100000:
                total += size

        return total


def find_delete_directory(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

        path = []
        dir_sizes = {'/': 0}

        for line in lines:
            inst = line.split()
            if inst[0] == '$':  # command
                if inst[1] == 'cd':
                    if inst[2] == '..':
                        path.pop()
                    else:
                        path.append(inst[2])

            elif inst[0] == 'dir':
                # directory
                path_key = ''.join(path) + inst[1]
                dir_sizes[path_key] = 0

            else:
                # file
                for i in range(len(path)):
                    dir_path = ''.join(path[0:i+1])
                    dir_sizes[dir_path] += int(inst[0])

        total_disk_space = 70000000
        total_needed_space = 30000000
        unused_space = total_disk_space - dir_sizes['/']
        space_needed = total_needed_space - unused_space

        delete_size = dir_sizes['/']
        for directory in dir_sizes:
            size = dir_sizes[directory]
            if size >= space_needed:
                delete_size = min(delete_size, size)

        return delete_size


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = find_delete_directory('day7data.txt')
    print(result)
