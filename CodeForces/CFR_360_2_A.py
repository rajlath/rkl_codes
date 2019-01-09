nb_opps, nb_days = [int(x) for x in input().split()]
arya_wins = 0
max_wins  = 0
max_con_wins = 0
for _ in range(nb_days):
    opps = input()
    if "0" in opps:
        max_con_wins += 1
        max_wins = max(max_wins, max_con_wins)
    else:
        max_con_wins = 0
print(max_wins)