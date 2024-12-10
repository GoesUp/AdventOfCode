import time
import re
import functools


def task1():
    with open("d04input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    grid = [[i for i in x] for x in lines]
    gridSol = [["." for i in x] for x in grid]

    found = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            searches = [
                [(i,j), (i,j+1), (i,j+2), [i,j+3]],
                [(i,j), (i,j-1), (i,j-2), [i,j-3]],
                [(i,j), (i+1,j), (i+2,j), [i+3,j]],
                [(i,j), (i-1,j), (i-2,j), [i-3,j]],

                [(i, j), (i + 1, j + 1), (i + 2, j + 2), [i + 3, j + 3]],
                [(i, j), (i + 1, j - 1), (i + 2, j - 2), [i + 3, j - 3]],
                [(i, j), (i - 1, j + 1), (i - 2, j + 2), [i - 3, j + 3]],
                [(i, j), (i - 1, j - 1), (i - 2, j - 2), [i - 3, j - 3]],
            ]

            for s in searches:
                try:
                    for ww,xx in s:
                        if ww < 0 or xx < 0 or ww > len(grid) or xx > len(grid[0]):
                            raise Exception()
                    ssss = "".join(grid[w][x] for w,x in s)
                except:
                    continue
                if ssss == "XMAS":
                    found += 1

                    for w,x in s:
                        gridSol[w][x] = grid[w][x]

    for x in gridSol:
        print("".join(x))

    print(found)




    print(time.time() - ttt)



def task2():
    with open("d04input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()


    grid = [[i for i in x] for x in lines]
    gridSol = [["." for i in x] for x in grid]
    found = 0
    def isOkay(subgrid: list[list[str]]):
        if not (subgrid[1][1] == "A"):
            return False

        return (
            ((subgrid[0][0] == "S" and subgrid[2][2] == "M") or
            (subgrid[2][2] == "S" and subgrid[0][0] == "M"))
            and
            ((subgrid[0][2] == "S" and subgrid[2][0] == "M") or
             (subgrid[2][0] == "S" and subgrid[0][2] == "M")
            )
        )

    for x in range(len(grid) - 2):
        for y in range(len(grid[0]) - 2):
            subgrid = [[grid[i][j] for j in range(y, y+3)] for i in range(x, x+3)]
            if isOkay(subgrid):
                found += 1
                gridSol[x][y] = grid[x][y]
                gridSol[x+2][y] = grid[x+2][y]
                gridSol[x][y+2] = grid[x][y+2]
                gridSol[x+2][y+2] = grid[x+2][y+2]
                gridSol[x+1][y+1] = grid[x+1][y+1]



    # for x in gridSol:
    #     print("".join(x))
    print(found)
    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
