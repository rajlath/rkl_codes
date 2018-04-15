for i in range(int(input())):
    n = int(input())
    for j in range(1, n):
        x = j * j
        if x == n:
            print(n)
            break
        elif x > n:
            print(j-1)
            break
