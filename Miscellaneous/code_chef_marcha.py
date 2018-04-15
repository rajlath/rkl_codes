for _ in range(int(input())):
    ans = "NO"
    nos_currency, amt_asked = [int(x) for x in input().split()]
    currency = []
    for _ in range(nos_currency):
        currency.append(int(input()))
    last = (1 <<  nos_currency) - 1
    for i in range(last+1):
        curr = i
        curr_sum = 0
        j = 0
        while j < nos_currency:
            if curr % 2 == 0:
                curr_sum += currency[j]
            curr >>= 1
            j += 1
        if curr_sum == amt_asked:
            ans = "YES"
            break
    print(ans)




