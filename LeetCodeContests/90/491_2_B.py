n = int(input())
s = sorted([int(x) for x in input().split()])
i = 0
while sum(s) < ((4.5) * n):
    s[i] = 5
    i += 1
print(i)

