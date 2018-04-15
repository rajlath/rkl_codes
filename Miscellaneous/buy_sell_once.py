prices = [310,315,275,295,260,270,290,230,255,250]

min_so_far = int(10e8)
max_all    = int(-10e8)
for price in prices:
    if price < min_so_far:
        min_so_far = price
    profit_today = price - min_so_far
    max_all = max(max_all, profit_today)
    #print(min_so_far, profit_today, max_all)
print(max_all)
