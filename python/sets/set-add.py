# The first line contains an integer , the total number of country stamps.
# The next  lines contains the name of the country where the stamp is from.
# input: 
"""
7
UK
China
USA
France
New Zealand
UK
France 
"""
# output: 5

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
list_diff_countries = set()
for i in range(n):
    list_diff_countries.add(input())

print(len(list_diff_countries))

