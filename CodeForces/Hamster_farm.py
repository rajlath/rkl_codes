n, k = [int(x) for x in input().split()]
wts = [int(x) for x in input().split()]
mins= [n%x for x in wts]
ans = wts[mins.index(min(mins))]
print(wts.index(ans)+1, n//ans)