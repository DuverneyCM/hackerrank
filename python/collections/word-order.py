# input:
# The first line contains the integer, n.
# The next n lines each contain a word.
"""
4
bcdef
abcdefg
bcde
bcdef
"""
# output:
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
"""
3
2 1 1
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

words = OrderedDict()
n = int(input())

for i in range(n):
    word = input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
print(*[value for value in words.values()])

# Curiously, also work, considering the order of items appear
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

words = defaultdict(int)
n = int(input())

for i in range(n):
    words[input()] += 1

print(len(words))
print(*[value for value in words.values()])
"""