# input:
# The first line contains an integer T, the number of test cases.
# The next T line(s) contains a string N.
"""
4
4.0O0
-1.00
+4.54
SomeRandomStuff
"""
# output:
# Output True or False for each test case.
# Number can start with +, - or . symbol.
# Number must contain at least  decimal value.
# Number must have exactly one . symbol.
# Number must not give any exceptions when converted using float(N).
"""
False
True
True
False
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input())
for _ in range(T):
    N = input()
    try:
        if re.fullmatch("^[+-]?[\d]*\.[\d]+$", N):
            float(N)
            print(True)
        else:
            print(False)
    except: 
        print(False)
