from collections import Counter


def task1():
    with open("d02input.txt", "r") as f:
        lines = f.read().split("\n")
    acc = 0
    for i in lines:
        ns = [int(w) for w in i.split()]
        trend = [b-a for a, b in zip(ns[0:-1], ns[1:])]

        all_positive = all(3 >= x >= 1 for x in trend)
        all_negative = all(-3 <= y <= -1 for y in trend)
        if not (all_positive or all_negative):
            continue

        acc += 1

    print(acc)

def task2():
    with open("d02input.txt", "r") as f:
        lines = f.read().split("\n")
    acc = 0
    for i in lines:
        ns = [int(w) for w in i.split()]
        possible = [ns]
        for ww in range(len(ns)):
            new_ns = [nnn for nnn in ns]
            new_ns.pop(ww)
            possible.append(new_ns)
        for xx in possible:
            trend = [b - a for a, b in zip(xx[0:-1], xx[1:])]
            all_positive = all(3 >= x >= 1 for x in trend)
            all_negative = all(-3 <= y <= -1 for y in trend)
            if not (all_positive or all_negative):
                continue

            acc += 1
            break

    print(acc)


if __name__ == '__main__':
    task1()
    task2()
