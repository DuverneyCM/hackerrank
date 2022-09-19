# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next  lines are divided into  parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.

# input:
"""
 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
"""

# output:
# sum of elements in set A.


# Enter your code here. Read input from STDIN. Print output to STDOUT
a, setA = int(input()), set(map(int, input().split()))
n = int(input())

for _ in range(n):
    [op, no_elems] = input().split()
    #no_elems = int(no_elems) 
    setB = set(map(int, input().split()))
    """
    if (op == "intersection_update"):
        setA &= setB
        #setA.intersection_update(setB)
    if (op == "update"):
        setA |= setB
        #setA.update(setB)
    if (op == "symmetric_difference_update"):
        setA ^= setB
        #setA.symmetric_difference_update(setB)
    if (op == "difference_update"):
        setA -= setB
        #setA.difference_update(setB)
    """
    #print(setA)
    eval( "".join(["setA.",op,"(setB)"]) )

print(sum(setA))
