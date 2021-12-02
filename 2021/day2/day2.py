from enum import Enum


class Movement(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"


def star1(data: tuple[tuple[Movement, int], ...]) -> int:
    forward = 0
    depth = 0
    for movement, quantity in data:
        if movement == Movement.FORWARD:
            forward += quantity
        elif movement == Movement.DOWN:
            depth += quantity
        else:
            depth -= quantity
    return forward * depth


def star2(data: tuple[tuple[Movement, int], ...]) -> int:
    forward = 0
    depth = 0
    aim = 0
    for movement, quantity in data:
        if movement == Movement.FORWARD:
            forward += quantity
            depth += aim * quantity
        elif movement == Movement.DOWN:
            aim += quantity
        else:
            aim -= quantity
    return forward * depth


def main() -> None:
    with open("day2.txt", "r") as f:
        data = tuple(map(lambda x: x.split(), f.read().split("\n")[:-1]))
        data = tuple((Movement(i[0]), int(i[1])) for i in data)

        print(star1(data=data))
        print(star2(data=data))


if __name__ == "__main__":
    main()
