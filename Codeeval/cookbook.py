
import heapq
portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

prices = {
   'ACME': 45.23,
   'AAPL': 612.7,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

minPrice = min(zip(prices.values(), prices.keys()) )
maxPrice = max(zip(prices.values(), prices.keys()))
print(minPrice, maxPrice)
sortedPrice = sorted(zip(prices.values(), prices.keys()))
print(sortedPrice)
print(min(sorted(prices)), prices[min(prices)])
print(max(sorted(prices)), prices[max(prices)])
print(sorted(prices.keys()))
