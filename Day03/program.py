import sys
import time
import array

title = "## Day 2: Corruption Checksum ##"
url = "https://adventofcode.com/2017/day/2"
expectedResultPart1 = 371
expectedResultPart2 = 369601

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dx1 = [1, 1, 0, -1, -1, -1, 0, 1]
dy1 = [0, -1, -1, -1, 0, 1, 1, 1]


def partOne(input):
    target = int(input.rstrip('\n'))

    memAddr = 1
    (x, y) = (0, 0)
    dir = 0
    increment = 1

    while True:
        for _ in range(2):
            for _ in range(increment):
                (x, y) = (x + dx[dir], y + dy[dir])
                memAddr += 1
                if memAddr == target:
                    return abs(x) + abs(y)
            dir = (dir + 1) % 4
        increment += 1

    return -1

def partTwo(input):
    target = int(input.rstrip('\n'))

    memAddr = 1
    (x, y) = (0, 0)
    dir = 0
    increment = 1

    grid = {}
    grid[(0, 0)] = 1

    while True:
        for _ in range(2):
            for _ in range(increment):
                val = 0
                (x, y) = (x + dx[dir], y + dy[dir])
                for i in range(8):
                    (nx, ny) = (x + dx1[i], y + dy1[i])
                    if (nx, ny) in grid:
                        val += grid[(nx, ny)]
                grid[(x, y)] = val
                if val > target:
                    return val
            dir = (dir + 1) % 4
        increment += 1

    return -1


print(title)
print(url)
for filePath in sys.argv[1:]:
    print(f"\nFile: {filePath}")
    with open(filePath, 'r') as file:
        input = file.read()

    start = time.perf_counter()
    resultPartOne = partOne(input);
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Part 1 Result: {resultPartOne} in {elapsed_ms:.3f}ms");

    start = time.perf_counter()
    resultPartTwo = partTwo(input);
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Part 2 Result: {resultPartTwo} in {elapsed_ms:.3f}ms");

if (resultPartOne != expectedResultPart1 or resultPartTwo != expectedResultPart2):
        sys.exit(1)
