import time
from enum import Enum

def task1():
    with open("d13input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()

    def read(line):
        ls = line.split("\n")
        first = ls[0].removeprefix("Button A: X+")
        first = first.split(", Y+")
        firstt = tuple(map(int, first))
        firsttt = lambda x, y: (x+firstt[0], y+firstt[1])
        second = ls[1].removeprefix("Button B: X+")
        second = second.split(", Y+")
        secondd = tuple(map(int, second))
        seconddd = lambda x, y: (x+secondd[0], y+secondd[1])

        prize_loc = ls[2].removeprefix("Prize: X=")
        prize_loc = prize_loc.split(", Y=")
        prize_loc = tuple(map(int, prize_loc))

        return firsttt, seconddd, prize_loc

    mem = {}

    def reach(locX, locY, presses, a, b, maxX, maxY, apr, bpr):
        # print(apr, bpr)
        if apr == 80 and bpr == 40:
            print("ayy")

        if (locX, locY) in mem:
            return mem[(locX, locY)]

        if apr > 100 or bpr > 100:
            return float("inf")

        if locX > maxX or locY > maxY:
            return float("inf")

        if locX == maxX and locY == maxY:
            return 0

        loxa, loya = a(locX, locY)
        loxb, loyb = b(locX, locY)
        sola = 3 + reach(loxa, loya, presses+1, a,b,maxX, maxY, apr+1, bpr)
        solb = 1 + reach(loxb, loyb, presses+1, a,b,maxX, maxY, apr, bpr+1)
        mem[(locX, locY)] = min(sola, solb)
        return min(sola, solb)

    s = 0
    for line in lines:
        print(line)
        a,b,p = read(line)
        mem = {}
        tot = reach(0,0,0, a,b,p[0], p[1], 0,0)
        print(tot)
        if tot < float("inf"):
            s+=tot

    print(s)






    print(time.time() - ttt)


def task2():
    with open("d13input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()

    def read(line):
        ls = line.split("\n")
        first = ls[0].removeprefix("Button A: X+")
        first = first.split(", Y+")
        firstt = tuple(map(int, first))
        firsttt = lambda x, y: (x + firstt[0], y + firstt[1])
        second = ls[1].removeprefix("Button B: X+")
        second = second.split(", Y+")
        secondd = tuple(map(int, second))
        seconddd = lambda x, y: (x + secondd[0], y + secondd[1])

        prize_loc = ls[2].removeprefix("Prize: X=")
        prize_loc = prize_loc.split(", Y=")
        prize_loc = tuple(map(int, prize_loc))

        return firsttt, seconddd, prize_loc

    mem = {}

    def reach(locX, locY, presses, a, b, maxX, maxY, apr, bpr):
        # print(apr, bpr)
        if apr == 80 and bpr == 40:
            print("ayy")

        if (locX, locY) in mem:
            return mem[(locX, locY)]

        # if apr > 100 or bpr > 100:
        #     return float("inf")

        if locX > maxX or locY > maxY:
            return float("inf")

        if locX == maxX and locY == maxY:
            return 0

        loxa, loya = a(locX, locY)
        loxb, loyb = b(locX, locY)
        sola = 3 + reach(loxa, loya, presses + 1, a, b, maxX, maxY, apr + 1, bpr)
        solb = 1 + reach(loxb, loyb, presses + 1, a, b, maxX, maxY, apr, bpr + 1)
        mem[(locX, locY)] = min(sola, solb)
        return min(sola, solb)

    s = 0
    for line in lines:
        print(line)
        a, b, p = read(line)
        mem = {}
        tot = reach(0, 0, 0, a, b, p[0]+10000000000000, p[1]+10000000000000, 0, 0)
        print(tot)
        if tot < float("inf"):
            s += tot

    print(s)

    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
