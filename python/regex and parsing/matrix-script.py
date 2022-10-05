# input:
# The first line contains space-separated integers N (rows) and M (columns) respectively.
# The next N lines contain the row elements of the matrix script.
# Matrix consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&)
# If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability
"""
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
"""
# output: This is Matrix#  %!

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

code = ""
for i in zip(*matrix):
    code += ''.join(i)
decoded = re.sub(r'(?<=\w)([ !@#$%&]+)(?=\w)', " ", code)
print(decoded)