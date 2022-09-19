# The first line of input contains an integer, .
# The second line contains  space-separated integers.
# The third line contains an integer, .
# The fourth line contains  space-separated integers.

# input:
"""
4
2 4 5 9
4
2 4 11 12
"""
# output:
"""
5
9
11
12
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
A = set(map(int, input().split()))
N = int(input())
B = set(map(int, input().split()))

sym_diff = A.difference(B)
sym_diff.update( B.difference(A) )
ordered_list = list(sym_diff)
ordered_list.sort()

for x in ordered_list:
    print(x) 
