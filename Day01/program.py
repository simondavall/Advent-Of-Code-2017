import sys
import array

title = "## Day 1: Inverse Captcha ##"
url = "https://adventofcode.com/2017/day/1"
expectedResultPart1 = 1393
expectedResultPart2 = 1292

def processInput(input):
    numbers = []
    for ch in input:
        if (ch.isdigit()):
            numbers.append(int(ch))
    return numbers

def partOne(input):
    tally = 0
    numbers = processInput(input)
    length = len(numbers)
    for i in range(length):
        if (input[i] == input[(i+1)%length]):
            tally += int(input[i])
    return tally

def partTwo(input):
    tally = 0
    numbers = processInput(input)
    length = len(numbers)
    offset = int(length / 2)
    for i in range(length):
        if (input[i] == input[(i+offset)%length]):
            tally += int(input[i])
    return tally

print(title)
print(url)
for filePath in sys.argv[1:]:
    print(f"\nFile: {filePath}")
    with open(filePath, 'r') as file:
        input = file.read()

    resultPartOne = partOne(input);
    print(f"Part 1 Result: {resultPartOne} in 0ms");

    resultPartTwo = partTwo(input);
    print(f"Part 2 Result: {resultPartTwo} in 0ms");

if (resultPartOne != expectedResultPart1 or resultPartTwo != expectedResultPart2):
        sys.exit(1)
