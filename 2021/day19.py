import time
from enum import Enum


def task1():
    with open("d19input.txt", "r") as f:
        lines = f.read().split("\n\n")
    ttt = time.time()

    def parse_input(lines: str) -> tuple[int, list[tuple[int, int, int]]]:
        lines = lines.split("\n")
        scanner_number = int(lines.pop(0).removeprefix("--- scanner ").removesuffix(" ---"))

        beacons = []
        for line in lines:
            x, y, z = map(int, line.split(","))
            beacons.append((x, y, z))

        return scanner_number, beacons

    def center_constellation_around_pivot(
            constellation: list[tuple[int, int, int]],
            pivot: tuple[int, int, int]
    ) -> list[tuple[int, int, int]]:
        return [
            (beacon[0] - pivot[0], beacon[1] - pivot[1], beacon[2] - pivot[2])
            for beacon in constellation
        ]

    def detect_quadrant(point: tuple[int, int, int]) -> int:
        # Z positive: 1234. Z negative: 5678
        # X positive: 1256. X negative: 3478
        # Y positive: 2367. Y negative: 1458
        possible = {1,2,3,4,5,6,7,8}
        if point[2] < 0:
            possible = possible - {1,2,3,4}
        else:
            possible = possible - {5,6,7,8}

        if point[1] < 0:
            possible = possible - {2,3,6,7}
        else:
            possible = possible - {1,4,5,8}

        if point[0] < 0:
            possible = possible - {1,2,5,6}
        else:
            possible = possible - {3,4,7,8}

        assert len(possible) == 1
        for possibility in possible:
            return possibility

    class Axis(Enum):
        X = "x"
        Y = "y"
        Z = "z"

    def rotate_point(point: tuple[int, int, int], axis: Axis) -> tuple[int, int, int]:
        quadrant = detect_quadrant(point)
        x,y,z = None, None, None

        if axis == Axis.X:
            x = point[0]
            if quadrant in {1,2}:
                y = point[2]
                z = -point[1]
            elif quadrant in {5,6}:
                z = point[1]
                y = -point[2]
            elif quadrant in {7,8}:
                z = -point[1]
                y = point[2]
            elif quadrant in {3,4}:
                y = point[2]
                z = -point[1]
        elif axis == Axis.Y:
            y = point[1]
            xx = point[0]
            zz = point[2]
            if quadrant in {1,4}:
                x = zz
                z = -xx
            elif quadrant in {5,8}:

            elif quadrant in {6,7}:
                raise NotImplementedError()
            elif quadrant in {2,3}:
                raise NotImplementedError()
        elif axis == Axis.Z:
            if quadrant in {1,5}:
                raise NotImplementedError()
            elif quadrant in {2,6}:
                raise NotImplementedError()
            elif quadrant in {3,7}:
                raise NotImplementedError()
            elif quadrant in {4,8}:
                raise NotImplementedError()
        else:
            raise NotImplementedError()

        return x,y,z

    USE_Z = True
    def generate_all_rotations(constellation: list[tuple[int, int, int]]) -> tuple[list[tuple[int, int, int]], ...]:
        final = []
        for xRot in [0, 1, 2, 3]:
            for yRot in [0, 1, 2, 3]:
                for zRot in [0, 1, 2, 3] if USE_Z else [0]:
                    resulting_beacons = []
                    for beacon in constellation:

                        for i in range(xRot):
                            beacon = rotate_point(beacon, Axis.X)

                        for j in range(yRot):
                            beacon = rotate_point(beacon, Axis.Y)

                        for j in range(zRot):
                            beacon = rotate_point(beacon, Axis.Z)

                        resulting_beacons.append(beacon)
                    final.append(resulting_beacons)

        return tuple(final)

    def get_matching_points(
            constellation1: list[tuple[int, int, int]],
            constellation2: list[tuple[int, int, int]]
    ) -> tuple[tuple[int, ...], tuple[int, ...]]:
        raise NotImplementedError()

    scanners = {}
    for line in lines:
        name, beacons = parse_input(line)
        scanners[name] = beacons

    scanner_ids = list(scanners.keys())
    scanner_ids.sort()
    already_checked = []
    for scanner1 in scanner_ids:
        print(scanner1)
        for scanner2 in scanner_ids:
            if scanner1 == scanner2:
                continue

            id1, id2 = scanner1, scanner2
            if id1 > id2:
                id1, id2 = id2, id1
            if (id1, id2) in already_checked:
                continue
            already_checked.append((id1, id2))

            scanner1_constellation = scanners[id1]
            scanner2_constellation = scanners[id2]
            match = False
            matching_indices = None
            for id_1, pivot_point_1 in enumerate(scanner1_constellation):
                if match:
                    break
                for id_2, pivot_point_2 in enumerate(scanner2_constellation):
                    centered_constellation_1 = center_constellation_around_pivot(scanner1_constellation, pivot_point_1)
                    centered_constellation_2 = center_constellation_around_pivot(scanner2_constellation, pivot_point_2)

                    cc1_rotations = generate_all_rotations(centered_constellation_1)
                    cc2_rotations = generate_all_rotations(centered_constellation_2)

                    for rotation_1 in cc1_rotations:
                        if match:
                            break
                        for rotation_2 in cc2_rotations:
                            matching_point_indices = get_matching_points(rotation_1, rotation_2)
                            if len(matching_point_indices) >= 12:
                                match = True
                                matching_indices = matching_point_indices
                                break

                    if match:
                        break

    print(time.time() - ttt)


def task2():
    with open("d19input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
