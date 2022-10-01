# input:
# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.
""""
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
"""
# output: 200


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

total = 0
X = int(input())
shoesList = Counter(map(int,input().split()))
N = int(input())
for i in range(N):
    [shoe_size, price] = list(map(int,input().split()))
    if shoe_size in shoesList:
        shoesList -= Counter([shoe_size])
        total += price
        #print(shoesList)
print(total)
