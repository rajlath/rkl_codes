
nb_days = int(input())
now_a, now_b, now_c = 0, 0, 0
for _ in range(nb_days):
    a, b, c = [int(x) for x in input().split()]
    next_a = a + max(now_b, now_c)
    next_b = b + max(now_a, now_c)
    next_c = c + max(now_a, now_b)
    now_a, now_b, now_c = next_a, next_b, next_c
print(max(next_a, next_b, next_c))
