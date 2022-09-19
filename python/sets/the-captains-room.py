# The first line consists of an integer, , the size of each group.
# The second line contains the unordered elements of the room number list

# input:
"""
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
"""
# output: 8

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

k = int(input())
family_rooms = list(map(int, input().split()))

people_by_room = Counter(family_rooms)
print( *[room for room, no_people in people_by_room.items() if no_people == 1] )

"""
people_by_room = [(room, family_rooms.count(room)) for room in set(family_rooms)]
for (room, no_people) in people_by_room:
    if no_people == 1: print(room) 
"""