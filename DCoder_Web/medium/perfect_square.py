from math import sqrt, floor
def isPerfect(N):
    if (sqrt(N) - floor(sqrt(N)) != 0):
        return False
    return True

def get_nearest_perfect(N):
    if isPerfect(N):
        return int(sqrt(N))
    else:
        above = -1
        below = -1
        n1 = 0

        n1 = N + 1
        while True:
            if isPerfect(n1):
                above = n1
                break
            n1 += 1
        n1 = N - 1
        while True:
            if isPerfect(n1):
                below = n1
                break
            n1 -= 1
        diff1 = above - N
        diff2 = N - below
        if diff1 > diff2:
            return int(sqrt(below))
        else:
            return int(sqrt(above))

for _ in range(int(input()))            :
    curr = int(input())
    print(get_nearest_perfect(curr))

