def solution(N):
    could_be = 1
    fcount   = 0
    while could_be * could_be < N:
        if N % could_be == 0:
            print(could_be)
            fcount += 2
        could_be += 1
    if could_be * could_be == N:fcount += 1
    return fcount


print(solution(64))




