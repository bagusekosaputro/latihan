#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sumMultiplier' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sumMultiplier(arr):
    result = 0
    sum_total = 0
    for i in arr:
        sum_total += i
    sum_total *= 2

    max_arr_value = max(arr)
    max_value = 0
    for i in arr:
        if i != max_arr_value:
            max_value = max_arr_value * i
            if max_value > sum_total:
                result = 1
                break
    return result


if __name__ == '__main__':
    result = sumMultiplier([2, 5, 6, -6, 16, 2, 3, 6, 5, 3])
    print(bool(result))