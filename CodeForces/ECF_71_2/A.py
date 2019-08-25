for _ in range(int(input())):
    buns, ham, chicken = [int(x) for x in input().split()]
    hcost, ccost = [int(x) for x in input().split()]
    profit = 0
    if ccost > hcost:
        cburg = min(buns//2, chicken)
        profit = cburg * ccost
        hburg = min((buns - cburg * 2) // 2, ham)
        profit += hburg * hcost
    else:
        hburg = min(buns//2, ham)
        profit = hburg * hcost
        cburg  = min((buns - hburg * 2) // 2, chicken)
        profit += cburg * ccost
    print(profit)



