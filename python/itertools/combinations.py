# input: HACK 2 
# A single line containing the string  and integer value  separated by a space.
# output:
""""
A
C
H
K
AC
AH
AK
CH
CK
HK
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

[S, k] = input().split()
all_k_combinations = []
for i in range(int(k)):
    subList = list(map(sorted, combinations(S,i+1)))
    subList.sort()
    all_k_combinations.extend( subList )
for item in all_k_combinations:
    print( "".join(item) )