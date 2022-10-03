# input:
# The first line contains  and  separated by a space.
# The next  lines contains the space separated marks obtained by students in a particular subject.
"""
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
"""
# output:
# Print the averages of all students on separate lines.
# The averages must be correct up to  decimal place.
"""
90.0 
91.0 
82.0 
90.0 
85.5 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
scores = []
for i in range(X):
    try: score = map(float, input().split())
    except: pass
    scores.append( score )

for col in zip(*scores):
    average = sum(col)/X 
    print( average )