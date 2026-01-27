import sys
import time
import copy
import queue

title = "## Day 21: Fractal Art ##"
url = "https://adventofcode.com/2017/day/21"
expectedResultPart1 = 184
expectedResultPart2 = 2810258

def to_key(pattern):
    key = [''.join(row) for row in pattern]
    return '/'.join(key)

def flip(pattern):
    return pattern[::-1] 

def rotate(pattern):
    return [list(row) for row in zip(*pattern[::-1])]

find_matching_rule_cache = {}
def find_matching_rule(pattern, rules):
    key = to_key(pattern)
    if key in find_matching_rule_cache:
        return find_matching_rule_cache[key]

    copy_pattern = copy.deepcopy(pattern)
    for _ in range(2):
        for _ in range(4):
            rule_key = to_key(copy_pattern)
            if rule_key in rules:
                rule = rules[rule_key]
                find_matching_rule_cache[key] = rule
                return rule
            copy_pattern = rotate(copy_pattern)
        copy_pattern = flip(copy_pattern)
    assert False, f"No rule found for pattern. {pattern}"        

def rule_to_pattern(rule):
    raw_pattern = rule.split('/')
    return [list(row) for row in raw_pattern]

def split_to_2x2_blocks(pattern):
    blocks = []
    n = len(pattern)
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            block = [
                [pattern[i][j], pattern[i][j+1]],
                [pattern[i+1][j], pattern[i+1][j+1]]
            ]
            blocks.append(block)
    return blocks

def split_to_3x3_blocks(pattern):
    blocks = []
    n = len(pattern)
    for i in range(0, n, 3):
        for j in range(0, n, 3):
            block = [
                [pattern[i][j], pattern[i][j+1], pattern[i][j+2]],
                [pattern[i+1][j], pattern[i+1][j+1], pattern[i+1][j+2]],
                [pattern[i+2][j], pattern[i+2][j+1], pattern[i+2][j+2]]
            ]
            blocks.append(block)
    return blocks

def consolidate_to_pattern(blocks):
    if not blocks:
        return []
    block_size = len(blocks[0])
    k = len(blocks)
    grid_size = int(k ** 0.5)
    if grid_size * grid_size != k:
        raise ValueError("Number of blocks must form a square layout (e.g., 1, 4, 9, 16, ...)")
    n = block_size * grid_size
    pattern = [[0] * n for _ in range(n)]
    for idx, block in enumerate(blocks):
        i = (idx // grid_size) * block_size
        j = (idx % grid_size) * block_size
        for bi in range(block_size):
            for bj in range(block_size):
                pattern[i + bi][j + bj] = block[bi][bj]
    return pattern   

def get_rules(input):
    lines = input.splitlines()
    rules = {}
    for line in lines:
        data = line.split(" => ")
        assert len(data) == 2, f"Expected 2 data items. Found:{len(data)}, Data:{data}"
        rules[data[0]] = rule_to_pattern(data[1])
    return rules

def partOne(input):
    iterations = 5
    raw_pattern = [ ".#.", "..#", "###"]
    pattern = [list(row) for row in raw_pattern]
    rules = get_rules(input)

    while iterations > 0:
        iterations -= 1
        new_pattern = []

        if len(pattern) % 2 == 0:
            blocks = split_to_2x2_blocks(pattern)
        else:
            blocks = split_to_3x3_blocks(pattern)

        for p in blocks:
            rule = find_matching_rule(p, rules)
            new_pattern.append(rule)
        
        pattern = consolidate_to_pattern(new_pattern)

    count = sum(row.count('#') for pixels in pattern for row in pixels)
    return count

def partTwo(input):
    iterations = 18
    raw_pattern = [ ".#.", "..#", "###"]
    pattern = [list(row) for row in raw_pattern]
    rules = get_rules(input)

    while iterations > 0:
        iterations -= 1
        new_pattern = []

        if len(pattern) % 2 == 0:
            blocks = split_to_2x2_blocks(pattern)
        else:
            blocks = split_to_3x3_blocks(pattern)

        for p in blocks:
            rule = find_matching_rule(p, rules)
            new_pattern.append(rule)
        
        pattern = consolidate_to_pattern(new_pattern)

    count = sum(row.count('#') for pixels in pattern for row in pixels)
    return count

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
