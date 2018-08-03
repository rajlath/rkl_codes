'''
#!/usr/bin/python

def ia(): return map(int, raw_input().split())

n, k = ia()
p = ia()
c = ia()

h = []
P = zip(p, c, xrange(n))
P.sort()

lst = [None] * n
h = []
for p, c, i in P:
    ans = c + sum(h)
    lst[i] = ans
    h.append(c)
    h.sort(reverse=True)
    h = h[:k]

print " ".join(map(str, lst))

4 2
4 5 9 7
1 2 11 33
'''
nk, k = [int(x) for x in input().split()]
knights = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]

data = sorted(zip(knights, coins, range(nk)))
have = [0] * nk
selected = []
for p, c, i in data:
    ans = c + sum(selected)
    have[i] = ans
    selected.append(c)
    selected = sorted(selected, reverse=True)[:k]
print(*have)






