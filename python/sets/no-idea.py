# input:
# The first line contains integers  and  separated by a space.
# The second line contains  integers, the elements of the array.
# The third and fourth lines contain  integers,  and , respectively.
"""
3 2
1 5 3
3 1
5 7
"""
# output:
# 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
[n, m] = map(int, input().split())
array = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for s in array:
    if s in A:
        happiness += 1
    if s in B:
        happiness -= 1

print(happiness)
