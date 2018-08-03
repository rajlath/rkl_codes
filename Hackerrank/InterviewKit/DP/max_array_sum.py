noe = int(input())
arr = [int(x) for x in input().split()]
res = 0
usesum = 0
dontuse= 0
for x in arr:
    next_use = dontuse + x
    res = max(res, next_use)
    next_dont= max(usesum, dontuse)
    usesum = next_use
    dontuse = next_dont
print(res)