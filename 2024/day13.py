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
        # if apr == 80 and bpr == 40:
        #     print("ayy")

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
        a,b,p = read(line)
        mem = {}
        tot = reach(0,0,0, a,b,p[0], p[1], 0,0)
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

        return firstt, secondd, prize_loc


    def solve_for_a_b(x1, x2, y1, y2, c1, c2):
        det = x1*y2 - x2*y1
        if det == 0:
            raise ValueError("No unique solution exists (determinant is zero).")

        a = (y2*c1 - y1*c2) / det
        b = (-x2*c1 + x1*c2) / det
        return a, b


    s = 0
    for line in lines:
        a, b, p = read(line)
        try:
            sol1, sol2 = solve_for_a_b(a[0], a[1], b[0], b[1], p[0]+10000000000000, p[1]+10000000000000)
            if int(sol1) == sol1 and int(sol2) == sol2:
                tot = 3*sol1 + sol2
                s += tot
        except:
            pass

    print(int(s))

    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
