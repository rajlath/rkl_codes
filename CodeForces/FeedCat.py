from math import ceil
hrs, mins = [int(x) for x in input().split()]
start_mins= hrs * 60 + mins
Limit_mins= 1200
additional_min = [0, Limit_mins-start_mins][start_mins<Limit_mins]
hunger, incr, price,decr_ratio = [int(x) for x in input().split()]

needed_now = ceil(hunger / decr_ratio)
curr_cost  = needed_now * price

needed_at8 = (ceil((hunger + additional_min * incr) / decr_ratio) * price) * 0.8

print(needed_at8, curr_cost)
print(min(needed_at8, curr_cost))