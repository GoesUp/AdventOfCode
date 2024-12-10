import time
from enum import Enum


class Direction(Enum):
    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"

TRANSITION = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
}

TRAVEL = {
    Direction.UP: lambda x,y: (x-1,y),
    Direction.RIGHT: lambda x,y: (x,y+1),
    Direction.DOWN: lambda x,y: (x+1,y),
    Direction.LEFT: lambda x,y: (x,y-1),
}


def task1():
    with open("d06input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    grid = [[x for x in y] for y in lines]
    locX, locY = -1, -1
    for posX, x in enumerate(grid):
        for posY, y in enumerate(x):
            if y == "^":
                locX, locY = posX, posY

    grid[locX][locY] = "X"
    direction = Direction.UP

    while 0 <= locX < len(grid) and 0 <= locY < len(grid[0]):
        queryX, queryY = TRAVEL[direction](locX, locY)
        if not (0 <= queryX < len(grid) and 0 <= queryY < len(grid[0])):
            break

        if grid[queryX][queryY] == "#":
            direction = TRANSITION[direction]
            continue

        locX, locY = queryX, queryY
        grid[locX][locY] = "X"

        # print("========")
        # for i in grid:
        #     print("".join(x for x in i))
        # time.sleep(0.5)

    counter = 0
    for x in grid:
        for y in x:
            if y == "X":
                counter += 1
    print(counter)
    print(time.time() - ttt)


def task2():
    with open("d06input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    grid = [[x for x in y] for y in lines]
    locX, locY = -1, -1
    possible_obstacles = []
    for posX, x in enumerate(grid):
        for posY, y in enumerate(x):
            if y == "^":
                locX, locY = posX, posY
            elif y != "#":
                possible_obstacles.append((posX, posY))

    grid[locX][locY] = "X"

    origX, origY = locX, locY
    successes = 0
    for number, obstacle in enumerate(possible_obstacles):
        print(number/len(possible_obstacles))
        locX, locY = origX, origY
        direction = Direction.UP
        path_memo: set[tuple[int, int, Direction]] = set()
        grid[obstacle[0]][obstacle[1]] = "O"
        while 0 <= locX < len(grid) and 0 <= locY < len(grid[0]):
            if (locX, locY, direction) in path_memo:
                successes += 1
                break
            path_memo.add((locX, locY, direction))
            queryX, queryY = TRAVEL[direction](locX, locY)
            if not (0 <= queryX < len(grid) and 0 <= queryY < len(grid[0])):
                break

            if grid[queryX][queryY] == "#" or ((queryX == obstacle[0]) and (queryY == obstacle[1])):
                direction = TRANSITION[direction]
                continue

            locX, locY = queryX, queryY
            grid[locX][locY] = "X"

            # print("========")
            # for i in grid:
            #     print("".join(x for x in i))
            # time.sleep(0.5)
        grid[obstacle[0]][obstacle[1]] = "."

    print(successes)
    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
