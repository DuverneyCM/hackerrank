# input:
# The first line contains the integer N.
# The next N lines contains N space separated integers of array A.
# The following N lines contains N space separated integers of array B.
"""
2
1 2
3 4
1 2
3 4
"""
# output:
# Compute the min along axis 0 and then print the max of that result.
"""
[[ 7 10]
 [15 22]]
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

N = int(input())
A = np.array([list(map(int, input().split())) for _ in range(N)])
B = np.array([list(map(int, input().split())) for _ in range(N)])

print( A @ B ) #print (np.matmul(A,B))