# input: 
"""
AABCAAADA
3
"""
# output:
"""
AB
CA
AD
""" 

import textwrap

def merge_the_tools(string, k):
    # your code goes here
    list_substr = textwrap.wrap(string, k)
    for ss in list_substr:
        txt = ""
        for c in ss:
            if c not in txt:
                txt += c
        print(txt)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)