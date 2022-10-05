# fix errors in the code
# input:
# first line, there is a single integer q denoting the number of queries
# Each of the following q lines contains a stream_name followed by integer n, and it corresponds to a single test for your
"""
3
odd 2
even 3
odd 5
"""
# output:
# For each of the queries (stream_name, n), if the stream_name is even then print_from_stream(n) is called.
# Otherwise, if the stream_name is odd, then print_from_stream(n, OddStream()) is called.
"""
1
3
0
2
4
1
3
5
7
9
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())