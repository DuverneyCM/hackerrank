# input:
# The first line contains N, the number of code lines.
# The next  lines contains CSS Codes.
"""
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}
"""
# output:
# Output the color codes with '#' symbols on separate lines.
"""
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
fullcode = ""
for i in range(N):
    fullcode += '\n'+input()
matches = re.findall(r"(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})(?!\n| )", fullcode)
print("\n".join(matches))
# (?!\n| )          prevent tags
# (?=;|,|\)|\}|\])  look for next character to a color