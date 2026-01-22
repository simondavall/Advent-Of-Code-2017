import sys
import time
import array

title = "## Day 2: Corruption Checksum ##"
url = "https://adventofcode.com/2017/day/2"
expectedResultPart1 = 42299
expectedResultPart2 = 277

def processInput(input):
    rows = []
    lines = input.splitlines()
    for line in lines:
        numbers = []
        for n in line.split():
            numbers.append(int(n))
        rows.append(numbers)
    return rows

def partOne(input):
    checksum = 0
    rows = processInput(input)
    for row in rows:
        minVal = min(row)
        maxVal = max(row)
        checksum += maxVal - minVal         
    return checksum

def partTwo(input):
    checksum = 0
    rows = processInput(input)
    for row in rows:
        for i in range(len(row) - 1):
            a = row[i]
            for j in range (i + 1, len(row)):
                b = row[j]
                if (a % b == 0):
                    checksum += int(a / b)
                    break
                if (b % a == 0):
                    checksum += int(b / a)
                    break
            else:
                continue
            break
                
    return checksum

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
