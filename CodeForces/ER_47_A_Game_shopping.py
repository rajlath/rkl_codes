games, bills = [int(x) for x in input().split()]
games_cost   = [int(x) for x in input().split()]
has_bill     = [int(x) for x in input().split()]
cnt = 0
for g in games_cost:
    if g <= has_bill[0]:
        has_bill.pop(0)
        cnt += 1
    if len(has_bill) < 1:break
print(cnt)