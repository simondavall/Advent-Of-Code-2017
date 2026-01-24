import sys
import time
import queue

title = "## Day 12: Digital Plumber ##"
url = "https://adventofcode.com/2017/day/12"
expectedResultPart1 = 169
expectedResultPart2 = 179

def processInput(input):
    return []

def partOne(input):
    lines = input.splitlines()
    programs = {}
    for line in lines:
        data = line.split(" <-> ")
        programs[int(data[0])] = list(map(int, data[1].split(", ")))
    
    zeroBasedPrograms = set()
    q = queue.Queue()
    q.put(0)

    while not q.empty():
        id = q.get()
        zeroBasedPrograms.add(id)
        for child in programs[id]:
            if not child in zeroBasedPrograms:
                q.put(child)
       
    return len(zeroBasedPrograms)

def partTwo(input):
    lines = input.splitlines()
    programs = {}
    for line in lines:
        data = line.split(" <-> ")
        programs[int(data[0])] = list(map(int, data[1].split(", ")))
    
    visited = set()
    no_of_groups = 0

    for i in programs:
        if i in visited:
            continue

        currentGroup = set()
        q = queue.Queue()
        q.put(i)
        while not q.empty():
            id = q.get()
            currentGroup.add(id)
            for child in programs[id]:
                if not child in currentGroup:
                    q.put(child)
        visited.update(currentGroup)
        no_of_groups += 1

    return no_of_groups

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
