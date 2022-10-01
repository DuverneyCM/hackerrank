# input:
# first line: length n and m of the groupA and groupB
"""
5 3
a
a
b
a
b
a
b
c
"""
# output:
# groupA positions where each item of groupB is in
"""
1 2 4
3 5
-1
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
groupA = defaultdict(lambda:[-1])
for i in range(n):
    c = input()
    if c in groupA:
        groupA[c].append(i+1)
    else:
        groupA[c] = [i+1]
for i in range(m):
    c = input()
    print(*groupA[c])