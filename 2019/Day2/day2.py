def runTheProgram(data):
    pointer = 0
    while pointer < len(data) and data[pointer] is not 99:
        opcode = data[pointer]
        parameter1 = data[pointer + 1]
        parameter2 = data[pointer + 2]
        resultDestination = data[pointer + 3]
        if opcode == 1:
            data[resultDestination] = data[parameter1] + data[parameter2]
        elif opcode == 2:
            data[resultDestination] = data[parameter1] * data[parameter2]
        pointer += 4
    return data


def runTheProgramWithExpectedResult(data, expectedResult) -> bool:
    pointer = 0
    while pointer < len(data) and data[pointer] is not 99:
        opcode = data[pointer]
        parameter1 = data[pointer + 1]
        parameter2 = data[pointer + 2]
        resultDestination = data[pointer + 3]
        if opcode == 1:
            data[resultDestination] = data[parameter1] + data[parameter2]
        elif opcode == 2:
            data[resultDestination] = data[parameter1] * data[parameter2]
        pointer += 4
        if data[0] > expectedResult:
            return False
    return data[0] == expectedResult


def part1(data) -> int:
    data[1] = 12
    data[2] = 2
    data = runTheProgram(data)
    return data[0]


def part2(data, expectedResult) -> int:
    for i in range(100):
        for j in range(100):
            newData = [] + data
            newData[1] = i
            newData[2] = j
            if runTheProgramWithExpectedResult(newData, expectedResult):
                return 100 * i + j


with open("day2.txt", "r") as f:
    data = list(map(int, f.read().split(",")))
    print(part1([] + data))
    print(part2(data, 19690720))
