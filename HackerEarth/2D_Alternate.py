arr = [int(x) for x in input().split()]
sum1 = sums = 0
odd = True
for i in arr:
    sums += i
    if odd:
        sum1 += i
    odd = not odd
sum2 = sums -  sum1

print(sum1)
print(sum2)
