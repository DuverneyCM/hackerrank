# input: Sorting1234
# A single line of input contains the string S

# output: ginortS1324
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.


# Enter your code here. Read input from STDIN. Print output to STDOUT
S = list(input())
sortedS = sorted(S, key=lambda c: (c.isdigit(), c.isdigit() and int(c) % 2 == 0, c.isupper(), c.islower(), c))

print( "".join(sortedS) )