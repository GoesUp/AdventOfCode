def part1(first, second) -> int:
    stevec = 0
    for i in range(first, second + 1):
        if "11" not in str(i) and "22" not in str(i) and "33" not in str(i) and "44" not in str(i) and \
                "55" not in str(i) and "66" not in str(i) and "77" not in str(i) and "88" not in str(i) and \
                "99" not in str(i) and "00" not in str(i):
            continue
        a = str(i)
        yikes = False
        for i in range(5):
            if int(a[i]) > int(a[i + 1]):
                yikes = True
                break
        if not yikes:
            stevec += 1

    return stevec


def part2(first, second) -> int:
    stevec = 0
    for i in range(first, second + 1):

        foundMatching = False
        if "11" in str(i):
            if "111" not in str(i):
                foundMatching = True
        if "22" in str(i):
            if "222" not in str(i):
                foundMatching = True
        if "33" in str(i):
            if "333" not in str(i):
                foundMatching = True
        if "44" in str(i):
            if "444" not in str(i):
                foundMatching = True
        if "55" in str(i):
            if "555" not in str(i):
                foundMatching = True
        if "66" in str(i):
            if "666" not in str(i):
                foundMatching = True
        if "77" in str(i):
            if "777" not in str(i):
                foundMatching = True
        if "88" in str(i):
            if "888" not in str(i):
                foundMatching = True
        if "99" in str(i):
            if "999" not in str(i):
                foundMatching = True
        if "00" in str(i):
            if "000" not in str(i):
                foundMatching = True

        if not foundMatching:
            continue

        a = str(i)
        yikes = False
        for i in range(5):
            if int(a[i]) > int(a[i + 1]):
                yikes = True
                break
        if not yikes:
            stevec += 1

    return stevec


print("Part 1:", part1(138307, 654504))
print("Part 2:", part2(138307, 654504))
