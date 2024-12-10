import time


def task1():
    with open("d09input.txt", "r") as f:
        line = f.read()
    ttt = time.time()

    disk = []
    mode = "file"
    file_index = 0
    for char in line:
        char = int(char)
        if mode == "file":
            disk += [file_index for _ in range(char)]
            mode = "empty"
        elif mode == "empty":
            disk += ["." for _ in range(char)]
            mode = "file"
            file_index += 1

    i, j = 0, len(disk) - 1
    while i < j:
        if disk[i] != ".":
            i += 1
            continue
        if disk[j] == ".":
            j -= 1
            continue
        disk[i], disk[j] = disk[j], disk[i]
        i += 1
        j -= 1

    print(sum([i * j for i, j in enumerate(disk) if j != "."]))

    print(time.time() - ttt)


def task2():
    with open("d09input.txt", "r") as f:
        line = f.read()
    ttt = time.time()

    disk = []
    mode = "file"
    file_index = 0
    spaces: list[tuple[int, int]] = []
    files: list[tuple[int, int]] = []
    for char in line:
        char = int(char)
        if mode == "file":
            files.append((len(disk), char))
            disk += [file_index for _ in range(char)]
            mode = "empty"
        elif mode == "empty":
            spaces.append((len(disk), char))
            disk += ["." for _ in range(char)]
            mode = "file"
            file_index += 1

    for file_range in range(len(files) - 1, 0, -1):
        if file_range % 100 == 0:
            print(file_range)
        file_location, file_length = files[file_range]
        for space_range in range(len(spaces)):
            space_location, space_length = spaces[space_range]

            if file_location < space_location:
                break

            if space_length < file_length:
                continue
            # print(
            #     f"{file_range} went from loc {file_location}-{file_location + file_length - 2} to loc {space_location}-{space_location + file_length - 2}")
            files[file_range] = (space_location, file_length)
            if files != space_length:
                spaces[space_range] = (space_location + file_length, space_length - file_length)
            break

    disk_copy = ["." for _ in range(len(disk))]
    for index, file in enumerate(files):
        for i in range(file[1]):
            new_ind = file[0] + i
            # disk_copy[new_ind:new_ind + 1] = index
            disk_copy = disk_copy[:new_ind] + [index] + disk_copy[new_ind + 1:]

    print(sum([i * j for i, j in enumerate(disk_copy) if j != "."]))

    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
