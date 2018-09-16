n = int(input())
for num in range(n):
    num = 0
    a = [ [-1 for x in range(n)] for y in range(n)]
    while num < n:
        i = 0
        while i < (n+1)//2:
            a[(i+num)%n][num] = num
            i += 1
        j = 0
        while j < (n + 1)//2 + 1:
            a[num][(j+num)%n] = num
            j += 1
        num += 1
    print(a)

    for i in range(n):
        for j in range(j):
            if j == 0:
                continue
        print(a[i][j]+1,end=" ")
        print()
