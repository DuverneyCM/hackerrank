# input:
# The first line contains two space separated integers, N and M.
# The next N lines contains M space separated integers of array A.
# The following N lines contains M space separated integers of array B.
"""
1 4
1 2 3 4
5 6 7 8
"""
# output:
# Print the result of each operation in the given order under Task.
"""
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

[N, M] = list(map(int, input().split()))
A = numpy.array([list(map(int, input().split())) for _ in range(N)])
B = numpy.array([list(map(int, input().split())) for _ in range(N)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)