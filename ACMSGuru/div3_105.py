
n = int(input())
a = (n // 3) * 2
if n % 3 == 0:
    b = 0
else:
    b = n%3 - 1
print(a + b)