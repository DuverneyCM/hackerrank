# input:
# The first line of input is the integer N, the number of email addresses.
# N lines follow, each containing a string with an email address.
"""
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
"""
# output: ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']


import re
def fun(s):
    # return True if s is a valid email, else return False
    return re.match(r'^[\w-]+@[^\W_]+\.[a-zA-Z]{1,3}$', s, re.I)
    #return re.match(r'^[a-z][\w-]*@[a-z0-9]+\.[a-z]{1,3}$', s, re.I)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)