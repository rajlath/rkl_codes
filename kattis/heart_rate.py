nb_test = int(input())
for _ in range(nb_test):
    b, t = [x for x in input().split()]
    b, t = int(b), float(t)
    print( (b - 1) * 60 / t,  b * 60 / t, (b + 1) * 60 / t)