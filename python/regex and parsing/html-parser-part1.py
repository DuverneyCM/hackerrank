# input:
# The first line contains integer N, the number of lines in a HTML code snippet.
# The next N lines contain HTML code.
"""
2
<html><head><title>HTML Parser - I</title></head>   
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
"""
# output:
# Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet
"""
Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        if attrs:
            print(*(f"-> {name} > {value}" for name, value in attrs), sep="\n")
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        if attrs:
            print(*(f"-> {name} > {value}" for name, value in attrs), sep="\n")

N = int(input())
htmlCode = '\n'.join([input() for x in range(N)])  
parser = MyHTMLParser()
parser.feed(htmlCode)
parser.close()