#!/usr/bin/env python3
# Luke Song Andy Shin
# Contest 1A

import sys

def see_sun(line):
    line = list(map(int, line))
    max_height = max(line)
    viewable = 0
    current_max = 0
    for height in line[::-1]:
        if height == max_height:
            viewable += 1
            break
        if current_max <= height:
            current_max = height
            viewable += 1
        else:
            continue
    return viewable
    
if __name__ == '__main__':
    for line in sys.stdin:
        print(see_sun(line.strip().split()))
