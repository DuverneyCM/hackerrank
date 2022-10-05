# input:
# The first line contains the space separated elements of array A.
# The second line contains the space separated elements of array B.
"""
0 1
2 3
"""
# output:
# First, print the inner product.
# Second, print the outer product.
"""
3
[[0 0]
 [2 3]]
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))
print( np.inner(A, B) )
print( np.outer(A, B) )