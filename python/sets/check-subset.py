# TASK
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

# INPUT
# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.

# CONSTRAINS
# 0 < T < 21
# 0 < number of elements in each set < 1001

# OUTPUT
# Output True or False for each test case on separate lines.

# input:
"""
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
"""

# output:
""""
True 
False
False
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))

    print(A.issubset(B))
    """
    is_A_in_B = True
    for x in A:
        if x not in B:
            is_A_in_B = False
    print(is_A_in_B)
    """