#!/usr/bin/env python3
# Luke Song Andy Shin
# problem 1B

import sys

# determines if isomorphic and returns boolean
def isIsomorphic(w1,w2):
    w1 = list(w1)
    w2 = list(w2)
    w1D = dict()
    w2D = dict()

    # insert letters into dictionaries
    for letter in w1:
        if letter in w1D:
            w1D[letter] = w1D[letter] + 1
        else:
            w1D[letter] = 1
    for letter in w2:
        if letter in w2D:
            w2D[letter] = w2D[letter] + 1
        else:
            w2D[letter] = 1
                                        
    if len(w1D.keys()) != len(w2D.keys()):      # if the number of keys aren't the same, return false 
        return False
    else:                                       # iterate dict and compare values
        for i, j in zip(w1D, w2D):
            if w1D[i] != w2D[j]:
                return False
    return True

if __name__ == '__main__':
    lines = [line.rstrip().split(' ') for line in sys.stdin.readlines()]
    for line in lines:
        w1 = line[0]
        w2 = line[1]
        if isIsomorphic(w1,w2):
            print("Isomorphic")
        else:
            print("Not Isomorphic")
