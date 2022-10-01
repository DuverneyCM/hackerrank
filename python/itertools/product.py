# input:
"""
1 2
3 4
"""
# output: (1, 3) (1, 4) (2, 3) (2, 4)

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*list(product(A,B)))