mod, nb = [int(x) for x in input().split()]
cnt = 0
ans = -1
done = []
for i in range(nb):
    curr = int(input()) % mod
    if curr in done:
        ans = i + 1
        break
    else:
        done.append(curr)
print(ans)      
        
        
        
        