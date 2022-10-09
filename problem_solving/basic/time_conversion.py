#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    pm = True if (s[-2:]) == "PM" else False
    if pm:
        hour = 12 + int(s[0:2]) if 12 + int(s[0:2]) < 24 else int(s[0:2])
        return f"{hour}{s[2:8]}"
    else:
        if int(s[0:2]) == 12:
            return f"00{s[2:8]}"
        else:
            return s[0:8]


if __name__ == '__main__':
    s = "07:05:45PM"
    result = timeConversion(s)
