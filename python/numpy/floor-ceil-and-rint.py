# input:
# A single line of input containing the space separated elements of array A.
"""
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
"""
# output:
# On the first line, print the floor of A.
# On the second line, print the ceil of A.
# On the third line, print the rint of A.
"""
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.] 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')

A = numpy.array(list(map(float, input().split())))
print( numpy.floor(A) )
print( numpy.ceil(A) )
print( numpy.rint(A) )