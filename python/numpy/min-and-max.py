# input:
# The first line of input contains space separated values of N and M.
# The next N lines contains M space separated integers.
"""
4 2
2 5
3 7
1 3
4 0
"""
# output:
# Compute the min along axis 0 and then print the max of that result.
"""
3
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

[N, M] = list(map(int, input().split()))
A = np.array([list(map(int, input().split())) for _ in range(N)])
print( np.max(np.min(A, axis = 1)) )