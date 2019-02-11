from collections import defaultdict
nb_cards = int(input())
special = defaultdict(list)
for _ in range(nb_cards):
    curr = input()
    if curr == curr[::-1]:
        special[curr[0]].append(curr)
sums = 0
for j in special.keys():
    i = len(special[j])
    sums += ( (i * (i-1)) // 2)
print(sums)
