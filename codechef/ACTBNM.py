
for _ in range(int(input())):
    S, H = [int(x) for x in input().split()]
    print(["Himawari","Shinchan"][S>H])
