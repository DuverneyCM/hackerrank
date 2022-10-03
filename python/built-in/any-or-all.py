# input:
# The first line contains an integer N. N is the total number of integers in the list.
# The second line contains the space separated list of N integers.
"""
5
12 9 61 5 14 
"""
# output: True
# If all the integers are positive, then you need to check if any integer is a palindromic integer
# e.g. palindromic integer: 8265628, 11, 77, 8

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, numbers = int(input()), input().split()
print( all([int(x)>0 for x in numbers]) and any([x[0] == x[-1] for x in numbers]) )
#anyPalindromic = any([x[0] == x[-1]  for x in numbers])
#allPositives = all([int(x)>0 for x in numbers])