import sys
import time

title = "## Day 22: Sporifica Virus ##"
url = "https://adventofcode.com/2017/day/22"
expectedResultPart1 = 5246
expectedResultPart2 = 2512059

directions = [(0,-1),(1,0),(0,1),(-1,0)]

def partOne(input):
    grid = [[char for char in row] for row in input.splitlines()]
    map = {}
    offset = int(len(grid)/2)
    for y in range(len(grid)):
        for x in range(len(grid)):
            map[(x - offset, y - offset)] = grid[y][x]
    
    dir = 0 # up
    (x, y) = (0,0)

    bursts = 10000
    infection_count = 0
    while bursts > 0:
        bursts -= 1
        ch = '.'
        if (x, y) in map:
            ch = map[(x, y)]
        
        if ch == '#':
            dir = (dir + 1) % len(directions)
            map[(x, y)] = '.'
        else:
            infection_count += 1
            dir = (len(directions) + dir -1) % len(directions)
            map[(x, y)] = '#'
        
        (dx, dy) = directions[dir]
        (x, y) = (x + dx, y + dy)

    return infection_count

def partTwo(input):
    grid = [[char for char in row] for row in input.splitlines()]
    map = {}
    offset = int(len(grid)/2)
    for y in range(len(grid)):
        for x in range(len(grid)):
            map[(x - offset, y - offset)] = grid[y][x]
    
    dir = 0 # up
    (x, y) = (0,0)

    bursts = 10000000
    infection_count = 0
    while bursts > 0:
        bursts -= 1
        ch = '.'
        if (x, y) in map:
            ch = map[(x, y)]
        
        if ch == '#':
            dir = (dir + 1) % len(directions)
            map[(x, y)] = 'F'
        elif ch == 'F':
            dir = (dir + 2) % len(directions)
            map[(x, y)] = '.'
        elif ch == 'W':
            infection_count += 1
            map[(x, y)] = '#'
        else:
            dir = (len(directions) + dir -1) % len(directions)
            map[(x, y)] = 'W'
        
        (dx, dy) = directions[dir]
        (x, y) = (x + dx, y + dy)

    return infection_count

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
