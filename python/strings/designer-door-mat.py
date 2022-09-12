#https://stackoverflow.com/questions/15286401/print-multiple-arguments-in-python

# input: 9 27
# output:
"""
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
[N, M] = map(int, input().split())
#print(f"{N} and {M}")

# 0 1 2 3 4 5 6 7 8     
# 1 3 5 7 9 7 5 3 1     > N - 2*abs(N//2 - i)
# 4 3 2 1 0 1 2 3 4     > abs(N//2 - i)
# center = N//2

for i in range(N):
    if (i == N//2):
        print("WELCOME".center(M,'-'))
    else:
        l=r= '-'*(3*abs(N//2 - i))
        c= ".|."*(N - 2*abs(N//2 - i))
        print(f"{l}{c}{r}")

