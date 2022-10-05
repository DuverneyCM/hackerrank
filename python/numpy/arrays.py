# input: 1 2 3 4 -8 -10
# A single line of input containing space separated numbers.

# output: [-10.  -8.   4.   3.   2.   1.]
# print a reversed NumPy array with the element type float.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.flip(numpy.array(arr,float))
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)