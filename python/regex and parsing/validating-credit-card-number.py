# input:
# The first line of input contains an integer N.
# The next N lines contain credit card numbers.
# It must start with a 4, 5 or 6.
# It must contain exactly 16 digits.
# It must only consist of digits (0-9).
# It may have digits in groups of 4, separated by one hyphen "-".
# It must NOT use any other separator like ' ' , '_', etc.
# It must NOT have 4 or more consecutive repeated digits.   
"""
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
"""
# output:
# Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'.
"""
Valid
Valid
Invalid
Valid
Invalid
Invalid
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
for i in range(N):
    card_number = input().strip()
    p_struct = "^[456][\d]{3}-?[\d]{4}-?[\d]{4}-?[\d]{4}$"
    card_number_only_digits = "".join(re.findall("\d+", card_number))
    max_3_repeats = r'((\d)(?!(\2){3})){16}'
    #max_3_repeats = r'(\d+)\1{3,}'
    
    m1 = re.search(p_struct, card_number)
    m2 = re.search(max_3_repeats, card_number_only_digits)
    
    if all([m1, m2]): print("Valid")
    else: print("Invalid")