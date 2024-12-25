import itertools
import time
from enum import Enum

def task1():
    with open("d25input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()

    keys = []
    locks = []

    def convert_to_lock(ls: list[str]) -> list[int]:
        acc = [-1 for _ in range(len(ls[0]))]
        for i in ls:
            for index, j in enumerate(i):
                if j == "#":
                    acc[index] += 1
        return acc


    def convert_to_key(ls: list[str]) -> list[int]:
        acc = [-1 for _ in range(len(ls[0]))]
        for i in ls:
            for index, j in enumerate(i):
                if j == "#":
                    acc[index] += 1
        return acc

    height = 0
    for line in lines:
        spl = line.split("\n")
        height = len(spl) - 2
        if list({x for x in spl[0]})[0] == "#":
            locks.append(convert_to_lock(spl))
        else:
            keys.append(convert_to_key(spl))

    ok_pairs = 0
    for lock in locks:
        for key in keys:
            was_okay = True
            for h1, h2 in zip(key, lock):
                if h1 + h2 > height:
                    was_okay = False
                    break
            if was_okay:
                ok_pairs += 1
    print(ok_pairs)




    print(time.time() - ttt)


def task2():
    with open("d25input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()






    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
