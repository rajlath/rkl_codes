def fun1(a, b):
    if a%2 == 0:
        pt = [b, 1, b^1, 0]
    else:
        pt = [a, a^b, a-1, (a-1)^b]
    return ["Even", "Odd"][pt[(b-a) % 4]%2]

nb_test = int(input())
for _ in range(nb_test):
    a, b = [int(x) for x in input().split()]
    print(fun1(a, b))