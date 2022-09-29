#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    count_dict = {}
    unique = 0
    for i in a:
        count_dict[i] = count_dict.get(i,0) + 1

    for i in a:
        if count_dict[i] == 1:
            unique = i

    return unique


if __name__ == '__main__':
    a = [1, 1, 2]
    result = lonelyinteger(a)
