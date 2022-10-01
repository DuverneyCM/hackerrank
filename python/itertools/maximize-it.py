# input:
# The first line contains  space separated integers  and .
# The next  lines each contains an integer , denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.
"""
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
"""
# output: 206
# combination with the maximum value


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

K, M = map(int, input().split())
sublists = []
for i in range(K):
    sublists.append( list(map(int, input().split())) )
    sublists[i].pop(0)

all_combs = list(product(*sublists))
all_results = [sum([pow(x, 2) for x in item])%M for item in all_combs]
print(max(all_results))