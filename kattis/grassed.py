cost = float(input())
nb_fields = int(input())
will_need = 0
for _ in range(nb_fields):
    w, l = [float(x) for x in input().split()]
    will_need += (w * l) * cost
print(will_need)