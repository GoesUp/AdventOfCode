import time
import re
import functools

def task1():
    with open("d03input.txt", "r") as f:
        text = f.read().replace("\n", "")

    lens = range(8,13)
    final = 0
    ttt = time.time()
    for i in range(len(text)):
        for j in lens:
            try:
                ss = text[i:i+j]
                if not (ss.startswith("mul(") and ss.endswith(")")):
                    continue

                remainder = ss.removeprefix("mul(").removesuffix(")")
                if not ("," in remainder):
                    continue

                ps = remainder.split(",")
                if not len(ps) == 2:
                    continue

                l, r = int(ps[0]), int(ps[1])
                if str(l) == ps[0] and str(r) == ps[1]:
                    final += l*r
            except:
                pass

    print(final)
    print(time.time() - ttt)

def task1better():
    with open("d03input.txt", "r") as f:
        text = f.read().replace("\n", "")

    ttt = time.time()
    final = sum(
        [
            functools.reduce(lambda a, b: a * b, map(int, i[4:-1].split(",")))
            for i in re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)
        ]
    )

    print(final)
    print(time.time() - ttt)



def task2():
    with open("d03input.txt", "r") as f:
        lines = f.read().replace("\n", "")

    lens = [4, 7] + list(range(8, 13))
    final = 0
    should_mult = True
    for i in range(len(lines)):
        for j in lens:
            try:
                ss = lines[i:i + j]
                if ss == "do()":
                    should_mult = True
                    break
                if ss == "don't()":
                    should_mult = False
                    break

                if not (ss.startswith("mul(") and ss.endswith(")")):
                    continue

                remainder = ss.removeprefix("mul(").removesuffix(")")
                if not ("," in remainder):
                    continue

                ps = remainder.split(",")
                if not len(ps) == 2:
                    continue

                l, r = int(ps[0]), int(ps[1])
                if str(l) == ps[0] and str(r) == ps[1]:
                    if should_mult:
                        final += l * r
            except:
                pass

    print(final)


if __name__ == '__main__':
    task1better()
    task2()
