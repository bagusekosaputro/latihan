#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    count_dist = {}
    duplicate = False
    min_distance = a[0]

    for i in range(len(a)):
        if a[i] not in count_dist:
            count_dist[a[i]] = i
        else:
            duplicate = True
            distance = abs(count_dist[a[i]] - i)
            if distance < min_distance:
                min_distance = distance

        i += 1

    if not duplicate:
        return -1
    return min_distance


if __name__ == '__main__':
    a = [7, 1, 3, 4, 1, 7]

    result = minimumDistances(a)
