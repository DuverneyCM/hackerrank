# Input Format
# The first line contains the space separated elements of set A.
# The second line contains integer n, the number of other sets.
# The next n lines contains the space separated elements of the other sets.
"""
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
"""
# Output: 
# Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())

is_superset_of_all = True
for i in range(n):
    B = set(map(int, input().split()))
    if not A.issuperset(B):
        is_superset_of_all = False
print(is_superset_of_all)