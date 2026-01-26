import sys
import time
import queue

title = "## Day 19: A Series of Tubes ##"
url = "https://adventofcode.com/2017/day/19"
expectedResultPart1 = "AYRPVMEGQ"
expectedResultPart2 = 16408

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def partOne(input):
    route = input.splitlines()
    (x, y) = (route[0].index('|'), 0)
    dir = 2 # down (0, 1)
    letters = []
    while True:
        # try stright ahead
        n_dir = dir
        success, (nx, ny) = try_direction(x, y, n_dir, route)
        if not success:
            # try left
            n_dir = (len(directions) + dir - 1) % len(directions)
            success, (nx, ny) = try_direction(x, y, n_dir, route)
            if not success:
                # try right
                n_dir = (dir + 1) % len(directions)
                success, (nx, ny) = try_direction(x, y, n_dir, route)
                if not success:
                    break # cannot progress
        if route[ny][nx].isalpha():
            letters.append(route[ny][nx])

        (x, y) = (nx, ny)
        dir = n_dir 

    return ''.join(letters)

def partTwo(input):
    route = input.splitlines()
    (x, y) = (route[0].index('|'), 0)
    dir = 2 # down (0, 1)
    steps = 0
    while True:
        steps += 1
        # try stright ahead
        n_dir = dir
        success, (nx, ny) = try_direction(x, y, n_dir, route)
        if not success:
            # try left
            n_dir = (len(directions) + dir - 1) % len(directions)
            success, (nx, ny) = try_direction(x, y, n_dir, route)
            if not success:
                # try right
                n_dir = (dir + 1) % len(directions)
                success, (nx, ny) = try_direction(x, y, n_dir, route)
                if not success:
                    break # cannot progress

        (x, y) = (nx, ny)
        dir = n_dir 

    return steps

def try_direction(x, y, dir, route):
    (dx, dy) = directions[dir]
    (nx, ny) = (x + dx, y + dy)
    if not is_in_bounds(nx, ny, len(route) - 1, len(route[0])) or route[ny][nx] == ' ':
        return False, (nx, ny)
    return True, (nx, ny) 

def is_in_bounds(x, y, height, width):
    return 0 <= x and x < width and 0 <= y and y < height


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
