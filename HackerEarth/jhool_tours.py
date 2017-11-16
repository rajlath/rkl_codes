'''
2
4 3
0 1
1 2
2 0
5 5
0 0
1 2
2 3
4 4
4 0
'''
for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    ranges = []
    for _ in range(m):
        s, e = [int(x) for x in input().split()]
        if s <= e:
            ranges.append((s+n, e+n))
        else:
            ranges.append((s, e+n)) 
          
    ranges.sort(key=lambda tup: tup[1])
    
    i = 0
    T = 0
    ok = True
    for i in range(len(ranges)):
        T = max(ranges[i][0], T)
        if ranges[i][1] < T:
            ok = False
        T+=1

    print("YES" if ok else "NO")
      
