# input:
"""
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""

# output
"""
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""



if __name__ == '__main__':
    N = int(input())
    listA = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            listA.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(listA)
        elif command[0] == "remove":
            listA.remove(int(command[1]))
        elif command[0] == "append":
            listA.append(int(command[1]))
        elif command[0] == "sort":
            listA.sort()
        elif command[0] == "pop":
            listA.pop()
        elif command[0] == "reverse":
            listA.reverse()