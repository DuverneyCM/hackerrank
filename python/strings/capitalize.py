#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    """
    words = s.split() #split just save words, and delete all spaces
    cwords = [w.capitalize() for w in words ]
    print(cwords)
    return " ".join(cwords)
    """
    result = []
    for w in re.split(r'(\s+)', s):
        if w[0] == " ":
            result.append( w )
        else:
            result.append(w.capitalize())
            #result.append( w[0].upper() + w[1:].lower() )
    return "".join(result)
    
    
"""
if w[0].isnumeric():
            result.append(w.title())
            #result.append(w.capitalize())
        else:
            result.append(w.title())
            #result.append(w.capitalize())
            
    return (" ".join(result)).title()

        return " ".join(w.capitalize() for w in s.split())
    else:
        return " ".join(w.title() for w in s.split())
        #return s.title()

capitalized = [''] * len(name)
    for i in range(len(name)):
        capitalized[i] = name[i][0].upper() + name[i][1:]
"""
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
