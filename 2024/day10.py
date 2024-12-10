import time


def task1():
    with open("d10input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    grid = [[int(x) for x in y] for y in lines]

    def find_zero_indices(grid: list[list[int]]) -> set[tuple[int, int]]:
        results = set()
        for inX, x in enumerate(grid):
            for inY, y in enumerate(x):
                if y == 0:
                    results.add((inX, inY))
        return results

    def generate_neighbors_from_positions(positions: set[tuple[int, int]], grid_size_x: int, grid_size_y: int) -> set[
        tuple[int, int]]:
        new_set = set()
        for position in positions:
            optOne = lambda x, y: (x, y + 1)
            optTwo = lambda x, y: (x, y - 1)
            optThree = lambda x, y: (x + 1, y)
            optFour = lambda x, y: (x - 1, y)
            options = (optOne, optTwo, optThree, optFour)
            for option in options:
                resulting = option(position[0], position[1])
                if 0 <= resulting[0] < grid_size_x and 0 <= resulting[1] < grid_size_y:
                    new_set.add(resulting)

        return new_set - positions

    zeroes = find_zero_indices(grid)
    total_trailheads = 0
    gsx, gsy = len(grid), len(grid[0])
    for zeroX, zeroY in zeroes:
        expected_number = 1
        positions = {(zeroX, zeroY)}
        possible_neighbors = generate_neighbors_from_positions(positions, gsx, gsy)
        okay_neighbors = set()
        while expected_number <= 9:
            for neighborX, neighborY in possible_neighbors:
                grid_value = grid[neighborX][neighborY]
                if grid_value == expected_number:
                    okay_neighbors.add((neighborX, neighborY))

            possible_neighbors = generate_neighbors_from_positions(okay_neighbors, gsx, gsy)
            if expected_number != 9:
                okay_neighbors = set()
            expected_number += 1
        total_trailheads += len(okay_neighbors)
    print(total_trailheads)

    print(time.time() - ttt)


def task2():
    with open("d10input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
