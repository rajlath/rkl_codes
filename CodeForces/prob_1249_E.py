floors, c = [int(x) for x in input().split()]
stairs = [int(x) for x in input().split()]
lifts  = [int(x) for x in input().split()]
ts = 0
te = c
ans = [0]
for i in range(1, floors):
    ts, te = min(ts, te) + stairs[i - 1], min(ts + c, te) + lifts[i - 1]
    ans.append(min(ts, te))
print(*ans)