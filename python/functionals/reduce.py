# input:
# First line contains n, the number of rational numbers.
# The ith of next n lines contain two integers each, the numerator( Ni ) and denominator( Di ) of the ith rational number in the list.
"""
3
1 2
3 4
10 6
"""
# output: 5 8
# Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)