from collections import Counter
from decimal import Decimal

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

temp = 0
dividers = []
for i in range(n):
    if a[i] != 0:
        dividers.append(Decimal(b[i])/ Decimal(a[i]))
    else:
        if b[i] == 0:
            temp +=1

if len(dividers) == 0:
    print(temp)
else:
    print(Counter(dividers).most_common(1)[0][1] + temp)