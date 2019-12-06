def part1(lines) -> int:
    connectionsReversed = dict()
    allObjects = set()

    for i in lines:
        center, orbit = i.split(")")
        connectionsReversed[orbit] = center
        allObjects.add(center)
        allObjects.add(orbit)

    countAll = 0

    for i in allObjects:
        count = 0
        obj = i
        while obj in connectionsReversed.keys():
            count += 1
            obj = connectionsReversed[obj]
        countAll += count

    return countAll


def part2(lines) -> int:
    connections = dict()
    connectionsReversed = dict()
    allObjects = set()

    for i in lines:
        center, orbit = i.split(")")
        if center in connections.keys():
            connections[center].append(orbit)
        else:
            connections[center] = [orbit]
        connectionsReversed[orbit] = center
        allObjects.add(center)
        allObjects.add(orbit)

    countSteps = 0
    parentYOU = connectionsReversed["YOU"]
    parentSAN = connectionsReversed["SAN"]

    visited = ["YOU"]
    currentPosition = parentYOU
    while True:
        result = goRecursive(currentPosition, parentSAN, connections, visited)
        if not result:
            visited.append(currentPosition)
            currentPosition = connectionsReversed[currentPosition]
            countSteps += 1
        else:
            countSteps += result
            break

    return countSteps - 1


def goRecursive(current, goal, connections, visited):
    if goal == current:
        return True

    if current not in connections.keys():
        return False

    for i in connections[current]:
        if i in visited:
            continue
        result = goRecursive(i, goal, connections, visited)
        if not result:
            continue
        return result + 1

    return False


with open("day6.txt", "r") as file:
    lines = file.read().split("\n")
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
