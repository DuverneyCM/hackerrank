# input:
# The first line contains the integer N.
# The next N lines contains the N space separated elements of array A.
"""
2
1.1 1.1
1.1 1.1
"""
# output:
# print the determinant of A
"""
0.0
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

N = int(input())
A = np.array([list(map(float, input().split())) for _ in range(N)])
print( np.around(np.linalg.det(A),2) )