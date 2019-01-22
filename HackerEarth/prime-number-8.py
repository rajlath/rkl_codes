P = [False, False] + [True] * 1001
for i in range(2, 1001):
    if P[i]:
        j = i * i
        while j < 1000:
            P[j] = False
            j += i
N = int(input())
for i in range(N+1):
    if P[i]:print(i, end=" ")


