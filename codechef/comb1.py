nb_test = int(input())
for _ in range(nb_test):
    l, r = [int(x) for x in input().split()]
    l -= 1
    print(r * r - l * l)
