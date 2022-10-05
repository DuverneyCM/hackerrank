# input:
# The first line contains an integer N, the number of inputs.
# N lines follow, each containing some string.
# A valid mobile number is a ten digit number starting with a 7, 8 or 9.
"""
2
9587456281
1252478965
"""
# output:
# print "YES" if it is a valid mobile number and "NO" if it is not on separate lines
"""
YES
NO
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
for i in range(N):      
    m = re.search(r"^[7|8|9][\d]{9}$",input().strip())
    if m: print("YES")
    else: print("NO")