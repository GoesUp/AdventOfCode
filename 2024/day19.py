import time
from enum import Enum

def task1():
    with open("d19input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()

    towels = lines[0].split(", ")
    designs = lines[1].split("\n")

    towel_cache: dict[str, set[str]] = {}
    for towel in towels:
        for letter in towel:
            if letter not in towel_cache:
                towel_cache[letter] = set()
            towel_cache[letter].add(towel)

    def can_it_be_made(design: str) -> bool:
        if len(design) == 0:
            return True

        fl = design[0]
        cache = towel_cache.get(fl, set())
        for possible in cache:
            if design.startswith(possible) and can_it_be_made(design.removeprefix(possible)):
                return True
        return False

    total = 0
    for design in designs:
        if can_it_be_made(design):
            total += 1
    print(total)



    print(time.time() - ttt)


def task2():
    with open("d19input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()

    towels = lines[0].split(", ")
    designs = lines[1].split("\n")

    towel_cache: dict[str, set[str]] = {}
    for towel in towels:
        for letter in towel:
            if letter not in towel_cache:
                towel_cache[letter] = set()
            towel_cache[letter].add(towel)

    memo = {}

    def can_it_be_made(design: str) -> int:
        if design in memo:
            return memo[design]

        if len(design) == 0:
            return 1

        fl = design[0]
        cache = towel_cache.get(fl, set())
        subtotal = 0
        for possible in cache:
            if design.startswith(possible):
                cibm = can_it_be_made(design.removeprefix(possible))
                subtotal += cibm
        memo[design] = subtotal
        return subtotal

    total = 0
    for index, design in enumerate(designs):
        print(f"\r{index}", end="")
        total += can_it_be_made(design)
        memo = {}
    print()
    print(total)


    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
