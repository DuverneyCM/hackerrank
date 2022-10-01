# input:
# The first line contains the number of items, N.
# The next N lines contains the item's name and price, separated by a space.
"""
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
"""
# output:
# Print the item_name and the accumulate net_price in order of its first occurrence.
"""
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

product_list = OrderedDict()
N = int(input())
for i in range(N):
    item = input().split()
    product_name = " ".join(item[:-1])
    product_price = int(item[-1])
    if product_name in product_list:
        product_list[product_name] += product_price
    else:
        product_list[product_name] = product_price

for name, price in product_list.items():
    print(f"{name} {price}")