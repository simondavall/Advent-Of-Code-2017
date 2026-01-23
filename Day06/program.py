import sys
import time

title = "## Day 6: Memory Reallocation ##"
url = "https://adventofcode.com/2017/day/6"
expectedResultPart1 = 6681
expectedResultPart2 = 2392

def findLargestItemIndex(numbers):
    max = 0
    idx = 0
    for i, n in enumerate(numbers):
        if (n > max):
            max = n
            idx = i
    return (idx, max)

def partOne(input):
    numbers = list(map(int, input.rstrip('\n').split('\t')))
    tnumbers = tuple(numbers)
    seen = set()
    seen.add(tnumbers)
    steps = 0
    
    while True:
        steps += 1
        (idx, max) = findLargestItemIndex(numbers)
        numbers[idx] = 0

        while max > 0:
            idx = (idx + 1) % len(numbers)
            numbers[idx] += 1
            max -= 1

        tnumbers = tuple(numbers)
        if tnumbers in seen:
            return steps
        seen.add(tnumbers)

def partTwo(input):
    numbers = list(map(int, input.rstrip('\n').split('\t')))
    tnumbers = tuple(numbers)
    seen = {}
    seen[tnumbers] = 0
    steps = 0
    
    while True:
        steps += 1
        (idx, max) = findLargestItemIndex(numbers)
        numbers[idx] = 0

        while max > 0:
            idx = (idx + 1) % len(numbers)
            numbers[idx] += 1
            max -= 1

        tnumbers = tuple(numbers)
        if tnumbers in seen:
            prev = seen[tnumbers]
            return steps - prev
        seen[tnumbers] = steps

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
