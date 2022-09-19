# The first line contains , the number of students who have subscribed to the English newspaper.
# The second line contains  space separated roll numbers of those students.
# The third line contains , the number of students who have subscribed to the French newspaper.
# The fourth line contains  space separated roll numbers of those students.

# input:
"""
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
"""
# output: 5
# total number of students who have subscriptions to both English and French newspapers

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, set_english = int(input()), set(list(map(int, input().split())))
m, set_french = int(input()), set(list(map(int, input().split())))

print( len(set_english & set_french) )
