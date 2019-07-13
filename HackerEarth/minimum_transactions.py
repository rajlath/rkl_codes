nb_people, nb_trans = [int(x) for x in input().split()]
trans = [0] * (nb_trans+ 1)
for i in range(nb_trans):
    a, b, amt = [int(x) for x in input().split()]
    trans[a - 1] += amt
    trans[b - 1] -= amt
print(sum(i for i in trans if i > 0))
