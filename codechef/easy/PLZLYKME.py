for _ in range(int(input())):
    L, D, S, C = [int(x) for x in input().split()]
    for i in range(1, D):
        S +=  S * C
        if S >= L:
            break
    print(["DEAD AND ROTTING","ALIVE AND KICKING"][S >= L])
