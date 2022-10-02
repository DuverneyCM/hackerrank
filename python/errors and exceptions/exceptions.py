# input:
# The first line contains T, the number of test cases.
# The next T lines each contain the space separated values of a and b.
"""
3
1 0
2 $
3 1
"""
# output:
# Print the value of a/b.
# In the case of ZeroDivisionError or ValueError, print the error code.
""""
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
div_list = []
for _ in range(n):
    div_list.append(input().split())
for [num, den] in div_list:
    
    try:
        if den == '0':
            raise ZeroDivisionError("integer division or modulo by zero")
        elif not num.isdigit():
            raise ValueError(num)
        elif not den.isdigit():
            raise ValueError(den)
        else:
            print(int(num)//int(den))        
    except ZeroDivisionError as e:  # ZeroDivisionError
        print("Error Code:",e)
    except ValueError as symbol:
        print("Error Code: invalid literal for int() with base 10: '%s'" % symbol)

