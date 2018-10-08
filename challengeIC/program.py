#!/usr/bin/env python3
# Luke Song Andy Shin
# problem IC

import sys

def swap_permutation(line, n):
    result = []
    while n != 0 and line:
        last_max_index = len(line) - line[::-1].index(max(line)) - 1        # get index of last max number if there is a tie
        if line[last_max_index] != line[0]:                                 # if max does not occurs first, perform swap
            result.append(line[last_max_index])
            line[last_max_index], line[0] = line[0], line[last_max_index] 
            n -= 1
        else:                                                               # if max occurs first, does not perform swap
            result.append(line[last_max_index])
        line.pop(0)                                                         # pop max value from line
    return (result + line)

def make_line(first_line):
    line = input().strip().split()
    return list(map(int, line))

if __name__ == '__main__':
    while True:
        try:
            first_line = input()
            first_line = first_line.strip().split()
            line = make_line(first_line)
            result = swap_permutation(line, int(first_line[1]))
            print(' '.join(str(number) for number in result))
        except EOFError:
            exit()
