'''
This is python translation of the solution provided
by all the successful submission, which surprisingly
has almost same code.

'''
n = int(input())
sums = 0
a = [0] + [int(x) for x in input().split()]
s = [0] * (n + 1)
m = 0
sums = 0
for i in range(1, n+1):
    sums += a[i]
    m += 1
    s[m] = a[i]
    while m >= 3 and s[m- 2] <= s[m-1] and s[m-1] >= s[m]:
        s[m-2] = s[m-2] - s[m -1] + s[m]
        m -= 2
value, sign, i, j = 0, 1, 1, m
while i <= j:
    if s[i] >= s[j]:
        value += sign * s[j]
        i += 1
    else:
        value += sign * s[j]
        j -= 1
    sign *= -1
print((sums + value)//2)




