# input:
# The first line of input contains space separated values of N and M.
# The next N lines contains M space separated integers.
"""
2 2
1 2
3 4
"""
# output:
# Compute the sum along axis 0. Then, print the product of that sum.
"""
24
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

[N, M] = list(map(int, input().split()))
A = numpy.array([list(map(int, input().split())) for _ in range(N)])
print( numpy.prod(numpy.sum(A, axis = 0)) )