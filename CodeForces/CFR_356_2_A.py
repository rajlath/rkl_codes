num_on_cards = [int(x) for x in input().split()]
discarded = 0
for num in num_on_cards:
    cnt = num_on_cards.count(num)
    if cnt > 1:
        discarded = max(discarded, num * min(cnt, 3))
print(sum(num_on_cards) - discarded)
