nb_bats =  int(input())
scores  = [int(x) for x in input().split() if int(x) != -1]
print(sum(scores) / len(scores))