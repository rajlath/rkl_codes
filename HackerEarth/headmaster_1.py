def check_unique(n):
    cnt = 0
    seen=[]
    alls = []
    while n!=0:
        n, c = divmod(n, 10)
        if c==0:continue
        if c in seen:
            return False
        else:            seen.append(c)

    return True

l, r = [int(x) for x in input().split()]
cnt = []
for i in range(l, r+1):
    if check_unique(i):cnt.append(i)
count = 0
print(cnt)
for i in cnt:
    cx = int(str(i).replace("0",""))
    print(cx)
    if cx in cnt:
        continue
    else:count += 1
print(count)

