nb_test = int(input())
for _ in range(nb_test):
    a, b = [int(x) for x in input().split()]
    print(9 * (a - 1) + b)