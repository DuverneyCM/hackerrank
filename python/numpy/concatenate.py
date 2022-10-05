# input:
# The first line contains space separated integers N, M and P.
# The next N lines contains the space separated elements of the P columns.
# After that, the next M lines contains the space separated elements of the P columns.
"""
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4
"""
# output:
# Print the concatenated array of size (N + M)xP.
"""
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

[N, M, P] = list(map(int, input().split()))
arrayN = numpy.array([list(map(int, input().split())) for _ in range(N)])
arrayM = numpy.array([list(map(int, input().split())) for _ in range(M)])

print( numpy.concatenate((arrayN, arrayM), axis = 0) )