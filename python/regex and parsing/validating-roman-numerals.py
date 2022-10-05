# input: CDXXI
# output: True

# matches anything like: M, MM, MMM or null
thousands = 'M{0,3}'
# matches anything like: C, CC, CCC, CD, D, DC, DCC, DCCC and CM (900)
hundreds = '(CM|CD|D?C{0,3})' 
# matches anything like: X, XX, XXX, XL, L, LX, LXX, LXXX and XC (90)
tens = '(XC|XL|L?X{0,3})'
# matches anything like: I, II, III, IV, V, VI, VII, VIII and IX (9)
digits = '(IX|IV|V?I{0,3})' 

#regex_pattern = r""	# Do not delete 'r'.
regex_pattern = '^'+thousands+hundreds+tens+digits+'$'

import re
print(str(bool(re.match(regex_pattern, input()))))