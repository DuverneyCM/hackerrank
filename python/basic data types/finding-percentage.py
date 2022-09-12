# input
"""
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
"""

# output
# 56.00


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    mean = 0.0
    for score in student_marks[query_name]:
        mean += score
    mean /= len(student_marks[query_name])
    formatted_float = "{:.2f}".format(mean)
    #print("{:.2f}".format(mean))
    print(formatted_float)