def depositProfit(deposit, rate, threshold):
    i = 1
    while deposit < threshold:
        deposit += deposit * rate / 100
        print(deposit, i)
        if deposit >= threshold:return i
        i += 1



print(depositProfit(100,20,170))