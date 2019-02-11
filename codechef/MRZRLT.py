nb_test = int(input())
for _ in range(nb_test):
    nb_round = int(input())
    one = [int(x) for x in input().split()]
    two = [int(x) for x in input().split()]
    res = 0
    for i in range(nb_round):
        #print(one[i]+1, two[i]+1 , (one[i]+1) / (two[i]+1))
        res = max(res,  (one[i]+1) / (two[i]+1))
    print("{:.7f}".format(res))
