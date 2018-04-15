#prices = [310,315,275,295,260,270,290,230,255,250]
prices = [12,11,13,9,12,8,14,13,15]

max_all = int(-10e9)
min_so_far = int(10e9)
max_profit_once = []
for price in prices:
    min_so_far = min(min_so_far, price)
    max_all    = max(max_all , price - min_so_far)
    max_profit_once.append(max_all)
print(max_profit_once)
max_price_so_far =  int(-10e9)
max_total_profit =  int(-10e9)
for i in range(len(prices)-1, -1, -1):
    max_price_so_far = max(max_price_so_far, prices[i])

    max_total_profit = max(max_total_profit, max_price_so_far - prices[i] + max_profit_once[i-1])
    print(max_price_so_far, max_total_profit)
print(max_total_profit)
