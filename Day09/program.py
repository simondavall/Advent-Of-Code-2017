import sys
import time

title = "## Day 9: Stream Processing ##"
url = "https://adventofcode.com/2017/day/9"
expectedResultPart1 = 12396
expectedResultPart2 = 6346

def processInput(input):
    return []

def partOne(input):
    is_garbage = False
    i = 0
    level = 0
    total = 0
    while i < len(input):
        ch = input[i]
        if ch == '!':
            i += 2
            continue
        if is_garbage:
            if ch == '>':
                is_garbage = False
        else:
            if ch == '{':
                level += 1
                total += level
            elif ch == '<':
                is_garbage = True
            elif ch == '}':
                level -= 1
        i += 1
            
    return total

def partTwo(input):
    is_garbage = False
    i = 0
    garbage_count = 0
    while i < len(input):
        ch = input[i]
        if ch == '!':
            i += 2
            continue
        if is_garbage:
            if ch == '>':
                is_garbage = False
            else:
                garbage_count += 1
        else:
            if ch == '<':
                is_garbage = True
        i += 1
    return garbage_count

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
