nb_test = int(input())
for _ in range(nb_test):
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    answer = 0
    for i in range(n - 1):
         for j in range(n - 1):
             answer = max(answer, a[i][j] + a[i+1][j+ 1])
    print(answer)
