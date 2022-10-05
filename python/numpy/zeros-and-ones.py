# input: 3 3 3
# A single line containing the space-separated integers
# each integer represent the size of each dimension
# the number of intergers represent the number of dimensions

# output:
# Print the concatenated array of size (N + M)xP.
"""
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
dimensions = tuple(map(int, input().split()))
print( numpy.zeros(dimensions, dtype = numpy.int) )
print( numpy.ones(dimensions, dtype = numpy.int) )  