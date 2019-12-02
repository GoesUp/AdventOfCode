fn = lambda x: int(x / 3) - 2


def part1(data) -> int:
    totalFuel = 0
    for i in data:
        totalFuel += fn(i)
    return totalFuel


def part2(data) -> int:
    totalFuel = 0
    for i in data:
        curentModuleFuel = fn(i)
        additionalFuel = fn(curentModuleFuel)
        if additionalFuel >= 0:
            curentModuleFuel += additionalFuel
        while additionalFuel > 0:
            additionalFuel = fn(additionalFuel)
            if additionalFuel > 0:
                curentModuleFuel += additionalFuel
        totalFuel += curentModuleFuel
    return totalFuel


with open("day2.txt", "r") as f:
    data = list(map(int, f.read().split("\n")))
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
