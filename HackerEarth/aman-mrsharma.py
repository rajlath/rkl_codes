nb_test = int(input())
toffees = 0
for _ in range(nb_test):
    radius, horlicks = [int(x) for x in input().split()]
    can_do = horlicks * 100
    need_to= 2 * int((22/7) * ( radius ))
    toffees += can_do >= need_to
print(toffees)