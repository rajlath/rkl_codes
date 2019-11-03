distance = int(input())
oc, of, od = [int(x) for x in input().split()]
cs, cb, cm, cd = [int(x) for x in input().split()]
online_cost = oc + max((distance - of), 0) * od
classic_cost = cb
classic_cost += (distance // cs) * cm
classic_cost += distance * cd
#print(online_cost, classic_cost)
if online_cost <= classic_cost:
    print("Online Taxi")
else:
    print("Classic Taxi")
