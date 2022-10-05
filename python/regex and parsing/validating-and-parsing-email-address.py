# input:
# The first line contains a single integer, n, denoting the number of email address.
# Each line i of the n subsequent lines contains a name and an email address as two space-separated values following this format:
"""
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
"""
# output:
# Print the space-separated name and email address pairs containing valid email addresses only
"""
DEXTER <dexter@hotmail.com>
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

n = int(input())

email_pattern = "^[a-z][\w\-\.]*@[a-z]+\.[a-z]{1,3}$"
for i in range(n):
    parsed_addr = email.utils.parseaddr(input())
    if re.search(email_pattern, parsed_addr[1]):
        print(email.utils.formataddr(parsed_addr)) 
        
"""
email_pattern = "^[<][a-z][\w\-\.]*@[a-z]+\.[a-z]{1,3}[>]$"
for i in range(n):
    name, email = input().split()
    m = re.match(email_pattern, email)
    if m:
        print(f"{name} {email}")
"""