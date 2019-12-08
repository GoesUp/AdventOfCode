def part1(pixels, width, height):
    newPixels = []
    for i in range(0, len(pixels), width * height):
        newPixels.append(pixels[i:i + width * height])
    newNewPixels = []
    for i in newPixels:
        counter0 = 0
        counter1 = 0
        counter2 = 0
        for j in i:
            if j == "0":
                counter0 += 1
            elif j == "1":
                counter1 += 1
            elif j == "2":
                counter2 += 1
        newNewPixels.append((counter0, counter1 * counter2))
    minElement = min(newNewPixels)
    return minElement[1]


def part2(pixels, width, height):
    newPixels = []
    for i in range(0, len(pixels), width * height):
        newPixels.append(pixels[i:i + width * height])
    layerTables = []
    visibleImage = [[2 for _ in range(0, width)] for _ in range(0, height)]
    for i in newPixels:
        temp = []
        for j in range(0, height):
            temp.append(i[j * width:j * width + width])
        temp = [[int(w) for w in x] for x in temp]
        newVisibleImage = []
        for k, l in zip(visibleImage, temp):
            newRow = []
            for m, n in zip(k, l):
                if m == 2:
                    newRow.append(n)
                else:
                    newRow.append(m)
            newVisibleImage.append(newRow)
        visibleImage = newVisibleImage
    image = "".join(("".join("1" if j == 1 else " " for j in i)) + "\n" for i in visibleImage)
    return image[1:]


with open("day8.txt", "r") as file:
    pixels = file.read()
    print("Part 1:", part1(pixels, 25, 6))
    print("Part 2:\n", part2(pixels, 25, 6))
