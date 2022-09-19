# Constrain: 1 < N < 10
# input: 5
# output:
"""
1
121
12321
1234321
123454321
"""

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(*[j if j<i else i - j%i for j in range(1,2*i)], sep="")
    print((111111111//(10**(9-i)))**2) # 11111**5 == 123454321
    print(int('1'*i)**2)
    