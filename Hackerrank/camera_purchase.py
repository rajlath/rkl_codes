'''
Sample Input 0

3
1 1 2
1 3 2
3
1
1
2
2
1 2
2
1
3
1
Sample Output 0

3
2
-1
'''
from collections import defaultdict
nob = int(input())
brands = [int(x) for x in input().split()]
prices  = [int(x) for x in input().split()]
price = defaultdict(list)
for b in range(1, nob+1):
    if brands[b] not in price: price[brands[b]] = []
    price[brands[b]].append(prices[b])
for i in range(int(input())):
    all_prices = []
    brand = int(input())
    pr = [int(x) for x in input().split()]
    k  = int(input())
    for j in range(brand):
        all_prices.extend([pr[j]])
    print(all_prices[int(input())-1])






