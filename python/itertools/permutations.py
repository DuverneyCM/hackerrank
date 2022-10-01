# input: HACK 2
# A single line containing the space separated string S and the integer value k >>   0 < k < len(S)
# output:
"""
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

[S, k] = input().split()
all_k_permutations = list(permutations(S,int(k)))
all_k_permutations.sort()
for item in all_k_permutations:
    print( "".join(item) )