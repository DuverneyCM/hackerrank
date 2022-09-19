# Input Format: a^b mod m
# The first line contains a, the second line contains b, and the third line contains m.
"""
3
4
5
"""
# output:
# pow(a,b)
# pow(a,b,m)

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))
print(pow(a,b,m))