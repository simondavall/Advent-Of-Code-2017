import sys
import time

title = "## Day 10: Knot Hash ##"
url = "https://adventofcode.com/2017/day/10"
expectedResultPart1 = 4480
expectedResultPart2 = "c500ffe015c83b60fad2e4b7d59dabc4"

def processInput(input):
    return []

def partOne(input):
    lengths = list(map(int, input.rstrip('\n').split(",")))
    numbers = list(range(256))
    cur = 0
    skip = 0
    for l in lengths:
        selection = []
        for i in range(cur, l + cur):
            selection.append(numbers[i % len(numbers)])
        selection.reverse()
        for i in range(cur, l + cur):
            numbers[i % len(numbers)] = selection[i - cur]
        cur += l + skip
        skip += 1

    return numbers[0] * numbers[1]

def partTwo(input):
    rounds = 64
    lengths = []
    for ch in input.rstrip('\n'):
        lengths.append(ord(ch))
    extra = [17, 31, 73, 47, 23]
    for n in extra:
        lengths.append(n)
    numbers = list(range(256))
    cur = 0
    skip = 0
    while rounds > 0:
        for l in lengths:
            selection = []
            for i in range(cur, l + cur):
                selection.append(numbers[i % len(numbers)])
            selection.reverse()
            for i in range(cur, l + cur):
                numbers[i % len(numbers)] = selection[i - cur]
            cur += l + skip
            skip += 1
        rounds -= 1

    idx = 0
    dense_hash = [0] * int(len(numbers) / 16)
    for i, n in enumerate(numbers):
        if (i % 16 == 0):
            dense_hash[int(i / 16)] = n
        else:
            dense_hash[int(i / 16)] ^= n 

    output = ""
    for n in dense_hash:
        output += f"{n:02x}"

    return output

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
