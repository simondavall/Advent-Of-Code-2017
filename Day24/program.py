import sys
import time
import copy

title = "## Day 24: Electromagnetic Moat ##"
url = "https://adventofcode.com/2017/day/24"
expectedResultPart1 = 1511
expectedResultPart2 = 1471

def process_input(input):
    components = [[int(n) for n in row.split('/')] for row in input.splitlines()]
    starts = []
    starts.extend((c, c[1]) if c[0] == 0 else (c, c[0]) for c in components if 0 in c)
    return components, starts

def partOne(input):
    components, starts = process_input(input)

    max_strength = 0
    for s in starts:
        new_available = [c for c in components if c is not s[0]]
        max_strength = find_strongest_path(s[1], sum(s[0]) , new_available, max_strength)

    return max_strength

def partTwo(input):
    components, starts = process_input(input)

    max_strength = 0
    max_length = 0
    for s in starts:
        new_available = [c for c in components if c is not s[0]]
        max_strength, max_length = find_longest_strongest_path(s[1], sum(s[0]), 1, new_available, max_strength, max_length)
    
    return max_strength

def get_valid_components(current, available_components):
    valid_components = []
    valid_components.extend((a, a[1]) if a[0] == current else (a, a[0]) for a in available_components if current in a)
    return valid_components

def find_strongest_path(current, strength, available, max_strength):
    valid_next_components = get_valid_components(current, available)

    if len(valid_next_components) == 0 and strength > max_strength:
        max_strength = strength
        return max_strength

    for nxt in valid_next_components:
        new_available = [c for c in available if c is not nxt[0]]
        max_strength = find_strongest_path(nxt[1], strength + sum(nxt[0]), new_available, max_strength)

    return max_strength

def find_longest_strongest_path(current, strength, length, available, max_strength, max_length):
    valid_next_components = get_valid_components(current, available)

    if len(valid_next_components) == 0:
        if length > max_length:
            max_length = length
            max_strength = strength
        elif length == max_length and strength > max_strength:
            max_strength = strength
        return max_strength, max_length

    for nxt in valid_next_components:
        new_available = [c for c in available if c is not nxt[0]]
        max_strength, max_length = find_longest_strongest_path(nxt[1], strength + sum(nxt[0]), length + 1, new_available, max_strength, max_length)

    return max_strength, max_length


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
