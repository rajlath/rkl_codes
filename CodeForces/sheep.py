
n, m = [int(x) for x in input().split()]
arr=[input().replace('.','D') for i in [3]*n]
flag1 = any('WS' in x or 'SW' in x for x in  arr)
flag2 = any('WS' in x or 'SW' in x for x in  (''.join(t) for t in zip(*arr)))
if flag1 or flag2:
    print("No")
else:
    print("Yes")
    print("\n".join(arr))