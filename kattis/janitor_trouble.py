from math import sqrt
a, b, c, d = [float(x) for x in input().split()]
semiperimeter = (a + b + c + d) / 2
ans = 1
for i in [a, b, c, d]:
    ans *= (semiperimeter -  i)
print(ans ** 0.5)


