import sys
import time

title = "## Day 13: Packet Scanners ##"
url = "https://adventofcode.com/2017/day/13"
expectedResultPart1 = 2264
expectedResultPart2 = 3875838

def processInput(input):
    return []

def get_scanner_range(n):
    first = list(range(n))
    second = first[1:-1]
    second.reverse()
    for i in second:
        first.append(i)
    return (first, len(first))

def partOne(input):
    lines = input.splitlines()
    scanner = {}
    depth = 0
    for line in lines:
        data = line.split(": ")
        scanner[int(data[0])] = int(data[1])
        depth = max([depth, int(data[0])])

    severity = 0
    for layer, r in scanner.items():
        scanner_range, range_length = get_scanner_range(r)
        if (scanner_range[layer % range_length] == 0):
            severity += layer * r
            
    return severity

def partTwo(input):
    lines = input.splitlines()
    scanner = {}
    depth = 0
    for line in lines:
        data = line.split(": ")
        scanner[int(data[0])] = get_scanner_range(int(data[1]))
        depth = max([depth, int(data[0])])

    severity = 0
    delay = 0
    layers = range(depth + 1)
    # sort scanners by range length so that the shorter ranges with a higher likelihood of
    # collisions exist are tried first
    sorted_scanner = dict(sorted(scanner.items(), key=lambda item: item[1][1]))
    while True:
        for layer, (scanner_range, range_length) in sorted_scanner.items():
            timer = layer + delay
            if (scanner_range[timer % range_length] == 0):
                # caught try next delay
                delay += 1
                break
        else:
            return delay

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
