
d = {}
for _ in range(int(input())):
    x, y = [int(x) for x in input().split()]
    d[(x, y)] = d.get((x, y), 0) + 1
d = sorted(d)    
for a, v in d:    
    print(a, d[(a, v)])
    
    
