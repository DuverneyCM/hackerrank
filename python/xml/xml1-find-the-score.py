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
# output: 5
# Output a single line, the integer score of the given XML document (number of attributes)


# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    return sum([len(child.attrib) for child in node.iter()])

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))