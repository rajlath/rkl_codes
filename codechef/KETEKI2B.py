nb_pkts, k = [int(x) for x in input().split()]
value = [int(x) for x in input().split()]
maxs  = sum(value[:k])

curr  = maxs
l, r, = 0, k
while r < nb_pkts:
    current = curr - value[l] + value[r]
    print(current)
    maxs = max(maxs, current)
    curr = current
    l += 1
    r += 1
print(maxs)    