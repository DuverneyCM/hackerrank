# input:
# The first line contains the integer, N.
# The next N lines each contain a line of the text.
# The text contains && and || symbols. Your task is to modify those symbols to the following:
# && -> and
# || -> or
# Neither && nor || occur in the start or end of each line.
"""
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
"""
# output:
"""
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def replace(match):
    
    if match.group(0)==' &&': return ' and'
    elif match.group(0)==' ||': return ' or'
    else: return str(match.group(0))

N = int(input())
code = '\n'.join([input() for x in range(N)])
print( re.sub(r"( [&&|\|\|]{2})(?= )", replace, code) )