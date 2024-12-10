from collections import Counter


def task1():
    with open("d01input.txt", "r") as f:
        lines = f.read().split("\n")
    pairs = [i.split("   ") for i in lines]
    left, right = [], []
    for i, j in pairs:
        left.append(int(i))
        right.append(int(j))
    left = sorted(left)
    right = sorted(right)
    print(sum([abs(i-j) for i,j in zip(left,right)]))


def task2():
    with open("d01input.txt", "r") as f:
        lines = f.read().split("\n")
    pairs = [i.split("   ") for i in lines]
    left, right = [], []
    for i, j in pairs:
        left.append(int(i))
        right.append(int(j))

    appears = {}
    total = 0
    c = Counter(right)
    for i in left:
        total += i * c[i]
    print(total)


if __name__ == '__main__':
    task1()
    task2()
