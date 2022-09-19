# The first line contains integer , the number of elements in the set .
# The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer , the number of commands.
# The next  lines contains either pop, remove and/or discard commands followed by their associated value.

# input:
"""
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
"""
# output: 4

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    if command[0] == "remove":
        if int(command[1]) in s:
            s.remove( int(command[1]) )
    if command[0] == "discard":
        s.discard( int(command[1]) )
    #print(s)

print(sum(s))