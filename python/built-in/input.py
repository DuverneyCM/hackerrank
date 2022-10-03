# input:
# The first line contains the space separated values of x and k.
# The second line contains the polynomial P.
"""
1 4
x**3 + x**2 + x + 1
"""
# output: true

# Enter your code here. Read input from STDIN. Print output to STDOUT
[x, k] = map(int, input().split())
print( eval(input()) == k )