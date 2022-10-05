# input:
# The first line contains the string S.
# The second line contains the string k to search.
"""
aaadaa
aa
"""
# output
# Print the tuple in this format: (start _index, end _index).
# If no match is found, print (-1, -1).
"""
(0, 1)
(1, 2)
(4, 5)
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()
k = input()

i = 0
m = re.search(k,S[i:])

if m:
    while m:
        print( (m.start()+i, m.end()+i-1) )
        i += m.start() + 1
        m = re.search(k,S[i:])
else:
    print((-1,-1))   