nod, k = [int(x) for x in input().split()]
temps  = [int(x) for x in input().split()]
if k == 1: print(max(temps))
else:
    maxs = sum(temps) / nod
    l = 0
    r = l + k
    while l < r:
        avg = temps[l:r+ 1]
        maxs= max(maxs, )
