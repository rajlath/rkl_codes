'''
2
5 3 2
1 2 3 4 5
5 2 4
1 2 3 4 5
'''
nb_test = int(input())
for _ in range(nb_test):
    n, a, b = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    B, A = 0, 0
    for i in arr:
        if i % a == 0:
            B += 1
        elif i % b == 0:
            A += 1
    print(["BOB", "ALICE"][A > B])
