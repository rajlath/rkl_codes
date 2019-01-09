n, k = [int(x) for x in input().split()]
i = 0
while k >= i + 1:
    k -= (i + 1)
    i =  (i + 1)%n
print(k)