def count_increases(numbers: tuple[int, ...]) -> int:
    count = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            count += 1
    return count


def star1(data: tuple[int, ...]) -> int:
    return count_increases(numbers=data)


def star2(data: tuple[int, ...]) -> int:
    sums = []
    for i in range(len(data) - 2):
        sums.append(data[i] + data[i + 1] + data[i + 2])
    return count_increases(numbers=tuple(sums))


def main() -> None:
    with open("day1.txt", "r") as f:
        data = tuple(map(int, f.read().split("\n")[:-1]))

        print(star1(data=data))
        print(star2(data=data))


if __name__ == "__main__":
    main()
