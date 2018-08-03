noe, r = [int(x) for x in input().split()]
arr    = [int(x) for x in input().split()]

mapA = {}
mapB = {}
cnt  = 0
cnt2 = 0
cnt1 = 0
for n in arr:
    if n % r == 0:
        pre = n // r
        if pre in mapB:cnt += mapB[pre]
        if pre in mapA:
            mapB[n] = mapB.get(n, mapB.get(n, 0))+mapA[pre]
    mapA[n] = mapA.get(n, 0) + 1
    #print(mapA, mapB)
print(cnt)
