# input:
# The first line contains an integer N, the total number of students.
# The second line contains the names of the columns in any order.
# The next  lines contains the marks, id, name and class, under their respective column names.
"""
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
"""
# output: 78.00
# Print the average marks of the list corrected to 2 decimal places.

# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://stackoverflow.com/questions/20263839/python-convert-a-string-to-arguments-list

from collections import namedtuple

student_List = []
N = int(input())
columns_names = input().split()

student = namedtuple('Student', columns_names)
for i in range(N):
    student_data = input().split()
    student_List.append( student(*student_data) )
print(
    round( sum(int(student.MARKS) for student in student_List )/N, 2)
)
