import sys
import time
import re

title = "## Day 25: The Halting Problem ##"
url = "https://adventofcode.com/2017/day/25"
expectedResultPart1 = 3362
expectedResultPart2 = 0

initial_pattern = r'^.+state\s(\w).\n.+after\s(\d+)\ssteps.$'
state_pattern = r'^In state (\w):\n.+value\sis\s(\d):\n.+value\s(\d).\n.+the\s(\w+).\n.+state\s(\w).\n.+value\sis\s(\d):\n.+value\s(\d).\n.+the\s(\w+).\n.+state\s(\w).'

def convert_move(str):
    if str == 'right':
        return 1
    else:
        return -1

def processInput(input):
    blocks = input.split('\n\n')
    matches = re.findall(initial_pattern, blocks[0])
    assert len(matches) == 1, f"Expected 1 matches. Found:{len(matches)}, Matches:{matches}"
    start = matches[0][0]
    steps = int(matches[0][1])

    states = {}
    for b in blocks[1:]:
        for match in re.finditer(state_pattern, b):
            states[match.group(1)] = \
                [\
                    (int(match.group(3)), convert_move(match.group(4)), match.group(5)),\
                    (int(match.group(7)), convert_move(match.group(8)), match.group(9))\
                ]
    return start, steps, states

def partOne(input):
    current_state, steps, states = processInput(input)
    cursor = 0
    tape = {}

    for _ in range(steps):
        state = states[current_state]
        if not cursor in tape:
            tape[cursor] = 0
        current_value = tape[cursor]
        write_value, cursor_increment, next_state = state[current_value]
        tape[cursor] = write_value
        cursor += cursor_increment
        current_state = next_state
        
    return sum(tape.values())

def partTwo(input):
    tally = 0
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
