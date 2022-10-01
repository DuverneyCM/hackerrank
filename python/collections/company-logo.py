#!/bin/python3

# input: aabbbccde
# output:
# Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.
"""
b 3
a 2
c 2
"""

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = Counter(input())
    abc = sorted(s.items(), key=lambda pair: (-pair[1], pair[0]))
    for i in abc[0:3]:
        print(*i)