l, r = [int(x) for x in input().split()]
is_unique = lambda x:len(set([y for y in str(x)]))==len(str(x))
maxs = -1
answ = -1
for i in range(l, r+1):
    if is_unique(i):
        curr =  (r - i) * (i - l)
        if curr >= maxs:
            maxs = curr
            answ = i


print(answ)