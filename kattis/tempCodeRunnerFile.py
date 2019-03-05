need = [1, 1, 2, 2, 2, 8]
has = [int(x) for x in input().split()]
ans = [need[i] - has[i] for i in range(7)]
print(*ans)