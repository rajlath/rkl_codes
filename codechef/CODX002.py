nb_Test = int(input())
for _ in range(nb_Test):
    amount, offer, offer_qty, cost = [int(x) for x in input().split()]
    answer = amount // cost
    answer += (answer // offer) * offer_qty
    print(answer)
