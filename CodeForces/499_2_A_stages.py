nol, maxs = [int(x) for x in input().split()]
ins = sorted([ord(x) for x in input()])
last = 0
ans  = 0
for i in ins:
    if i - last > 1:
        ans += (i - 96)
        maxs -= 1
        last  = i
        if maxs ==0:break
#print(maxs)
print([-1, ans][maxs<=0])








