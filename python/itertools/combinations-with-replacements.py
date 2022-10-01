# input: HACK 2 
# A single line containing the string  and integer value  separated by a space.
# output:
"""
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
from itertools import combinations_with_replacement

[S, k] = input().split()
comb_with_replace = []

comb_with_replace = list(map(sorted, combinations_with_replacement(S,int(k))))
comb_with_replace.sort()

for item in comb_with_replace:
    print( "".join(item) )