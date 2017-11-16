def can_eat(dora, l, r, t):
    if dora <= l:
        return r - dora <= t
    if dora >= r:
        return dora - l <= t
    return r - l + min(dora - l, r - dora) <= t
for _ in range(int(input())):
    len_fld = int(input())    
    field   = input()
    time_limit = int(input())
    dorae = []
    cakes = []
    for i,v in enumerate(field):
        if v == "P":dorae.append(i)
        elif v == "*": cakes.append(i)
    print(dorae, cakes)    
    while dorae and cakes:
        dora = dorae.pop()
        l = r = cakes[-1]
        while cakes and can_eat(dora, cakes[-1], r, time_limit):
            l = cakes.pop()
    print("NO" if cakes else "YES")        
        
    
