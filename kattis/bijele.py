need = [1, 1, 2, 2, 2, 8]
has = [int(x) for x in input().split()]
#print(need, has)
ans = [need[i] - has[i] for i in range(6)]
print(*ans)