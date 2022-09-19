# Input Format
# The first line contains the length of side AB.
# The second line contains the length of side BC.

# Output Format
# Output MBC in degrees.

# input
"""
10
10
"""
# Output: 45°

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

AC = abs(complex(AB,BC))
MC = AC/2
angleMBC = angleC = math.acos(BC/AC)*180/math.pi 
print("{}\N{DEGREE SIGN}".format( round(angleMBC) ))
