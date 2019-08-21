n, k = [int(x) for x in input().split()]
elem = [int(x) for x in input().split()]
if k != 0:
    k = [1, 2][k % 2 == 0]
for i in range(k):
    curr_max = max(elem)
    elem = [curr_max - elem[i] for i in range(n)]
print(*elem)