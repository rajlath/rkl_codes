from math import sqrt
def solution(N):
    maxs  = int(sqrt(N))
    for i in range(maxs, 0, -1):
        if N%i == 0:
            return 2 * (i + N//i)



print(solution(30))




