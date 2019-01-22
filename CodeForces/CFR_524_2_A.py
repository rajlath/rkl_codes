nb_query = int(input())
for _ in range(nb_query):
    l, r = [int(x) for x in input().split()]
    y = r - l + 1
    x = y // 2
    if y & 1: x -= r
    if l % 2 == 0: x = -x
    print(x)
