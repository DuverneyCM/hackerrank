# input:
# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.
"""
6
append 1
append 2
append 3
appendleft 4
pop
popleft
"""
# output: 1 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()

N = int(input())
for i in range(N):
    cmd = input().split()
    if len(cmd) == 1:
        eval( "".join(["d.",cmd[0],"()"]) )
    else:
        eval( "".join(["d.",cmd[0],"(",cmd[1],")"]) )

print(*d)
