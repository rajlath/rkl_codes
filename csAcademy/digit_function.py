def F(x):
    x -= sum([int(a) for a in str(x)])
    return x

n = int(input())
cnt = 1
while n > 0:
    cnt += 1
    n = F(n)
print(cnt)

