import sys
import time
import array

title = "## Day 4: High-Entropy Passphrases ##"
url = "https://adventofcode.com/2017/day/4"
expectedResultPart1 = 383
expectedResultPart2 = 265

def partOne(input):
    tally = 0
    phrases = input.splitlines()
    for phrase in phrases:
        words = phrase.split(' ')
        word_hash_set = set(words)
        if (len(word_hash_set) == len(words)):
            tally += 1

    return tally

def partTwo(input):
    phrases = input.splitlines()
    invalidCount = 0
    for phrase in phrases:
        words = phrase.split(' ')
        for i in range(len(words) - 1):
            first = ''.join(sorted(words[i]))
            for j in range(i + 1, len(words)):
                if (len(words[i]) != len(words[j])):
                    continue
                second = ''.join(sorted(words[j]))
                if (first == second):
                    invalidCount += 1
                    break; # invalid, don't need to check further
            else:
                continue
            break
    return len(phrases) - invalidCount

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
