#!/usr/bin/env python3
# Luke Song Andy Shin
# challengeID

import sys

# helper function to greedly search if that distance is plantable
def plantable(pots, dist, flowers):
    prev_one = pots[0]                                              # prev plant is initially first plant
    plantable = 1                                                   # first plant is always planted
    for pot in pots:
        if (pot - prev_one) >= dist:        
            prev_one = pot
            plantable += 1
    return plantable >= flowers

# binary search list of possible distance and find out the max
def max_min(pots, flowers):
    left = 0
    right = pots[-1] - pots[0] + 1                                  # max dist is difference between greatest pot number and the smallest
    current_diff = 0
    while left < right:
        mid = (left + right) // 2
        if plantable(pots, mid, flowers):                           # if that distance is plantable check if its max and keep binary search  
            current_diff = max(current_diff, mid)
            left = mid + 1
        else:
            right = mid
    return current_diff - 1

if __name__ == '__main__':
    while True:
        try:
            first_line = input().strip().split()
            pots = []
            for _ in range(int(first_line[0])):
                pots.append(int(input().strip()))
            print(max_min(sorted(pots), int(first_line[1])))
        except EOFError:
            exit()
