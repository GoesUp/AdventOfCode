import time
from enum import Enum

def task1():
    with open("d17input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()

    vals = lines[0].split("\n")
    regA = int(vals[0].split(": ")[1])
    regB = int(vals[1].split(": ")[1])
    regC = int(vals[2].split(": ")[1])
    print(f"{regA=} {regB=} {regC=}")

    program = list(map(int,lines[1].removeprefix("Program: ").split(",")))
    print(f"{program=}")

    def combo_handler(value: int) -> int:
        nonlocal regA, regB, regC

        if value <= 3:
            return value

        if value == 4:
            return regA

        if value == 5:
            return regB

        if value == 6:
            return regC

        raise Exception("Invalid value")

    pointer = 0
    output = []
    while True:
        if pointer >= len(program):
            break

        instruction = program[pointer]
        pointer += 1
        operand = program[pointer]
        pointer += 1

        if instruction == 0: # adv
            regA = int(regA / (2 ** combo_handler(operand)))
        elif instruction == 1:
            regB = regB ^ operand
        elif instruction == 2:
            regB = combo_handler(operand) % 8
        elif instruction == 3:
            if regA != 0:
                pointer = operand
        elif instruction == 4:
            regB = regB ^ regC
        elif instruction == 5:
            o = combo_handler(operand) % 8
            # print(o)
            output.append(o)
        elif instruction == 6: # bdv
            regB = int(regA / (2 ** combo_handler(operand)))
        elif instruction == 7: # cdv
            regC = int(regA / (2 ** combo_handler(operand)))
        else:
            raise Exception("Invalid instruction")

    print(",".join(list(map(str, output))))
    print(f"{regA=} {regB=} {regC=}")



    print(time.time() - ttt)


def task2():
    with open("d17input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()

    vals = [2,4,1,1,7,5,4,4,1,4,0,3,5,5,3,0]

    def compute_res(x):
        d = (x % 8)
        a = d ^ 1
        return ((((d ^ 1) ^ (x >> a)) ^ 4) % 8)

    x_cand = {0}  # end = 0 to get out of loop

    for v in vals[::-1]:
        next_x_cand = set()
        for x_next in x_cand:
            for d in range(8):
                x_current = x_next * 8 + d
                if compute_res(x_current) == v:
                    next_x_cand.add(x_current)
        x_cand = next_x_cand
        if not x_cand:
            break

    print("min xval:", min(x_cand))


    # m = 0
    # for i in range(213,10000000000):
    #     x = i
    #     done = True
    #     mm = 0
    #     for v in vals:
    #
    #         res = (((x%8)^1) ^ int(x / (2 ** ((x%8)^1)))) ^ 4 % 8
    #         if res != v:
    #             done = False
    #             break
    #         x = x//8
    #         mm += 1
    #     if mm >= m:
    #         m = mm
    #         print(f"{i=} {m=}")
    #     if done:
    #         print(f"DONE {i=}")




    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
