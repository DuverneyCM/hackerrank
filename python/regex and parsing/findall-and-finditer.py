# input: rabcdeefgyYhFjkIoomnpOeorteeeeet
# output: 
# all the substrings of S that contains 2 or more vowels.
# Also, these substrings must lie in between 2 consonants and should contain vowels only
"""
ee
Ioo
Oeo
eeeee
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()

vocal = 'aeiouAEIOU'
consonant = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
pattern = ''.join(['(?<=[',consonant,'])([',vocal,']{2,})(?=[',consonant,'])'])
matcher = re.findall(pattern, S)
try:
    print(*matcher, sep='\n') if matcher else print(-1)
except:
    print(-11)