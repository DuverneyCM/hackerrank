# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# input:
"""
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
"""

# output: 4
# total number of students who are subscribed to the English newspaper only

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, set_english = int(input()), set(map(int, input().split()))
m, set_french = int(input()), set(map(int, input().split()))
print( len(set_english - set_french) )  # - = .difference()
