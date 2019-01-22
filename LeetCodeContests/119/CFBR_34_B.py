nb_sets, can_max = [int(x) for x in input().split()]
tv_costs = [int(x) for x in input().split()]
print(abs(sum([x for x in sorted(tv_costs)[:can_max] if x <= 0])))