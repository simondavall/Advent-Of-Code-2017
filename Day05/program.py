import sys
import time
import array

title = "## Day 5: A Maze of Twisty Trampolines, All Alike ##"
url = "https://adventofcode.com/2017/day/5"
expectedResultPart1 = 326618
expectedResultPart2 = 21841249

def processInput(input):
    numbers = []
    for str in input.splitlines():
        numbers.append(int(str))
    return numbers

def partOne(input):
    jumps = processInput(input)
    ip = 0
    steps = 0

    while ip < len(jumps):
        steps += 1
        currJump = jumps[ip]
        jumps[ip] += 1
        ip += currJump

    return steps

def partTwo(input):
    jumps = processInput(input)
    ip = 0
    steps = 0

    while ip < len(jumps):
        steps += 1
        currJump = jumps[ip]
        if (jumps[ip] >= 3):
            jumps[ip] -= 1
        else:
            jumps[ip] += 1
        ip += currJump

    return steps


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
