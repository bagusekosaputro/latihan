#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    count_losses = []
    left = 0
    while left < len(price) - 1:
        right = left + 1
        print(left,right)
        if price[left] > price[right]:
            loss = price[left] - price[right]
            count_losses.append(loss)
        else:
            right += 1
        left += 1
    print(count_losses)


if __name__ == '__main__':
    price = [20, 7, 8, 2, 5]
    # result = minimumLoss(price)

    res = [ord(v) if k < 1 else ord(v) + ord(v) for k, v in enumerate("Close")]
    print(res)


