for _ in range(int(input())):
    days = int(input())
    prices = [10**18] * 5 + [int(x) for x in input().split()]
    good_days = 1
    for  i in range(6, len(prices)):
        last_prices = prices[i-5:i]
        #print(i)
        good_days += min(last_prices) > prices[i]
        #print(last_prices ,min(last_prices),prices[i])
    print(good_days)
