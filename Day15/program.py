import sys
import time

title = "## Day 15: Dueling Generators ##"
url = "https://adventofcode.com/2017/day/15"
expectedResultPart1 = 0
expectedResultPart2 = 0

def processInput(input):
    return []

def partOne(input):
    start_values = input.splitlines()
    assert len(start_values) == 2, f"Expected 2 values, Found:{len(start_values)}"
    generatorA = int(start_values[0])
    generatorB = int(start_values[1])

    limit = 40000000
    mask = 0xffff
    tally = 0
    while limit > 0:
        generatorA = (generatorA * 16807) % 2147483647
        generatorB = (generatorB * 48271) % 2147483647
        if generatorA & mask == generatorB & mask:
            tally += 1
        limit -= 1

    return tally

def partTwo(input):
    start_values = input.splitlines()
    assert len(start_values) == 2, f"Expected 2 values, Found:{len(start_values)}"
    generatorA = int(start_values[0])
    generatorB = int(start_values[1])

    genA_values = []
    genB_values = []

    limit = 5000000
    mask = 0xffff
    tally = 0
    while len(genA_values) < limit or len(genB_values) < limit:
        generatorA = (generatorA * 16807) % 2147483647
        if (generatorA % 4 == 0):
            genA_values.append(generatorA)
        generatorB = (generatorB * 48271) % 2147483647
        if (generatorB % 8 == 0):
            genB_values.append(generatorB)
    
    for i in range(limit):
        if genA_values[i] & mask == genB_values[i] & mask:
            tally += 1

    return tally

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
