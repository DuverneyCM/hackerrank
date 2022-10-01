# input:
# The first line contains a single integer T, the number of test cases.
# For each test case, there are 2 lines.
# The first line of each test case contains n, the number of cubes.
# The second line contains n space separated integers, denoting the sideLengths of each cube in that order.
""""
2
6
4 3 2 1 3 4
3
1 3 2
"""
# output:
# For each test case, output a single line containing either Yes or No.
""""
yes
no
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

T = int(input())
block = []
for i in range(T):
    n = int(input())
    block = deque(map(int, input().split())) 
    
    isPilled = True
    topBlock = max(block[0], block[-1])
    while block:
        if block[0] >= block[-1]: currentBlock = block.popleft()
        else: currentBlock = block.pop()
        if topBlock >= currentBlock: topBlock = currentBlock
        else:
            isPilled = False
            break
    print("Yes") if isPilled == True else print("No")
    