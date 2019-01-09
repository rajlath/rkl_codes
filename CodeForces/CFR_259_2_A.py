n = int(input())
for i in range(n):
    p = abs(n//2 - i)
    a = '*' * p
    b = 'D' * (n - 2 * p)
    print(a + b + a)