periods = int(input())
life = 0
for _ in range(periods):
    a, b = [float(x) for x in input().split()]
    if a == 0:
        break
    life += (a * b)
print(life)