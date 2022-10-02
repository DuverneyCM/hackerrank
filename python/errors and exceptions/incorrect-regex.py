# input:
# The first line contains integer T, the number of test cases.
# The next T lines contains the string S.
"""
2
.*\+
.*+
"""
# output:
# Print "True" or "False" for each test case without quotes.
"""
True
False
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
#regex_list = []
for _ in range(n):
    #regex_list.append(input())
    
    try:
        re.compile(input())
        print("True")    
    except re.error:
        print("False")