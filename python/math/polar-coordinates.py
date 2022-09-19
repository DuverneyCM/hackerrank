# Input Format
# A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.

# Output Format
# Output two lines: 
#   The first line should contain the value of r.
#   The second line should contain the value of phi.

# input:  1+2j
# output: (correct up 3 decimals)
#   2.23606797749979
#   1.1071487177940904

# Enter your code here. Read input from STDIN. Print output to STDOUT
#import math.complex

#import numpy as np
import math

z = complex(input())
print(abs(z))
print(math.atan2(z.imag,z.real))
#print(np.angle(z,True))