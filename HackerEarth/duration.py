nb_test = int(input())
for _ in range(nb_test):
    sh, sm, eh, em = [int(x) for x in input().split()]
    interval = (eh * 60 + em ) - (sh * 60 + sm)
    h, m = divmod(interval, 60)
    print(h, m)