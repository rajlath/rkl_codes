nb_Test = int(input())
for _ in range(nb_Test):
    needed = [int(x) for x in input().split()]
    have   = [int(x) for x in input().split()]
    price  = [int(x) for x in input().split()]
    has_amt= int(input())
    #price_cup = sum(price)
    #answer = has_amt // price_cup
    #print(answer)
    left = 1
    rite = int(1e13)

    while left <= rite:
        amount = has_amt
        mid = (left + rite) >> 1
        #print(mid)
        to_pay = 0
        for i in range(4):
            to_pay += max(0, ((mid * needed[i]) - have[i])*price[i])
        #print(mid, to_pay)
        if to_pay <= has_amt:
            answer = mid
            left = mid + 1
        else:
            rite = mid - 1
        #print(left, rite)

    print(answer)