nb_roads = int(input())
H = [0] * nb_roads
V = [0] * nb_roads
ans = []
for i in range(nb_roads * nb_roads):
    h, v = [int(x) for x in input().split()]
    if h in H or v in V:
        continue
    else:        
        H.append(h)
        V.append(v)
        ans.append(i+1)
print(*ans)        
