import sys
import time

sys.setrecursionlimit(10000)


def task1():
    with open("d18input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    X = 70
    Y = 70
    FIRST = 1024

    # X = 6
    # Y = 6
    # FIRST = 12

    grid = [[float("inf") for _ in range(X + 1)] for _ in range(Y + 1)]
    fallen = [tuple(map(int, x.split(","))) for x in lines][:FIRST]
    fallen = set(fallen)
    grid[0][0] = 0

    changed = True
    while changed:
        changed = False

        grid_new = [[x for x in y] for y in grid]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j,i) in fallen:
                    continue
                opts = [
                    (i-1, j),
                    (i+1, j),
                    (i, j-1),
                    (i, j+1),
                ]
                vals = []
                for opt1,opt2 in opts:
                    if opt1 < 0 or opt2 < 0:
                        continue
                    try:
                        val = grid[opt1][opt2]
                        vals.append(val + 1)
                    except:
                        pass
                if min(vals) < grid[i][j]:
                    grid_new[i][j] = min(vals)
                    changed = True

        grid = grid_new

    print(grid[X][Y])



    print(time.time() - ttt)


def task2():
    with open("d18input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    X = 70
    Y = 70
    FIRST = 2900

    # X = 6
    # Y = 6
    # FIRST = 12
    assert float("inf") == float("inf")
    for f in range(FIRST, len(lines)):
        print(f"\r{f}", end="")
        grid = [[float("inf") for _ in range(X + 1)] for _ in range(Y + 1)]
        fallenx = [tuple(map(int, x.split(","))) for x in lines][:f]
        fallen = set(fallenx)
        grid[0][0] = 0

        changed = {(0,0)}
        while len(changed):
            new_changed = set()
            grid_new = [[x for x in y] for y in grid]

            for i,j in changed:
                if (j,i) in fallen:
                    continue
                opts = [
                    (i-1, j),
                    (i+1, j),
                    (i, j-1),
                    (i, j+1),
                ]
                # vals = []
                # for opt1,opt2 in opts:
                #     if opt1 < 0 or opt2 < 0:
                #         continue
                #     try:
                #         val = grid[opt1][opt2]
                #         vals.append(val + 1)
                #     except:
                #         pass
                valid = {}
                for opt1, opt2 in opts:
                    if opt1 < 0 or opt2 < 0:
                        continue
                    try:
                        if grid[i][j] + 1 < grid[opt1][opt2]:
                            grid_new[opt1][opt2] = grid[i][j] + 1
                            new_changed.add((opt1, opt2))
                    except:
                        pass
            changed = new_changed
            grid = grid_new

        if grid[X][Y] == float("inf"):
            print()
            print(f, fallenx[-1])
            break

    print(time.time() - ttt)


if __name__ == '__main__':
    # task1()
    task2()
