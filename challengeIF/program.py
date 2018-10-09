#!/usr/bin/env python3
# Luke Song Andy Shin
# problem 1F

import sys

scores = [2, 3, 7]

def score_possible(wanted_score):
    result = [[] for _ in range(wanted_score + 1)]                          # result 2d matrix to store result for each score
    for index in range(1, wanted_score + 1):                                # iterate scores upto wanted_score
        for score in scores:                                                # iterate possible score combinations
            if (index - score) >= 0:
                if not result[index - score] and (index - score) == 0:      # when wanted_score is a intial case like score = 2, score = 3
                    result[index].append([score])
                else:
                    for comb in result[index - score]:                      # append previous score combination with current score and add to result list
                        comb = sorted(comb + [score])
                        if comb not in result[index]:
                            result[index].append(comb)
    return sorted(result[wanted_score])

if __name__ == '__main__':
    for score in sys.stdin:
        wanted_score = int(score.strip())
        possibility = score_possible(wanted_score)
        if possibility:
            if len(possibility) > 1:
                print("There are {} ways to achieve a score of {}:".format(len(possibility), wanted_score))
            else:
                print("There is 1 way to achieve a score of {}:".format(wanted_score))                      # account for grammar diff
            for comb in possibility:
                print(' '.join(str(i) for i in comb))
        else:
            print("There are 0 ways to achieve a score of {}:".format(wanted_score))
