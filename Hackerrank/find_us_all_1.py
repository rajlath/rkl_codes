loop = int(input())
a, b, c = [int(x) for x in input().split()]
mod = 1000000007
for i in range(loop):
    a1 = (b + c)%mod
    b1 = (a + c)%mod
    c1 = (a + b)%mod
    a, b, c = a1, b1, c1
print(a)
print(b)
print(c)
