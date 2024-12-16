import sys
import time
from enum import Enum

from pyasn1_modules.rfc1157 import RequestID
sys.setrecursionlimit(10000)


class Direction(Enum):
    UP="up"
    DOWN="down"
    LEFT="left"
    RIGHT="right"

def task1():
    with open("d16input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    grid = [[x for x in y] for y in lines]


    directions = {
        Direction.UP: lambda x,y:(x-1, y),
        Direction.DOWN: lambda x,y:(x+1, y),
        Direction.LEFT: lambda x,y: (x, y-1),
        Direction.RIGHT: lambda x,y: (x, y+1),
    }

    rot_left = {
        Direction.UP: Direction.LEFT,
        Direction.LEFT: Direction.DOWN,
        Direction.DOWN: Direction.RIGHT,
        Direction.RIGHT: Direction.UP
    }
    rot_right = {
        Direction.UP: Direction.RIGHT,
        Direction.LEFT: Direction.UP,
        Direction.DOWN: Direction.LEFT,
        Direction.RIGHT: Direction.DOWN
    }

    current_direction = Direction.RIGHT
    found_min = 65436
    loc_mins: dict[tuple[int, int], int] = {}
    on_best: set[tuple[int, int]] = set()

    def rec(x,y,gr,direction, rot, d, tot, total_path):
        nonlocal found_min
        nonlocal on_best

        if (x,y) in loc_mins:
            if rot == 0:
                lm_val = loc_mins[(x,y)]
                if lm_val + 1000 < tot:
                    return float("inf")
                elif lm_val > tot:
                    print(f"[FM={found_min}] [LK={len(loc_mins.keys())}] [D={d}] I've been in {(x,y)=} before, but {tot=} is cheaper than {lm_val=}.")
                    loc_mins[(x,y)] = tot
        elif rot == 0:
            print(f"[FM={found_min}] [LK={len(loc_mins.keys())}] [D={d}] It's the first time I'm in {(x,y)=}. I'm setting its val to {tot=}.")
            loc_mins[(x,y)] = tot

        # print(f"\r{d+1}             ", end="")
        # print()
        # print()
        # for xxx in gr:
        #     print("".join(xxx))
        # time.sleep(0.01)

        if tot > found_min:
            return float("inf")

        if gr[x][y] in ["#", "X"] and rot == 0:
            return float("inf")

        if rot > 1:
            return float("inf")

        if gr[x][y] == "E":
            print(f"{tot=} {d=}")
            if tot < found_min:
                print(f"fmin: {found_min}->{tot}")
                found_min = tot

            for path_part in total_path:
                on_best.add(path_part)
            return 0

        gr_c: list[list[str]] = [[x for x in y] for y in gr]
        gr_c[x][y] = "X"

        fw_dir_x, fw_dir_y = directions[direction](x,y)
        # try rotations
        possible = [
            1+rec(fw_dir_x, fw_dir_y, gr_c, direction, 0, d+1, tot+1, [ttt for ttt in total_path] + [(fw_dir_x, fw_dir_y)]),
            1000+rec(x,y,gr_c,rot_left[direction], rot+1, d+1,tot+1000, [ttt for ttt in total_path]),
            1000+rec(x,y,gr_c,rot_right[direction], rot+1, d+1, tot+1000, [ttt for ttt in total_path]),
        ]
        return min(possible)

    sx, sy = None, None
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "S":
                sx, sy = x,y
    assert sx is not None
    assert sy is not None
    print(rec(sx, sy, grid, current_direction, 0, 0, 0, [(sx, sy)]))
    print(len(on_best))
    for g in range(len(grid)):
        for gg in range(len(grid[g])):
            if (g,gg) in on_best:
                print("O", end="")
            else:
                print(grid[g][gg], end="")
        print()
    print(time.time() - ttt)


def task1b():
    with open("d16input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    grid = [[x for x in y] for y in lines]




    def rec(x,y,gr,direction, rot):
        # print()
        # print()
        # for xxx in gr:
        #     print("".join(xxx))
        # time.sleep(0.01)
        if gr[x][y] in ["#", "X"] and rot == 0:
            return float("inf")

        if rot > 1:
            return float("inf")

        if gr[x][y] == "E":
            return 0

        gr_c: list[list[str]] = [[x for x in y] for y in gr]
        gr_c[x][y] = "X"

        fw_dir_x, fw_dir_y = directions[direction](x,y)
        # try rotations
        possible = [
            1+rec(fw_dir_x, fw_dir_y, gr_c, direction, 0),
            1000+rec(x,y,gr_c,rot_left[direction], rot+1),
            1000+rec(x,y,gr_c,rot_right[direction], rot+1),
            ]
        return min(possible)

    sx, sy = None, None
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "S":
                sx, sy = x,y
    assert sx is not None
    assert sy is not None
    print(rec(sx, sy, grid, current_direction, 0))
    print(time.time() - ttt)


def task2():
    with open("d16input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()




    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
