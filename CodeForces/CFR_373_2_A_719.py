nb_days = int(input())
days    = [int(x) for x in input().split()]
if days[-1] == 15:
    print("DOWN")
elif nb_days == 1:
    print("-1")
elif days[-1] == 0:
    print("ÜP")
elif days[-1] > days[-2]:
    print("ÜP")