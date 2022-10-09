#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i,j,k):
    counts = 0
    while i <= j:
        n = str(i)
        l = len(n)
        reverse_no = ""
        while l > 0:
            reverse_no += (n[l - 1])
            l -= 1
        diff = abs(i - int(reverse_no))

        if diff % k == 0:
            counts += 1

        i += 1

    return counts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')

    first_multiple_input = input().rstrip().split()

    i = int(20)

    j = int(23)

    k = int(6)

    result = beautifulDays(i,j,k)

