

# Input Format
# The first line contains the first integer, a, and the second line contains the second integer, b.
# Sample Input:
"""
177
10
"""
# Smaple Output:
"""
17
7
(17, 7)
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())

print(a//b)
print(a%b)
print(divmod(a,b))