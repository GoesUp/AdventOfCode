import itertools
import time
from enum import Enum

def task1():
    with open("d24input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()

    initials_raw = lines[0].split("\n")
    initials = {}
    for row in initials_raw:
        label, value = row.split(": ")
        initials[label] = value == "1"

    not_done = 1
    while not_done:
        not_done = 0
        for row in lines[1].split("\n"):
            f,s = row.split(" -> ")
            if s in initials:
                continue
            f1, operator, f2 = f.split(" ")
            if f1 not in initials or f2 not in initials:
                not_done += 1
                continue
            f1_val = initials[f1]
            f2_val = initials[f2]
            if operator == "AND":
                initials[s] = f1_val and f2_val
            elif operator == "OR":
                initials[s] = f1_val or f2_val
            elif operator == "XOR":
                initials[s] = f1_val ^ f2_val
            else:
                raise Exception("Invalid operator")

    zs = []
    for label, value in initials.items():
        if label.startswith("z"):
            zs.append((label, value))
    zs.sort()
    print(zs)

    final = 0
    for _, vrednost in zs[::-1]:
        final *= 2
        if vrednost:
            final += 1
    print(final)


    print(time.time() - ttt)


def task2():
    with open("d24input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()


    def work_with_swapped(gates: list[str]) -> bool:
        initials_raw = lines[0].split("\n")
        initials = {}
        for row in initials_raw:
            label, value = row.split(": ")
            initials[label] = value == "1"

        not_done = 1
        while not_done:
            not_done = 0
            for row in gates:
                f, s = row.split(" -> ")
                if s in initials:
                    continue
                f1, operator, f2 = f.split(" ")
                if f1 not in initials or f2 not in initials:
                    not_done += 1
                    continue
                f1_val = initials[f1]
                f2_val = initials[f2]
                if operator == "AND":
                    initials[s] = f1_val and f2_val
                elif operator == "OR":
                    initials[s] = f1_val or f2_val
                elif operator == "XOR":
                    initials[s] = f1_val ^ f2_val
                else:
                    raise Exception("Invalid operator")

        zs = []
        xs = []
        ys = []
        for label, value in initials.items():
            if label.startswith("z"):
                zs.append((label, value))
            if label.startswith("y"):
                ys.append((label, value))
            if label.startswith("x"):
                xs.append((label, value))
        zs.sort()
        xs.sort()
        ys.sort()
        print(zs)

        finalZ = 0
        for _, vrednost in zs[::-1]:
            finalZ *= 2
            if vrednost:
                finalZ += 1

        finalX = 0
        for _, vrednost in xs[::-1]:
            finalX *= 2
            if vrednost:
                finalX += 1

        finalY = 0
        for _, vrednost in ys[::-1]:
            finalY *= 2
            if vrednost:
                finalY += 1

        return finalX + finalY == finalZ

    rows = lines[1].split("\n")
    combinations = []
    for i in range(len(rows) - 1):
        for j in range(i+1, len(rows)):
            combinations.append((rows[i], rows[j]))

    combos = []
    for comb in itertools.combinations(combinations, 4):
        testing = set()
        for a,b in comb:
            testing.add(a)
            testing.add(b)
        if len(testing) < 6:
            print(f"\r{len(testing)}", end="")
            continue

        combos.append(comb)
    print(combos)
    print(len(combos))




    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
