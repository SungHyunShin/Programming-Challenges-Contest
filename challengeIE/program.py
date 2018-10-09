#!/usr/bin/env python3
# Luke Song Andy Shin
# challenge1E

import sys
import itertools

def binary_string(length, count):
    result = []
    for positions in itertools.combinations(range(length), count):      # Generate possible places that 1 can be inserted
        binary_string = [0] * length
        for pos in positions:                                           # Add 1 to locations in binary_string
            binary_string[pos] = 1
        result.append(''.join(map(str, binary_string)))
    return sorted(result)

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    for index, line in enumerate(lines):
        line = line.strip().split()
        strings = binary_string(int(line[0]), int(line[1]))
        for string in strings:
            print(string)
        if index < len(lines) - 1:
            print()
