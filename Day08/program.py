import sys
import time
import re

title = "## Day 8: I Heard You Like Registers ##"
url = "https://adventofcode.com/2017/day/8"
expectedResultPart1 = 6012
expectedResultPart2 = 6369

def condition_satisfied(operator, a, b):
    match operator:
        case "<":
            return a < b
        case ">":
            return a > b
        case "==":
            return a == b
        case "!=":
            return a != b
        case ">=":
            return a >= b
        case "<=":
            return a <= b
        case _:
            assert False, f"Unknown operator {operator}"

def setValues(match):
    return match.group(1), match.group(2), int(match.group(3)),\
        match.group(4), match.group(5), int(match.group(6))

def partOne(input):
    registers = {}
    for match in re.finditer(r'^(\w+)\s(\w+)\s(-?\d+)\sif\s(\w+)\s(.+)\s(-?\d+)$', input, re.MULTILINE):
        reg, action, amount, operandA, operator, operandB = setValues(match)

        if not operandA in registers:
            registers[operandA] = 0
        if not reg in registers:
            registers[reg] = 0

        if (condition_satisfied(operator, registers[operandA], operandB)):
            if (action == 'inc'):
                registers[reg] += amount
            else:
                registers[reg] -= amount

    return max(registers.values())

def partTwo(input):
    registers = {}
    maxValue = 0
    for match in re.finditer(r'^(\w+)\s(\w+)\s(-?\d+)\sif\s(\w+)\s(.+)\s(-?\d+)$', input, re.MULTILINE):
        reg, action, amount, operandA, operator, operandB = setValues(match)

        if not operandA in registers:
            registers[operandA] = 0
        if not reg in registers:
            registers[reg] = 0

        if (condition_satisfied(operator, registers[operandA], operandB)):
            if (action == 'inc'):
                registers[reg] += amount
            else:
                registers[reg] -= amount
        if (registers[reg] > maxValue):
            maxValue = registers[reg]

    return maxValue

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
