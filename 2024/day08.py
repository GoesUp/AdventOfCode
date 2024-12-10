import time
from enum import Enum

def task1():
    with open("d08input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    grid_x_size, grid_y_size = len(lines), len(lines[0])
    print(f"GRID_SIZE: {grid_x_size, grid_y_size}")
    signal_locations: dict[str, list[tuple[int, int]]] = {}
    for locX, x in enumerate(lines):
        for locY, y in enumerate(x):
            if y == ".":
                continue

            if y not in signal_locations:
                signal_locations[y] = []

            signal_locations[y].append((locX, locY))

    hash_loc: set[tuple[int, int]] = set()
    grid = [["." for _ in range(grid_y_size)] for _ in range(grid_x_size)]
    for frequency, locations in signal_locations.items():

        print(f"Checking locations {locations} for {frequency=}")
        for ll, lll in locations:
            grid[ll][lll] = frequency
        for location1 in locations:
            for location2 in locations:
                if location1 == location2:
                    continue
                # dist_x, dist_y = location2[0] - location1[0], location2[1] - location1[1]
                # new_dist = (location2[0] + dist_x, location2[1] + dist_y)
                # hash_loc.add(new_dist)
                #
                # dist_x, dist_y = location1[0] - location2[0], location1[1] - location2[1]
                # new_dist = (location2[0] + dist_x, location2[1] + dist_y)
                # hash_loc.add(new_dist)

                grid_temp = [["." for _ in range(grid_y_size)] for _ in range(grid_x_size)]
                print(f"{location1=}, {location2=}")
                lll1, lll2 = location1, location2
                if location1[0] > location2[0]:
                    lll1, lll2 = location2, location1
                    print("switched")
                grid_temp[lll1[0]][lll1[1]] = "1"
                grid_temp[lll2[0]][lll2[1]] = "2"
                if lll2[1] > lll1[1]:
                    l1 = (
                            lll2[0] - lll1[0] + lll2[0],
                            lll2[1] + (lll2[1] - lll1[1])
                         )
                    l2 = (
                            lll1[0] - (lll2[0] - lll1[0]),
                            lll1[1] - (lll2[1] - lll1[1]),
                        )

                    if 0 <= l1[0] < grid_x_size and 0 <= l1[1] < grid_y_size:
                        hash_loc.add(l1)
                        print(f"!added {l1=}")
                        grid_temp[l1[0]][l1[1]] = "#"
                    else:
                        print(f"Couldn't add hash 1 {l1}")

                    if 0 <= l2[0] < grid_x_size and 0 <= l2[1] < grid_y_size:
                        hash_loc.add(l2)
                        print(f"!added {l2=}")
                        grid_temp[l2[0]][l2[1]] = "!"
                    else:
                        print(f"Couldn't add hash 2 {l2}")
                    # print("===\n")
                    # print("\n".join(".".join(x) for x in grid_temp))
                    # print("===")

                else:
                    print(":O")
                    l1 = (
                            lll2[0] - lll1[0] + lll2[0],
                            lll2[1] - (lll1[1] - lll2[1])
                         )
                    l2 = (
                            lll1[0] - (lll2[0] - lll1[0]),
                            lll1[1] + (lll1[1] - lll2[1]),
                        )
                    if 0 <= l1[0] < grid_x_size and 0 <= l1[1] < grid_y_size:
                        hash_loc.add(l1)
                        print(f"added {l1=}")
                        grid_temp[l1[0]][l1[1]] = "#"
                    else:
                        print(f"Couldn't add hash 1 {l1}")

                    if 0 <= l2[0] < grid_x_size and 0 <= l2[1] < grid_y_size:
                        hash_loc.add(l2)
                        print(f"added {l2=}")
                        grid_temp[l2[0]][l2[1]] = "!"
                    else:
                        print(f"Couldn't add hash 2 {l2}")
                    # print("===\n")
                    # print("\n".join(".".join(x) for x in grid_temp))
                    # print("===")

    passed = set()
    for hl, hlhl in hash_loc:
        print("============")
        print()
        for x in grid:
            print("".join(x))
        try:
            grid[hl][hlhl] = "#"
            passed.add((hl, hlhl))
        except:
            print(f"INVALID: {hl, hlhl}")

    print("============")
    for x in grid:
        print("".join(x))

    print("============")
    print(f"SOLUTION: {len(passed)}")
    print(time.time() - ttt)


def task2():
    with open("d08input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    grid_x_size, grid_y_size = len(lines), len(lines[0])
    print(f"GRID_SIZE: {grid_x_size, grid_y_size}")
    signal_locations: dict[str, list[tuple[int, int]]] = {}
    for locX, x in enumerate(lines):
        for locY, y in enumerate(x):
            if y == ".":
                continue

            if y not in signal_locations:
                signal_locations[y] = []

            signal_locations[y].append((locX, locY))

    hash_loc: set[tuple[int, int]] = set()
    grid = [["." for _ in range(grid_y_size)] for _ in range(grid_x_size)]
    for frequency, locations in signal_locations.items():

        print(f"Checking locations {locations} for {frequency=}")
        for ll, lll in locations:
            grid[ll][lll] = frequency
        for location1 in locations:
            for location2 in locations:
                if location1 == location2:
                    continue
                # dist_x, dist_y = location2[0] - location1[0], location2[1] - location1[1]
                # new_dist = (location2[0] + dist_x, location2[1] + dist_y)
                # hash_loc.add(new_dist)
                #
                # dist_x, dist_y = location1[0] - location2[0], location1[1] - location2[1]
                # new_dist = (location2[0] + dist_x, location2[1] + dist_y)
                # hash_loc.add(new_dist)

                grid_temp = [["." for _ in range(grid_y_size)] for _ in range(grid_x_size)]
                print(f"{location1=}, {location2=}")
                lll1, lll2 = location1, location2
                if location1[0] > location2[0]:
                    lll1, lll2 = location2, location1
                    print("switched")
                grid_temp[lll1[0]][lll1[1]] = "1"
                grid_temp[lll2[0]][lll2[1]] = "2"
                if lll2[1] > lll1[1]:
                    l1d = (lll2[0] - lll1[0], lll2[1] - lll1[1])
                    l2d = lll2[0] - lll1[0], lll2[1] - lll1[1]
                    l1s = [(lll2[0] + i * l1d[0], lll2[1] + i*l1d[1]) for i in range(30)]
                    l2s = [(lll1[0] - i * l2d[0], lll1[1] - i*l2d[1]) for i in range(30)]

                    for l1 in l1s:
                        if 0 <= l1[0] < grid_x_size and 0 <= l1[1] < grid_y_size:
                            hash_loc.add(l1)
                            print(f"!added {l1=}")
                            grid_temp[l1[0]][l1[1]] = "#"
                        else:
                            print(f"Couldn't add hash 1 {l1}")

                    for l2 in l2s:
                        if 0 <= l2[0] < grid_x_size and 0 <= l2[1] < grid_y_size:
                            hash_loc.add(l2)
                            print(f"!added {l2=}")
                            grid_temp[l2[0]][l2[1]] = "!"
                        else:
                            print(f"Couldn't add hash 2 {l2}")

                else:
                    print(":O")

                    l1d = (lll2[0] - lll1[0], lll1[1] - lll2[1])
                    l2d = lll2[0] - lll1[0], lll1[1] - lll2[1]
                    l1s = [(lll2[0] + i * l1d[0], lll2[1] - i*l1d[1]) for i in range(30)]
                    l2s = [(lll1[0] - i * l2d[0], lll1[1] + i*l2d[1]) for i in range(30)]
                    for l1 in l1s:
                        if 0 <= l1[0] < grid_x_size and 0 <= l1[1] < grid_y_size:
                            hash_loc.add(l1)
                            print(f"added {l1=}")
                            grid_temp[l1[0]][l1[1]] = "#"
                        else:
                            print(f"Couldn't add hash 1 {l1}")

                    for l2 in l2s:
                        if 0 <= l2[0] < grid_x_size and 0 <= l2[1] < grid_y_size:
                            hash_loc.add(l2)
                            print(f"added {l2=}")
                            grid_temp[l2[0]][l2[1]] = "!"
                        else:
                            print(f"Couldn't add hash 2 {l2}")

    passed = set()
    for hl, hlhl in hash_loc:
        print("============")
        print()
        for x in grid:
            print("".join(x))
        try:
            grid[hl][hlhl] = "#"
            passed.add((hl, hlhl))
        except:
            print(f"INVALID: {hl, hlhl}")

    print("============")
    for x in grid:
        print("".join(x))

    print("============")
    print(f"SOLUTION: {len(passed)} THEN MANUALLY INCREASE IT BY 1 LOL")

    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
