import time
from enum import Enum

def task1():
    with open("d11input.txt", "r") as f:
        numbers = f.read().split(" ")
    ttt = time.time()

    numbers = list(map(int, numbers))
    for _ in range(25):
        new_numbers = []
        for i in numbers:
            if i == 0:
                new_numbers.append(1)
            elif len(str(i)) % 2 == 0:
                l = len(str(i))
                l2 = int(l/2)
                left, right = int(str(i)[:l2]), int(str(i)[l2:])
                new_numbers += [left, right]
            else:
                new_numbers.append(i * 2024)
        numbers = new_numbers

    print(len(numbers))

    print(time.time() - ttt)


def task2():
    with open("d11input.txt", "r") as f:
        numbers = f.read().split(" ")
    ttt = time.time()
    numbers = list(map(int, numbers))

    def process_number(number: int) -> dict[int, int]:
        sn = str(number)
        output: list[int] = []
        if number == 0:
            output.append(1)
        elif len(sn) % 2 == 0:
            l = len(sn)
            l2 = int(l/2)
            left, right = int(sn[:l2]), int(sn[l2:])
            output += [left, right]
        else:
            output.append(number * 2024)

        r = {}
        for i in output:
            r[i] = r.get(i, 0) + 1
        return r

    state: dict[int, int] = {}
    for number in numbers:
        state[number] = state.get(number, 0) + 1

    for _ in range(75):
        new_state: dict[int, int] = {}
        for number, quantity in state.items():
            rule = process_number(number)
            for result, resQuant in rule.items():
                new_state[result] = new_state.get(result, 0) + resQuant * quantity
        state = new_state

    result = sum([x for x in state.values()])
    print(f"{result=}")




    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
