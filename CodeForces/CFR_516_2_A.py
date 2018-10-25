a, b, c = [int(x) for x in input().split()]
need = 0
if (a + b) <= c:
    need += c - (a + b) + 1
if (a + c) <= b:
    need += b - (a + c) + 1
if (b + c) <= a:
    need += a - (b + c) + 1
print(need)


