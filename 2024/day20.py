import time
from enum import Enum

def task1():
    with open("d20input.txt", "r") as f:
        lines: list[str] = f.read().split("\n")
    ttt = time.time()

    lines: list[list[str|int]] = [[x for x in y] for y in lines]
    for line_index in range(len(lines)):
        for col_index in range(len(lines[line_index])):
            if lines[line_index][col_index] == "S":
                lines[line_index][col_index] = 0
            elif lines[line_index][col_index] == ".":
                lines[line_index][col_index] = float("inf")

    basic = [[x for x in y] for y in lines]

    def simulate(grid: list[list[str | int]], lox: int, loy: int) -> int:
        changes = {(lox, loy)}
        nc2 = set()
        for x, y in changes:
            for a in [
                (x - 1, y),
                (x + 1, y),
                (x, y - 1),
                (x, y + 1),
            ]:
                nc2.add(a)
        changes = list(nc2)
        found_len = float("inf")
        while changes:
            new_changes = set()
            for lindex, cindex in changes:
                try:
                    item = grid[lindex][cindex]
                    if item == "#":
                        continue

                    neighbors_loc = [
                        (lindex - 1, cindex),
                        (lindex + 1, cindex),
                        (lindex, cindex - 1),
                        (lindex, cindex + 1),
                    ]
                    nlf = lambda x: 0 < x[0] < len(grid) and 0 < x[1] < len(grid[0])
                    neighbors_loc = list(filter(nlf, neighbors_loc))
                    nlactual = [grid[a][b] for a,b in neighbors_loc if grid[a][b] not in ["#", "E"]]
                    if item == "E":
                        if any([x < float("inf") for x in nlactual]):
                            return min(nlactual) + 1
                        continue
                    for quant in nlactual:
                        if quant + 1 < item:
                            new_changes.add((lindex, cindex))
                            grid[lindex][cindex] = quant + 1
                except:
                    pass


            nc2 = set()
            for x,y in new_changes:
                for a in [
                        (x - 1, y),
                        (x + 1, y),
                        (x, y - 1),
                        (x, y + 1),
                    ]:
                    nc2.add(a)
            changes = list(nc2)

    endx, endy = None, None
    for inx in range(len(basic) - 1):
        for iny in range(len(basic[inx]) - 1):
            if basic[inx][iny] == 0:
                endx, endy = inx, iny

    starting_point = simulate([[x for x in y] for y in basic], endx, endy)
    ooo = 0
    for gridx in range(1, len(basic)):
        for gridy in range(1, len(basic)):
            if basic[gridx][gridy] == "#":
                print(gridx, gridy)
                b2 = [[x for x in y] for y in basic]
                b2[gridx][gridy] = float("inf")
                res = simulate(b2, endx, endy)
                if res + 100 <= starting_point:
                    ooo += 1

    print("=====")
    print(ooo)










    print(time.time() - ttt)


def task2():
    with open("d20input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()




    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
