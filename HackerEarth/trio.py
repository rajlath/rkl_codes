
n, m = [int(x) for x in input().split()]
arr  = [int(x) for x in input().split()]
mods = {}
ans = 0
for x in arr:
    y = x%m
    mods[y] = mods.get(y, 0) + 1
print(mods)    
for i in range(m+1):    
    for j in range(i+1, m+1):
        md = (m - (i+j)%m)%m
        if md > i and md > j:
            ans += mods[i] * mods[j] * mods[md]
    md = (m - (2*1)%m)%m
    if md != i and i != 0:
        ans += ((mods[i] * (mods[i]-1))/2  * mods[md])
    else:
        ans += (mods[i] * (mods[i]-1) * (mods[i]-2))/6
print(ans)                
        
            
