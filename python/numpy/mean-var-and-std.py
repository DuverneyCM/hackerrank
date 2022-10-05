# input:
# The first line of input contains space separated values of N and M.
# The next N lines contains M space separated integers.
"""
2 2
1 2
3 4
"""
# output:
# First, print the mean along axis 1.
# Second, print the var along axis 0.
# Third, print the std by default, along the axis None.
"""
[ 1.5  3.5]
[ 1.  1.]
1.11803398875
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

[N, M] = list(map(int, input().split()))
A = np.array([list(map(int, input().split())) for _ in range(N)])
print( np.mean(A, axis = 1) )
print( np.var(A, axis = 0) )
print( np.around(np.std(A, axis = None),11) )