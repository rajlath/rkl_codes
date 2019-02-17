nb_Test = int(input())
for _ in range(nb_Test):
    nb_chefs = int(input())
    jars = [int(x) for x in input().split()]
    needs = 0
    for i in jars:
        needs = needs + i -1
    print(needs + 1)




