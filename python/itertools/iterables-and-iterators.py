# input:
# Size list N, list of characters, number of attemps K
"""
4
a a c d
2
"""
# output: 0.8333 probability that found 'a' in K attemps



# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

def probability_of_find_a_with_K_attemps(letters_list, letter, K ):
    combs = list(combinations(letters, K))
    number_of_occurs = sum(1 if letter in sublist else 0 for sublist in combs)
    return number_of_occurs / len(combs)

N = int(input())
letters = input().split()
K = int(input())

print ( probability_of_find_a_with_K_attemps(letters, 'a', K) )