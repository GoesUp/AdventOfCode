import time
from enum import Enum

def task1():
    with open("d07input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    eqs = []
    for line in lines:
        l, r = line.split(": ")
        r = list(map(int, r.split(" ")))
        eqs.append((int(l), r))


    def generate_combinations(l: list[int]):
        if len(l) == 1:
            return [str(l[0])]

        rec = generate_combinations(l[1:])
        return [f"{l[0]}+{x}" for x in rec] + [f"{l[0]}*{x}" for x in rec]

    def gen_comb2(l: list[int], acc):
        if len(l) == 0:
            return acc

        return gen_comb2(l[1:], [a + l[0] for a in acc] + [a * l[0] for a in acc])

    def eval2(s):
        num1 = None
        num2 = None
        operator = None
        mode = 1
        while len(s):
            char, s = s[0], s[1:]
            if mode == 1:
                num1 = int(char)
                mode = 2
            elif mode == 2:
                if char == "+":
                    operator = lambda x,y: x+y
                    mode = 3
                elif char == "*":
                    operator = lambda x,y: x*y
                    mode = 3
                else:
                    num1 = num1 * 10 + int(char)
            elif mode == 3:
                num2 = int(char)
                mode = 4
            elif mode == 4:
                if char == "+":
                    num1 = operator(num1, num2)
                    operator = lambda x,y: x+y
                    mode = 3
                elif char == "*":
                    num1 = operator(num1, num2)
                    operator = lambda x,y: x*y
                    mode = 3
                else:
                    num2 = num2 * 10 + int(char)
        return operator(num1, num2)


    is_okay = 0
    for expected, nums in eqs:
        generated = gen_comb2(nums[1:], [nums[0]])
        # evaluated = [eval2(x) for x in generated]
        valid = sum(expected == x for x in generated)
        if valid > 0:
            is_okay += expected

    print(is_okay)

    print(time.time() - ttt)


def task2():
    with open("d07input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()



    eqs = []
    for line in lines:
        l, r = line.split(": ")
        r = list(map(int, r.split(" ")))
        eqs.append((int(l), r))


    def generate_combinations(l: list[int]):
        if len(l) == 1:
            return [str(l[0])]

        rec = generate_combinations(l[1:])
        return [f"{l[0]}+{x}" for x in rec] + [f"{l[0]}*{x}" for x in rec]

    def gen_comb2(l: list[int], acc):
        if len(l) == 0:
            return acc

        return gen_comb2(l[1:], [a + l[0] for a in acc] + [a * l[0] for a in acc] + [int(f"{a}{l[0]}") for a in acc])


    is_okay = 0
    for expected, nums in eqs:
        generated = gen_comb2(nums[1:], [nums[0]])
        # evaluated = [eval2(x) for x in generated]
        valid = sum(expected == x for x in generated)
        if valid > 0:
            is_okay += expected

    print(is_okay)

    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
