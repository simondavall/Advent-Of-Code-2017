import sys
import time

title = "## Day 11: Hex Ed ##"
url = "https://adventofcode.com/2017/day/11"
expectedResultPart1 = 743
expectedResultPart2 = 1493

def move(direction):
    match direction:
        case "n": return (0, -2)
        case "s": return (0, 2)
        case "se": return (2, 1)
        case "sw": return (-2, 1)
        case "ne": return (2, -1)
        case "nw": return (-2, -1)
        case _: assert False, f"Unknown direction '{direction}'"

def distance_from_origin(x, y):
    (x ,y) = (abs(x), abs(y))
    dx = int(x / 2)
    dy = int((y - dx) / 2)
    return dx + dy

def partOne(input):
    path = input.rstrip('\n').split(',')
    (x, y) = (0, 0)
    for dir in path:
        (dx, dy) = move(dir)
        (x, y) = (x + dx, y + dy)

    return distance_from_origin(x, y)

def partTwo(input):
    path = input.rstrip('\n').split(',')
    (x, y) = (0, 0)
    max_dist = 0
    for dir in path:
        (dx, dy) = move(dir)
        (x, y) = (x + dx, y + dy)
        cur_dist = distance_from_origin(x, y)
        if (cur_dist > max_dist):
            max_dist = cur_dist

    return max_dist

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
