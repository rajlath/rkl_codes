nb_discount, amt_to_spend = [int(x) for x in input().split()]
discount_data = []
for _ in range(nb_discount):
    discount_data.append([[int(x) for x in input().split()]])
sorted(discount_data)
discount_recived = 0
min_spend = amt_to_spend
for i in discount_data:
    print(i)
    discount_recived += i[0][1]
    if i[0][0] > amt_to_spend:
        min_spend = min(min_spend, i[0][0] - discount_recived)
    else:
        min_spend = min(min_spend , amt_to_spend - discount_recived)
print(min_spend)






