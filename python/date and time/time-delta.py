# input:
# The first line contains T, the number of testcases.
# Each testcase contains 2 lines, representing time t1 and time t2.
"""
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
"""
# output:
"""
25200
88200
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    ts1 = datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    ts2 = datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    seconds_delta = int(abs((ts2-ts1).total_seconds()))
    return str(seconds_delta)
    
    
if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "./output.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
