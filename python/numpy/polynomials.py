# input:
# The first line contains the space separated value of the coefficients in P.
# The second line contains the value of x.
"""
1.1 2 3
0
"""
# output:
# print the evaluation of the polynom P at the point x.
"""
3.0
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

polynom = list(map(float, input().split()))
x = float(input())
print( np.polyval(polynom, x) )