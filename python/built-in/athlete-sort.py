# input:
# The first line contains N and M separated by a space.
# The next N lines each contain M elements.
# The last line contains K.
"""
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
"""
# output:
# Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.
"""
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    sorted_arr = sorted(arr, key=lambda col: col[k])
    for row in sorted_arr:
        print(*row)