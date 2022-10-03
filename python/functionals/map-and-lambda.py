# input: 5
# output: [0, 1, 1, 8, 27]
# A list on a single line containing the cubes of the first  fibonacci numbers.

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a1, a2 = 0, 1
    fib_list = []
    if n == 0: return fib_list

    fib_list.append(a1)
    while len(fib_list) < n:
        fib_list.append(a2)
        a1, a2 = a2, a1+a2
        
    return(fib_list)
    
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))