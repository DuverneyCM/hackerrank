# input: 3 3
# A single line containing the space separated values of N (rows) and M (colums).

# output:
# Print the desired X array.
"""
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')
[N, M] = list(map(int, input().split()))
print( numpy.eye(N, M, k = 0) ) 