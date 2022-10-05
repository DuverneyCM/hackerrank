# input:
# The first line of input contains an integer N, the number of mobile phone numbers.
# N lines follow each containing a mobile number.
"""
3
07895462130
919875641230
9195969878
"""
# output:
# Print N mobile numbers on separate lines in the required format.
"""
+91 78954 62130
+91 91959 69878
+91 98756 41230
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def wrapper(f):
    def fun(l):
        # complete the function
        f(["+91 " + phone[-10:-5] + " " + phone[-5:] for phone in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 