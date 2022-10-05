# fix errors in the code
# input:
"""
3
programming is awesome
"""
# output:
# print the sum of scores of all words
# if the number of vowels (a,e,i,o,u,y) is even, then the word score is 2. Otherwise, the word score is 1.
"""
4
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1 #++score
    return score


n = int(input())
words = input().split()
print(score_words(words))