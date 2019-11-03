for _ in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    print(["no", "wonderful"][a%b==0 or a%c==0])