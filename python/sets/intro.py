# input:
"""
10
161 182 161 154 176 170 167 171 170 174
"""
# output: 
# 169.375

def average(array):
    # your code goes here
    distint_heights = set(array)
    return sum(distint_heights)/len(distint_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)