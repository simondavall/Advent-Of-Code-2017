import sys
import time
import queue

title = "## Day 14: Disk Defragmentation ##"
url = "https://adventofcode.com/2017/day/14"
expectedResultPart1 = 8106
expectedResultPart2 = 1164

disk = []

def partOne(input):
    disk.clear()
    tally = 0
    for i in range(128):
        rounds = 64
        hash_input = []
        key_string = input.rstrip('\n') + f"-{i}"
        for ch in key_string:
            hash_input.append(ord(ch))

        extra = [17, 31, 73, 47, 23]
        for n in extra:
            hash_input.append(n)

        numbers = list(range(256))
        cur = 0
        skip = 0
        while rounds > 0:
            for h in hash_input:
                selection = []
                for i in range(cur, h + cur):
                    selection.append(numbers[i % len(numbers)])
                selection.reverse()
                for i in range(cur, h + cur):
                    numbers[i % len(numbers)] = selection[i - cur]
                cur += h + skip
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

        binary_output = ""
        for h in output:
            binary_output += f"{int(h, 16):04b}"

        disk.append(list(binary_output))
        tally += binary_output.count("1")

    return tally

def isInBounds(x, y, height, width):
    return 0 <= x and x < width and 0 <= y and y < height

def partTwo(input):
    directions = [(0,-1),(1, 0),(0, 1),(-1, 0)]
    height = 128
    width = 128
    visited = set()
    region_count = 0
    for y in range(height):
        for x in range(width):
            if (x, y) in visited or disk[y][x] == '0':
                continue
            visited.add((x, y))
            region_count += 1
            q = queue.Queue()
            q.put((x, y))
            while not q.empty():
                (tx, ty) = q.get()
                disk[ty][tx] = region_count
                for dx, dy in directions:
                    (nx, ny) = (tx + dx, ty + dy)
                    if (nx, ny) in visited:
                        continue
                    visited.add((nx, ny))
                    if not isInBounds(nx, ny, height, width) or disk[ny][nx] == '0':
                        continue
                    q.put((nx, ny))

    return region_count

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
