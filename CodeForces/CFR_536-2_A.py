nb_elements = int(input())
elements    = sorted([int(x) for x in input().split()])
a = elements[:nb_elements//2]
b = elements[nb_elements//2:][::-1]
ans = sum([(x+y) ** 2 for x, y in zip(a, b)])
print(ans)