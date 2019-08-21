for _ in range(int(input())):
    n, d, r = [int(x) for x in input().split()]
    answer = str(n / d)
    fract  = answer.split(".")[1]
    print(fract)
