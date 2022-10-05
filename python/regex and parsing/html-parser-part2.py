# input:
# The first line contains integer N, the number of lines in a HTML code snippet.
# The next N lines contain HTML code.
"""
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
"""
# output:
# Print the single-line comments, multi-line comments and the data in order of their occurrence from top to bottom in the snippet.
"""
>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data != '\n':
            if '\n' in data:
                print(f'>>> Multi-line Comment\n{data}')
            else:
                print(f'>>> Single-line Comment\n{data}')
    def handle_data(self, data):
        if data != '\n':
            print(f">>> Data\n{data}")
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()