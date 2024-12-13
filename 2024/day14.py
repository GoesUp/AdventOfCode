import time
from enum import Enum

def task1():
    with open("d07input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()



    print(time.time() - ttt)


def task2():
    with open("d07input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()




    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
