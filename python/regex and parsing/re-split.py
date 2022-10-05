# input: 100,000,000.000
# string with integer digits and commas ',' and dots '.'

# output:
# splitted string by the tokens ',' and '.'
"""
100
000
000
00
"""

regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))