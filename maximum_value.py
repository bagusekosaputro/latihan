#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMaximumValue' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER_ARRAY pos
#  3. LONG_INTEGER_ARRAY amount
#

def findMaximumValue(prices, pos, amount):
    maxValue = []
    for k, v in enumerate(pos):
        arr_pos = v-1
        arr = prices[arr_pos:]
        if len(arr) == 1 and arr[0] <= amount[k]:
            break

        count = sumValues(arr, amount[k])
        maxValue.append(count)

    return maxValue

def sumValues(arr, amount):
    total = arr[0]
    step = 0
    for i in arr[1:]:
        if total > amount:
            break
        total += i
        step += 1
    return step

if __name__ == '__main__':
    prices = [1, 2, 3, 4, 5]
    pos = [1, 3]
    amount = [5, 5]

    result = findMaximumValue(prices, pos, amount)
    print(result)
