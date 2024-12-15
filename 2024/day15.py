import time
from enum import Enum

def parse_grid(up: str) -> tuple[list[list[str]], tuple[int, int]]:
    parsed = [[x for x in y] for y in up.split("\n")]
    for i in range(len(parsed)):
        for j in range(len(parsed[i])):
            if parsed[i][j] == "@":
                return parsed, (i, j)

    raise Exception("waat")

def task1():
    with open("d15input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()

    grid_unparsed = lines[0]
    directions = lines[1].replace("\n", "")

    grid, (botX, botY) = parse_grid(grid_unparsed)
    print(botX, botY)

    dirs = {
        "<": lambda x, y: (x, y-1),
        ">": lambda x, y: (x, y+1),
        "^": lambda x, y: (x-1, y),
        "v": lambda x, y: (x+1, y)
    }

    def move(direction, i, j) -> bool:
        wantedX, wantedY = dirs[direction](i, j)
        wanted_content = grid[wantedX][wantedY]
        if wanted_content == ".":
            grid[wantedX][wantedY], grid[i][j] = grid[i][j], "."
            return True
        elif wanted_content == "#":
            return False
        elif wanted_content == "O":
            if move(direction, wantedX, wantedY):
                grid[wantedX][wantedY], grid[i][j] = grid[i][j], "."
                return True
            return False

    for g in grid:
        print("".join(g))
    for direction in directions:
        print(f"Next movement: {direction}")
        # time.sleep(3)
        if move(direction, botX, botY):
            botX, botY = dirs[direction](botX, botY)

        print()
        print()
        print()
        for g in grid:
            print("".join(g))
        print("", end="")
        # time.sleep(1)

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                total += 100*i+j
    print(total)


    print(time.time() - ttt)

def task2():
    with open("d15input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()

    grid_unparsed = lines[0].replace("\n", "waaaat").replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.").replace("waaaat", "\n")
    directions = lines[1].replace("\n", "")

    grid, (botX, botY) = parse_grid(grid_unparsed)
    print(botX, botY)

    dirs = {
        "<": lambda x, y: (x, y - 1),
        ">": lambda x, y: (x, y + 1),
        "^": lambda x, y: (x - 1, y),
        "v": lambda x, y: (x + 1, y)
    }

    def move(direction, i, j, force=False) -> bool:
        nonlocal grid
        wantedX, wantedY = dirs[direction](i, j)
        wanted_content = grid[wantedX][wantedY]

        if force:
            if move(direction, wantedX, wantedY):
                grid[wantedX][wantedY], grid[i][j] = grid[i][j], "."
                return True
            return False

        if wanted_content == ".":
            grid[wantedX][wantedY], grid[i][j] = grid[i][j], "."
            return True
        elif wanted_content == "#":
            return False
        # elif wanted_content == "O":
        #     if move(direction, wantedX, wantedY):
        #         grid[wantedX][wantedY], grid[i][j] = grid[i][j], "."
        #         return True
        #     return False
        elif wanted_content in ["[", "]"]:
            if (wanted_content == "[" and direction == ">") or (wanted_content == "]" and direction == "<"):
                if move(direction, wantedX, wantedY, True):
                    grid[wantedX][wantedY], grid[i][j] = grid[i][j], "."
                    return True
                return False

            elif wanted_content == "[" and direction == "^":
                grid_copy = [[x for x in y] for y in grid]
                if move(direction, wantedX, wantedY) and move(direction, wantedX, wantedY+1):
                    grid[wantedX][wantedY], grid[i][j] = grid[i][j], "."
                    # grid[wantedX][wantedY+1], grid[i][j+1] = grid[i][j+1], "."
                    return True
                grid = [[x for x in y] for y in grid_copy]
                return False

            elif wanted_content == "]" and direction == "^":
                grid_copy = [[x for x in y] for y in grid]
                if move(direction, wantedX, wantedY) and move(direction, wantedX, wantedY-1):
                    grid[wantedX][wantedY], grid[i][j] = grid[i][j], "."
                    # grid[wantedX][wantedY-1], grid[i][j-1] = grid[i][j-1], "."
                    return True
                grid = [[x for x in y] for y in grid_copy]
                return False

            elif wanted_content == "]" and direction == "v":
                grid_copy = [[x for x in y] for y in grid]
                if move(direction, wantedX, wantedY) and move(direction, wantedX, wantedY-1):
                    grid[wantedX][wantedY], grid[i][j] = grid[i][j], "."
                    # grid[wantedX][wantedY-1], grid[i][j-1] = grid[i][j-1], "."
                    return True
                grid = [[x for x in y] for y in grid_copy]
                return False

            elif wanted_content == "[" and direction == "v":
                grid_copy = [[x for x in y] for y in grid]
                if move(direction, wantedX, wantedY) and move(direction, wantedX, wantedY+1):
                    grid[wantedX][wantedY], grid[i][j] = grid[i][j], "."
                    # grid[wantedX][wantedY+1], grid[i][j+1] = grid[i][j+1], "."
                    return True
                grid = [[x for x in y] for y in grid_copy]
                return False


    for g in grid:
        print("".join(g))
    for direction in directions:
        print(f"Next movement: {direction}")
        # time.sleep(3)
        if move(direction, botX, botY):
            botX, botY = dirs[direction](botX, botY)

        print()
        print()
        print()
        for g in grid:
            print("".join(g))
        print("", end="")
        # time.sleep(1)

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                total += 100 * i + j
    print(total)

    print(time.time() - ttt)


if __name__ == '__main__':
    # task1()
    task2()
