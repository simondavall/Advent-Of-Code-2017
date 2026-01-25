import sys
import time

title = "## Day 16: Permutation Promenade ##"
url = "https://adventofcode.com/2017/day/16"
expectedResultPart1 = "iabmedjhclofgknp"
expectedResultPart2 = "oildcmfeajhbpngk"

def processInput(input):
    return []

def perform_dance(moves, programs):
    for move in moves:
        if move[0] == 's':
            pivot = len(programs) - int(move[1:])
            programs = programs[pivot:] + programs[:pivot]
            continue
        elif move[0] == 'x':
            nums = move[1:].split('/')
            a = int(nums[0])
            b = int(nums[1])
            (programs[a], programs[b]) = (programs[b], programs[a])
        elif move[0] == 'p':
            name = move[1:].split('/')
            a = programs.index(name[0])
            b = programs.index(name[1])
            (programs[a], programs[b]) = (programs[b], programs[a])
        else:
            assert False, f"Unknown dance move '{move[0]}'"

    return programs



def partOne(input):
    data = input.splitlines()
    assert len(data) == 2, f"Expected 2 vlaues, found:{len(data)}"
    programs = data[0].split(',')
    moves = data[1].rstrip('\n').split(',')

    programs = perform_dance(moves, programs)

    tally = 0
    return ''.join(programs)

def partTwo(input):
    data = input.splitlines()
    assert len(data) == 2, f"Expected 2 vlaues, found:{len(data)}"
    programs = data[0].split(',')
    moves = data[1].rstrip('\n').split(',')

    cache = set()
    repeats_after = 0
    # find out if dance repeats itself
    while True:
        state = (''.join(programs))
        if state in cache:
            # print(f"Found repeat after {repeats_after} rounds")
            break
        cache.add(state)

        programs = perform_dance(moves, programs)
        repeats_after += 1

    one_billion = 1000000000
    effective_loop = one_billion % repeats_after
    
    for _ in range(effective_loop):
        programs = perform_dance(moves, programs) 

    return ''.join(programs)

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
