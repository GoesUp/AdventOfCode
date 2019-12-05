def part1(instructions, inputValue) -> int:
    pointer = 0
    outputValue = 0
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
                instructions[parameter1] = inputValue
            elif opCode == 4:
                outputValue = instructions[parameter1]
            pointer += 2

    return outputValue

def part2(instructions, inputValue) -> int:
    pointer = 0
    outputValue = 0
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
                instructions[parameter1] = inputValue
            elif opCode == 4:
                outputValue = instructions[parameter1]
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


with open("day5.txt", "r") as file:
    instructions = list(map(int, file.read().split(",")))

    print("Part 1:", part1(instructions + [], 1))
    print("Part 2:", part2(instructions + [], 5))
