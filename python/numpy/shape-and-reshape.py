# input: 1 2 3 4 5 6 7 8 9
# A single line of input containing  space separated integers.

# output: 
# Print the X NumPy array.
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

my_array = numpy.array(list(map(int,input().split())))
print(numpy.reshape(my_array, (3,3)))