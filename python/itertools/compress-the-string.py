# input: 1222311
# A single line of input consisting of the string S.

# output: (1, 1) (3, 2) (1, 3) (2, 1)
# (number of consecutive occurrences, character that occur)

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

S = input()
print(*[( len(list(g)), int(k) ) for k, g in groupby(S)])