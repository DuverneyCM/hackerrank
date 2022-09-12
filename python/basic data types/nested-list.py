# input
"""
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""

# output
"""
Berry
Harry
"""

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append((name,score))
    
    groups = {}
    for name, score in records:
        if score not in groups:
            groups.update({score: [name]})
        else:
            groups[score].append(name)
    
    second_lower = sorted(list(groups.keys()))[1]
    groups[second_lower].sort()
    for name in groups[second_lower]:
        print(name)
    #sorted_groups = sorted(groups).
    #groups.sort(key = lambda x: x[1])
    #print(groups)
    #print(groups[second_lower])
