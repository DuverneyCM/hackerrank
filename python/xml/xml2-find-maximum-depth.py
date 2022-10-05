# input:
# The first line contains N, the number of lines in the XML document.
# The next N lines follow containing the XML document.
"""
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
"""
# output: 1
# Output a single line, the integer value of the maximum level of nesting in the XML document.


# Enter your code here. Read input from STDIN. Print output to STDOUT
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    [depth(element, level) for element in list(elem)]
    maxdepth = max(level, maxdepth)
    return maxdepth

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)