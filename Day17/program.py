import sys
import time

title = "## Day 17: Spinlock ##"
url = "https://adventofcode.com/2017/day/17"
expectedResultPart1 = 2000
expectedResultPart2 = 10242889

def processInput(input):
    return []

def partOne(input):
    buffer = [0]
    step = int(input.strip('\n'))

    idx = 0
    for i in range(1, 2018):
        idx = ((idx + step) % len(buffer)) + 1
        buffer.insert(idx, i)

    return buffer[(idx + 1) % len(buffer)]

def partTwo(input):
    step = int(input.strip('\n'))

    idx = 0
    for i in range(1, 50000000):
        idx = ((idx + step) % i) + 1
        if idx == 1:
            value_after_zero = i

    return value_after_zero

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
