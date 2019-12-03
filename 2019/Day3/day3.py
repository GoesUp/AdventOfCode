def getAllLines(path):
    lines = []
    start = (0, 0)

    for i in path:
        direction, steps = i[0], int(i[1:])
        newLine = ()
        if direction == "R":
            newLine = (start, (start[0] + steps, start[1]))
        elif direction == "L":
            newLine = (start, (start[0] - steps, start[1]))
        elif direction == "U":
            newLine = (start, (start[0], start[1] + steps))
        elif direction == "D":
            newLine = (start, (start[0], start[1] - steps))

        lines.append(newLine)
        start = newLine[1]

    return lines


def generatePoints(lineStart, lineEnd):
    if lineStart[0] == lineEnd[0]:
        if lineStart[1] < lineEnd[1]:
            points = [(lineStart[0], i) for i in range(lineStart[1], lineEnd[1] + 1)]
            return set(points)
        else:
            points = [(lineStart[0], i) for i in range(lineEnd[1], lineStart[1] + 1)]
            return set(points)
    if lineStart[0] < lineEnd[0]:
        points = [(i, lineStart[1]) for i in range(lineStart[0], lineEnd[0] + 1)]
        return set(points)
    else:
        points = [(i, lineStart[1]) for i in range(lineEnd[0], lineStart[0] + 1)]
        return set(points)


def getLineIntersections(line1, line2):
    line1Start, line1End = line1
    line2Start, line2End = line2

    if line1Start[0] - line1End[0] == 0:  # vertical
        if line2Start[0] - line2End[0] == 0:  # vertical
            if line1Start[0] == line2Start[0]:
                result = generatePoints(line1Start, line1End).intersection(generatePoints(line2Start, line2End))
                return result
            else:
                return set()
        else:  # horizontal
            if min(line1Start[1], line1End[1]) <= line2Start[1] <= max(line1Start[1], line1End[1]):
                if min(line2Start[0], line2End[0]) <= line1Start[0] <= max(line2Start[0], line2End[0]):
                    return {(line1Start[0], line2Start[1])}
                else:
                    return set()
            else:
                return set()
    else:  # horizontal
        if line2Start[1] - line2End[1] == 0:  # horizontal
            if line1Start[1] == line2Start[1]:
                result = generatePoints(line1Start, line1End).intersection(generatePoints(line2Start, line2End))
                return result
            else:
                return set()
        else:  # vertical
            if min(line2Start[1], line2End[1]) <= line1Start[1] <= max(line2Start[1], line2End[1]):
                if min(line1Start[0], line1End[0]) <= line2Start[0] <= max(line1Start[0], line1End[0]):
                    return {(line2Start[0], line1Start[1])}
                else:
                    return set()
            else:
                return set()


def getPathIntersections(wires):
    wireOneLines = getAllLines(wires[0])
    wireTwoLines = getAllLines(wires[1])

    intersections = set()
    for i in wireOneLines:
        for j in wireTwoLines:
            currentIntersection = getLineIntersections(i, j)
            intersections = intersections.union(currentIntersection)

    return intersections - {(0, 0)}


def isPointOnLine(line, point) -> bool:
    return min(line[0][0], line[1][0]) <= point[0] <= max(line[0][0], line[1][0]) and min(line[0][1], line[1][1]) <= \
           point[1] <= max(line[0][1], line[1][1])


def getPointDistance(point1, point2) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def part1(wires) -> int:
    return min(map(lambda x: abs(x[0]) + abs(x[1]), getPathIntersections(wires)))


def part2(wires) -> int:
    intersections = getPathIntersections(wires)

    wireOneLines = getAllLines(wires[0])
    wireTwoLines = getAllLines(wires[1])

    allLengths = []
    for i in intersections:
        # Wire 1
        lengthOne = 0
        for j in wireOneLines:
            if isPointOnLine(j, i):
                lengthOne += getPointDistance(j[0], i)
                break
            else:
                lengthOne += getPointDistance(j[0], j[1])

        lengthTwo = 0
        for j in wireTwoLines:
            if isPointOnLine(j, i):
                lengthTwo += getPointDistance(j[0], i)
                break
            else:
                lengthTwo += getPointDistance(j[0], j[1])

        allLengths.append(lengthOne + lengthTwo)

    return min(allLengths)


with open("day3.txt", "r") as file:
    wires = list(map(lambda x: x.split(","), file.read().split("\n")))
    print("Part 1:", part1(wires))
    print("Part 2:", part2(wires))
