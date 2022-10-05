# input:
# The first line contains an integer N, the number of lines in the HTML code snippet.
# The next N lines contain HTML code.
"""
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""
# output:
# Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.
"""
head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"{tag}")
        if attrs:
            print(*(f"-> {name} > {value}" for name, value in attrs), sep="\n")
    def handle_startendtag(self, tag, attrs):
        print(f"{tag}")
        if attrs:
            print(*(f"-> {name} > {value}" for name, value in attrs), sep="\n")

N = int(input())
htmlCode = '\n'.join([input() for x in range(N)])  
parser = MyHTMLParser()
parser.feed(htmlCode)
parser.close()