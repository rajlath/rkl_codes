l, r, a = [int(x) for x in input().split()]
if l == r:
    ans = l * 2 + ( a - a%2)
else:
   mins = min(l, r)
   maxs = max(l, r)
   diff = maxs - mins
   if diff < a:
       a -= diff
       e = a - a%2
       ans = maxs * 2 + e
   elif diff == a:
       ans = maxs * 2
   else:
       ans = (mins + a) * 2

print(ans)

