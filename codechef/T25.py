for i in range(int(input())):
    noc, amount = [int(x) for x in input().split()]
    city_cost   = [int(x) for x in input().split()]
    city_cost   = sorted(city_cost)
    start_with  = sum(city_cost[:noc])
    if start_with > amount:
        for i in range(noc-1, -1, -1):
            start_with -= city_cost[i]
            if start_with < amount:
                print(noc - i, amount-start_with)
    else:
        l = 0
        r = noc
        while amount > start_with:
            start_with -city_cost[l] + city_cost[r]
            if start_with < amount:
                print(amount)

