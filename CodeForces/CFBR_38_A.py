nb_ranks = int(input())
years = [int(x) for x in input().split()]
curr, nexts = [int(x) for x in input().split()]
print(sum( years[(curr-1):(nexts - 1)]))