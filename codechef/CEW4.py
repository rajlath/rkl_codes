n = int(input())
deed= [int(x) for x in input().split()]

pos = [0] * (n+1)
zer = [0] * (n+1)
neg = [0] * (n+1)
poe = [0] * (n+1)
nee = [0] * (n+1)

for i, v in enumerate(deed):
    pos[i] = pos[i-1]
    zer[i] = zer[i-1]
    neg[i] = neg[i-1]
    poe[i] = poe[i-1]
    nee[i] = nee[i-1]
    if v < 0: neg[i] += 1
    if v ==0: zer[i] += 1
    if v >=0: pos[i] += 1
    if v ==1: poe[i] += 1
    if v ==-1:noe[i] += 1
for _ in range(int(input())):
    l, r = [int(x)-1 for x in input().split()]
    if l == r:
        print(1)
    else:
        negi = neg[r] - neg[l-1]
        zeri = zer[r] - zer[l-1]
        posi = pos[r] - pos[l-1]
        poei = poe[r] - poe[l-1]
        neei = nee[r] - nee[l-1]

        ans = posi
        if negi%2==0: ans += negi
        else:
            if poei >= 1:
                ans += negi + 1
            else:
                ans += negi - 1
        if ans == 0:
            if poei > 1 and neei == 0:
                ans = 2
            else:
                ans = 1
        print(ans)



