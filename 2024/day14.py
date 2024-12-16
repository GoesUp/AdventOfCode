import time
import tkinter
from enum import Enum
from tkinter import Tk, Canvas

import matplotlib.pyplot as plt
import numpy as np
from tkinter import *


def task1():
    with open("d14input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    gridH = 103
    gridW = 101
    # gridH = 7
    # gridW = 11

    grid = [["." for _ in range(gridW)] for _ in range(gridH)]
    halfH, halfW = int((gridH - 1) / 2) , int((gridW - 1) / 2)

    q_quant = [0,0,0,0]
    for line in lines:
        pos, vel = line.split(" v=")
        pos = pos.removeprefix("p=")
        posX, posY = tuple(map(int, pos.split(",")))
        velX, velY = tuple(map(int, vel.split(",")))
        # print(f"{(posX,posY)=} {(velX, velY)=}")
        for xxxx in range(100):
            new_posX, new_posY = posX+velX, posY+velY
            while new_posX < 0:
                new_posX += gridW
            while new_posX >= gridW:
                new_posX -= gridW
            while new_posY < 0:
                new_posY += gridH
            while new_posY >= gridH:
                new_posY -= gridH

            # print(f"({posX}, {posY}) -> ({new_posX}, {new_posY})")
            posX, posY = new_posX, new_posY

        if posX < halfW and posY < halfH:
            q_quant[0] += 1
        elif posX < halfW and posY > halfH:
            q_quant[1] += 1
        elif posX > halfW and posY < halfH:
            q_quant[2] += 1
        elif posX > halfW and posY > halfH:
            q_quant[3] += 1

        if grid[posY][posX] == ".":
            grid[posY][posX] = 1
        else:
            grid[posY][posX] += 1

    print(q_quant[0] * q_quant[1] * q_quant[2] * q_quant[3])

    # for x in range(len(grid)):
    #     for y in range(len(grid[x])):
    #         if x == halfH or y == halfW:
    #             grid[x][y] = " "
    # for line in grid:
    #     print("".join([str(l) for l in line]))




    print(time.time() - ttt)


def task2():
    with open("d14input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    gridH = 103
    gridW = 101

    grid = [["." for _ in range(gridW)] for _ in range(gridH)]
    halfH, halfW = int((gridH - 1) / 2), int((gridW - 1) / 2)

    posvel = []
    for line in lines:
        pos, vel = line.split(" v=")
        pos = pos.removeprefix("p=")
        posX, posY = tuple(map(int, pos.split(",")))
        velX, velY = tuple(map(int, vel.split(",")))
        posvel.append((posX, posY, velX, velY))

    master = Tk()
    # master.geometry(f"{len(grid[0])}x{len(grid)}")
    master.title("Points")
    canvas = Canvas(master,
               width=len(grid[0])*10,
               height=len(grid)*10, bg='gray')
    # tkinter._test()
    for xxxx in range(10000):
        # print(xxxx)
        canvas.pack()
        grid = [["." for _ in range(gridW)] for _ in range(gridH)]
        for index, item in enumerate(posvel):
            posX, posY, velX, velY = item
            new_posX, new_posY = posX + velX, posY + velY
            while new_posX < 0:
                new_posX += gridW
            while new_posX >= gridW:
                new_posX -= gridW
            while new_posY < 0:
                new_posY += gridH
            while new_posY >= gridH:
                new_posY -= gridH
            posvel[index] = (new_posX, new_posY, velX, velY)
            if grid[new_posY][new_posX] == ".":
                grid[new_posY][new_posX] = 1
            else:
                grid[new_posY][new_posX] += 1

        oooh = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[i])-1):
                if grid[i][j] != "." and grid[i-1][j] != "." and grid[i+1][j] != "." and grid[i][j-1] != "." and grid[i][j+1] != ".":
                    oooh += 1

        if 4000 < xxxx < 8000:
            middle_count = 0
            span = 15
            offset = 0
            midg = int(len(grid)/2)
            midgg = int(len(grid[0])+2)
            for g in range(len(grid)):
                for gg in range(len(grid[g])):
                    if midg - span + offset <= g <= midg +span+offset and midgg -span+offset <= gg <= midgg + span+offset and grid[g][gg] != ".":
                        middle_count += 1
                    if grid[g][gg] == ".":
                        pass
                    else:
                        canvas.create_oval(g*10, gg*10, g*10, gg*10, fill="white", width=5, tags="oval")
            if 7379 < xxxx < 7385:
                master.update()
                print(xxxx + 1)
                time.sleep(5)
            canvas.delete("oval")



    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
