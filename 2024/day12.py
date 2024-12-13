import time
from enum import Enum
from pydoc import plainpager


def task1():
    with open("d12input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    grid = [[x for x in l] for l in lines]
    plant_info: dict[str, list[tuple[int, int]]] = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            plant_type = grid[i][j]
            plant_info[plant_type] = plant_info.get(plant_type, [])
            plant_info[plant_type].append((i, j))

    def post_process_plant_type(locations: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
        groups = []
        new_group = [locations.pop(0)]
        while len(locations):
            found_neighbor = False
            for i, loc in enumerate(locations):
                locs = [
                    (loc[0], loc[1] + 1),
                    (loc[0], loc[1] - 1),
                    (loc[0] - 1, loc[1]),
                    (loc[0] + 1, loc[1]),
                ]
                found_neighbor = any(any(ll == l for ll in new_group) for l in locs)
                if found_neighbor:
                    new_group.append(locations.pop(i))
                    break
            if not found_neighbor:
                groups.append(new_group)
                if locations:
                    new_group = [locations.pop(0)]
        groups.append(new_group)
        return groups

    new_plant_info = {}
    for plant_type, plant_locations in plant_info.items():
        processed = post_process_plant_type(plant_locations)
        for i, p in enumerate(processed):
            new_plant_info[f"{plant_type}{i}"] = p

    def get_surrounding(loc: tuple[int, int], g: list[list[str]]) -> tuple[str, ...]:
        locs = [
            (loc[0], loc[1] + 1),
            (loc[0], loc[1] - 1),
            (loc[0] - 1, loc[1]),
            (loc[0] + 1, loc[1]),
        ]
        out: list[str] = []
        for locX, locY in locs:
            if 0 <= locX < len(g) and 0 <= locY < len(g[0]):
                out.append(g[locX][locY])
        return tuple(out)

    total = 0
    for plant_type, plant_locations in new_plant_info.items():
        plant_area = len(plant_locations)
        plant_perimeter = 0
        for plant_location in plant_locations:
            surr = get_surrounding(plant_location, grid)
            plant_perimeter += 4 - sum(s == plant_type[0] for s in surr)
        print(f"Plant {plant_type} plants with price {plant_area} * {plant_perimeter} = {plant_area * plant_perimeter}")
        total += plant_area * plant_perimeter
    print(total)

    print(time.time() - ttt)


def task2():
    with open("d12input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()


    grid = [[x for x in l] for l in lines]
    plant_info: dict[str, list[tuple[int, int]]] = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            plant_type = grid[i][j]
            plant_info[plant_type] = plant_info.get(plant_type, [])
            plant_info[plant_type].append((i, j))

    def post_process_plant_type(locations: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
        groups = []
        new_group = [locations.pop(0)]
        while len(locations):
            found_neighbor = False
            for i, loc in enumerate(locations):
                locs = [
                    (loc[0], loc[1] + 1),
                    (loc[0], loc[1] - 1),
                    (loc[0] - 1, loc[1]),
                    (loc[0] + 1, loc[1]),
                ]
                found_neighbor = any(any(ll == l for ll in new_group) for l in locs)
                if found_neighbor:
                    new_group.append(locations.pop(i))
                    break
            if not found_neighbor:
                groups.append(new_group)
                if locations:
                    new_group = [locations.pop(0)]
        groups.append(new_group)
        return groups

    new_plant_info = {}
    for plant_type, plant_locations in plant_info.items():
        processed = post_process_plant_type(plant_locations)
        for i, p in enumerate(processed):
            new_plant_info[f"{plant_type}{i}"] = p
    del plant_info

    def where_border(pt: str, loc: tuple[int, int], g: list[list[str]]) -> set[str]:
        sides = set()


        locs = {
            "right": (loc[0], loc[1] + 1),
            "left": (loc[0], loc[1] - 1),
            "up": (loc[0] - 1, loc[1]),
            "down": (loc[0] + 1, loc[1])
        }

        for k, v in locs.items():
            locX, locY = v
            if 0 <= locX < len(g) and 0 <= locY < len(g[0]) and g[locX][locY] != pt:
                sides.add(k)
            if locX < 0:
                sides.add("up")
            if locX >= len(g):
                sides.add("down")
            if locY < 0:
                sides.add("left")
            if locY >= len(g[0]):
                sides.add("right")

        return sides

    del plant_type, plant_locations
    total = 0
    for plant_type, plant_locations in new_plant_info.items():
        plant_area = len(plant_locations)

        side_up = []
        side_left = []
        side_right = []
        side_down = []
        mapping = {
            "right": side_right,
            "left": side_left,
            "up": side_up,
            "down": side_down
        }
        for plant_location in plant_locations:
            borders = where_border(plant_type[0], plant_location, grid)
            for b in borders:
                mapping[b].append(plant_location)

        sides = sum([
            len(post_process_plant_type(x))
            for x in mapping.values()
            if len(x) > 0
        ])

        print(f"Plant {plant_type} plants with price {plant_area} * {sides} = {plant_area * sides}")
        total += plant_area * sides
    print(total)


    print(time.time() - ttt)


if __name__ == '__main__':
    # task1()
    task2()
