lens = int(input())
arrs = [int(x) for x in input().split()]
petu,ketu = 0, 0
while len(arrs) > 0:
    petu += arrs.pop(0)
    if len(arrs)>0:
        ketu += arrs.pop()
print(abs(petu - ketu))