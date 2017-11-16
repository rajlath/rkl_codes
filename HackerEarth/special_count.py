for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    if k%2 or k>(n*n/2):
        print("NO")
    else:
        print("YES")
