# input:
# The first line contains the space separated values of N and M.
# The next N lines contains the space separated elements of M columns.
"""
2 2
1 2
3 4
"""

# output:
# First, print the transpose array and then print the flatten.
"""
[[1 3]
 [2 4]]
[1 2 3 4]
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

[N, M] = list(map(int, input().split()))
np_matrix = numpy.array([list(map(int, input().split())) for i in range(N)])
print( numpy.transpose(np_matrix) )
print( np_matrix.flatten() )