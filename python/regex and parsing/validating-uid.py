# input:
# The first line contains an integer , the number of test cases.
# The next  lines contains an employee's UID.
# It must contain at least  uppercase English alphabet characters.
# It must contain at least  digits ( - ).
# It should only contain alphanumeric characters ( - ,  -  &  - ).
# No character should repeat.
# There must be exactly  characters in a valid UID.
"""
2
B1CD102354
B1CDEF2354
"""
# output:
# print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines.
"""
Invalid
Valid
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
# Declare the patterns
no_repeats = r'(?!.*(.).*\1)' 
two_plus_uppercase = r'(?=(?:.*[A-Z]){2,})'
three_plus_digits = r'(?=(?:.*\d){3,})'
ten_alphanumeric = r'[\w]{10}'
filters = [no_repeats, two_plus_uppercase, three_plus_digits, ten_alphanumeric]

for i in range(0, N):
    uid = input()
    print('Valid') if all([re.match(f, uid) for f in filters]) else print('Invalid')