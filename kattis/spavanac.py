h, m = [int(x) for x in input().split()]
minutes = h * 60 + m  - 45
if minutes < 0:minutes += 1440
h, m = divmod(minutes, 60)
print(h, m)
