a, b = [int(x) for x in input().split()]
splits = 0
for i in [2, 3, 5]:
    while a%i == 0 and b%i==0:
        a //= i
        b //= i
    while a%i == 0:
        a //= i
        splits += 1
    while b%i == 0:
        b //= i
        splits += 1
print([-1, splits][a == b])


