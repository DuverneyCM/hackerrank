# input: ..12345678910111213141516171820212223
# output: 1
# print the most repeated character

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

m = re.search(r'([^\W_])\1+', input().strip())
try:
    print(*m.group(1) if m else -1)
except:
    print("-1")

# print(collections.Counter(s).most_common(1)[0])

# self.repeat_regexp = re.compile(r'(\w)(\1{2,})')
# self.repl = r'\1'

# d = collections.defaultdict(int)
# for c in s: d[c] += 1
# print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0])

# all_matches = re.findall(r'([^\W_])', input().strip())


