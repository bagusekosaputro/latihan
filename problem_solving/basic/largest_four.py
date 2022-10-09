#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'largestFour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def largestFour(arr):
    print(sorted(arr)[-4:])


# Write your code here

if __name__ == '__main__':
    result = largestFour([4, 5, -2, 3, 1, 2, 6, 6])
