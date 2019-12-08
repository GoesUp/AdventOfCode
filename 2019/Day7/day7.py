def machine(instructions, inputValue) -> int:
    pointer = 0
    outputValue = []
    while True:
        opCode = instructions[pointer]
        if opCode % 100 in [1, 2]:
            parameter1 = instructions[pointer + 1]
            parameter2 = instructions[pointer + 2]
            paramMode = ((opCode // 100) % 10, (opCode // 1000) % 10, opCode // 10000)
            resultDestination = instructions[pointer + 3]
            if (opCode % 100) == 1:
                if paramMode[0] == 0 and paramMode[1] == 0:
                    instructions[resultDestination] = instructions[parameter1] + instructions[parameter2]
                elif paramMode[0] == 1 and paramMode[1] == 1:
                    instructions[resultDestination] = parameter1 + parameter2
                elif paramMode[0] == 1:
                    instructions[resultDestination] = parameter1 + instructions[parameter2]
                elif paramMode[1] == 1:
                    instructions[resultDestination] = instructions[parameter1] + parameter2
            elif (opCode % 100) == 2:
                if paramMode[0] == 0 and paramMode[1] == 0:
                    instructions[resultDestination] = instructions[parameter1] * instructions[parameter2]
                elif paramMode[0] == 1 and paramMode[1] == 1:
                    instructions[resultDestination] = parameter1 * parameter2
                elif paramMode[0] == 1:
                    instructions[resultDestination] = parameter1 * instructions[parameter2]
                elif paramMode[1] == 1:
                    instructions[resultDestination] = instructions[parameter1] * parameter2
            pointer += 4
        elif opCode % 100 == 99:
            break
        elif opCode % 100 in [3, 4]:
            parameter1 = instructions[pointer + 1]
            if opCode == 3:
                instructions[parameter1] = inputValue[0]
                inputValue = inputValue[1:]
            elif opCode == 4:
                outputValue += [instructions[parameter1]]
            pointer += 2
        elif opCode % 100 == 5:
            parameter1 = instructions[pointer + 1]
            parameter2 = instructions[pointer + 2]
            paramMode = ((opCode // 100) % 10, (opCode // 1000) % 10)
            if paramMode[0] == 0:
                if instructions[parameter1] != 0:
                    if paramMode[1] == 0:
                        pointer = instructions[parameter2]
                    else:
                        pointer = parameter2
                else:
                    pointer += 3
            else:
                if parameter1 != 0:
                    if paramMode[1] == 0:
                        pointer = instructions[parameter2]
                    else:
                        pointer = parameter2
                else:
                    pointer += 3
        elif opCode % 100 == 6:
            parameter1 = instructions[pointer + 1]
            parameter2 = instructions[pointer + 2]
            paramMode = ((opCode // 100) % 10, (opCode // 1000) % 10)
            if paramMode[0] == 0:
                if instructions[parameter1] == 0:
                    if paramMode[1] == 0:
                        pointer = instructions[parameter2]
                    else:
                        pointer = parameter2
                else:
                    pointer += 3
            else:
                if parameter1 == 0:
                    if paramMode[1] == 0:
                        pointer = instructions[parameter2]
                    else:
                        pointer = parameter2
                else:
                    pointer += 3
        elif opCode % 100 == 7:
            parameter1 = instructions[pointer + 1]
            parameter2 = instructions[pointer + 2]
            paramMode = ((opCode // 100) % 10, (opCode // 1000) % 10)
            resultDestination = instructions[pointer + 3]

            if paramMode[0] == 0 and paramMode[1] == 0:
                if instructions[parameter1] < instructions[parameter2]:
                    instructions[resultDestination] = 1
                else:
                    instructions[resultDestination] = 0
            elif paramMode[0] == 1 and paramMode[1] == 1:
                if parameter1 < parameter2:
                    instructions[resultDestination] = 1
                else:
                    instructions[resultDestination] = 0
            elif paramMode[0] == 1:
                if parameter1 < instructions[parameter2]:
                    instructions[resultDestination] = 1
                else:
                    instructions[resultDestination] = 0
            elif paramMode[1] == 1:
                if instructions[parameter1] < parameter2:
                    instructions[resultDestination] = 1
                else:
                    instructions[resultDestination] = 0
            pointer += 4
        elif opCode % 100 == 8:
            parameter1 = instructions[pointer + 1]
            parameter2 = instructions[pointer + 2]
            paramMode = ((opCode // 100) % 10, (opCode // 1000) % 10)
            resultDestination = instructions[pointer + 3]

            if paramMode[0] == 0 and paramMode[1] == 0:
                if instructions[parameter1] == instructions[parameter2]:
                    instructions[resultDestination] = 1
                else:
                    instructions[resultDestination] = 0
            elif paramMode[0] == 1 and paramMode[1] == 1:
                if parameter1 == parameter2:
                    instructions[resultDestination] = 1
                else:
                    instructions[resultDestination] = 0
            elif paramMode[0] == 1:
                if parameter1 == instructions[parameter2]:
                    instructions[resultDestination] = 1
                else:
                    instructions[resultDestination] = 0
            elif paramMode[1] == 1:
                if instructions[parameter1] == parameter2:
                    instructions[resultDestination] = 1
                else:
                    instructions[resultDestination] = 0
            pointer += 4

    return outputValue

def part1(numbers):
    permutations = [[0, 1, 2, 3, 4], [1, 0, 2, 3, 4], [2, 0, 1, 3, 4], [0, 2, 1, 3, 4], [1, 2, 0, 3, 4],
                    [2, 1, 0, 3, 4], [2, 1, 3, 0, 4], [1, 2, 3, 0, 4], [3, 2, 1, 0, 4], [2, 3, 1, 0, 4],
                    [1, 3, 2, 0, 4], [3, 1, 2, 0, 4], [3, 0, 2, 1, 4], [0, 3, 2, 1, 4], [2, 3, 0, 1, 4],
                    [3, 2, 0, 1, 4], [0, 2, 3, 1, 4], [2, 0, 3, 1, 4], [1, 0, 3, 2, 4], [0, 1, 3, 2, 4],
                    [3, 1, 0, 2, 4], [1, 3, 0, 2, 4], [0, 3, 1, 2, 4], [3, 0, 1, 2, 4], [4, 0, 1, 2, 3],
                    [0, 4, 1, 2, 3], [1, 4, 0, 2, 3], [4, 1, 0, 2, 3], [0, 1, 4, 2, 3], [1, 0, 4, 2, 3],
                    [1, 0, 2, 4, 3], [0, 1, 2, 4, 3], [2, 1, 0, 4, 3], [1, 2, 0, 4, 3], [0, 2, 1, 4, 3],
                    [2, 0, 1, 4, 3], [2, 4, 1, 0, 3], [4, 2, 1, 0, 3], [1, 2, 4, 0, 3], [2, 1, 4, 0, 3],
                    [4, 1, 2, 0, 3], [1, 4, 2, 0, 3], [0, 4, 2, 1, 3], [4, 0, 2, 1, 3], [2, 0, 4, 1, 3],
                    [0, 2, 4, 1, 3], [4, 2, 0, 1, 3], [2, 4, 0, 1, 3], [3, 4, 0, 1, 2], [4, 3, 0, 1, 2],
                    [0, 3, 4, 1, 2], [3, 0, 4, 1, 2], [4, 0, 3, 1, 2], [0, 4, 3, 1, 2], [0, 4, 1, 3, 2],
                    [4, 0, 1, 3, 2], [1, 0, 4, 3, 2], [0, 1, 4, 3, 2], [4, 1, 0, 3, 2], [1, 4, 0, 3, 2],
                    [1, 3, 0, 4, 2], [3, 1, 0, 4, 2], [0, 1, 3, 4, 2], [1, 0, 3, 4, 2], [3, 0, 1, 4, 2],
                    [0, 3, 1, 4, 2], [4, 3, 1, 0, 2], [3, 4, 1, 0, 2], [1, 4, 3, 0, 2], [4, 1, 3, 0, 2],
                    [3, 1, 4, 0, 2], [1, 3, 4, 0, 2], [2, 3, 4, 0, 1], [3, 2, 4, 0, 1], [4, 2, 3, 0, 1],
                    [2, 4, 3, 0, 1], [3, 4, 2, 0, 1], [4, 3, 2, 0, 1], [4, 3, 0, 2, 1], [3, 4, 0, 2, 1],
                    [0, 4, 3, 2, 1], [4, 0, 3, 2, 1], [3, 0, 4, 2, 1], [0, 3, 4, 2, 1], [0, 2, 4, 3, 1],
                    [2, 0, 4, 3, 1], [4, 0, 2, 3, 1], [0, 4, 2, 3, 1], [2, 4, 0, 3, 1], [4, 2, 0, 3, 1],
                    [3, 2, 0, 4, 1], [2, 3, 0, 4, 1], [0, 3, 2, 4, 1], [3, 0, 2, 4, 1], [2, 0, 3, 4, 1],
                    [0, 2, 3, 4, 1], [1, 2, 3, 4, 0], [2, 1, 3, 4, 0], [3, 1, 2, 4, 0], [1, 3, 2, 4, 0],
                    [2, 3, 1, 4, 0], [3, 2, 1, 4, 0], [3, 2, 4, 1, 0], [2, 3, 4, 1, 0], [4, 3, 2, 1, 0],
                    [3, 4, 2, 1, 0], [2, 4, 3, 1, 0], [4, 2, 3, 1, 0], [4, 1, 3, 2, 0], [1, 4, 3, 2, 0],
                    [3, 4, 1, 2, 0], [4, 3, 1, 2, 0], [1, 3, 4, 2, 0], [3, 1, 4, 2, 0], [2, 1, 4, 3, 0],
                    [1, 2, 4, 3, 0], [4, 2, 1, 3, 0], [2, 4, 1, 3, 0], [1, 4, 2, 3, 0], [4, 1, 2, 3, 0]]

    maxOutput = 0

    previousOutput = 0
    for i in permutations:
        previousOutput = 0
        for j in i:
            previousOutput = machine(numbers, [j, previousOutput])[-1]
        if previousOutput > maxOutput:
            maxOutput = previousOutput

    return maxOutput




with open("day7.txt", "r") as file:
    numbers = list(map(int, file.read().split(",")))
    print("Part 1:", part1(numbers + []))
