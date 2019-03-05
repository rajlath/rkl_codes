modulo = 1000000007
ncr    = []
ncr = [[0] * 1003 for i in range(1003)]
ncr = []
for i in range(1002): ncr[i][0] = 1
index = 1
for i in range(1, 1001):
    for j in range(1, i + 1):
        ncr[i][j] = (ncr[i - 1][j - 1] + ncr[i - 1][j]) % mod

nb_Test = int(input())
for _ in  range(nb_Test):
    a, b, c = [int(x) for x in input().split()]
    acr = ncr[a][0:a + 2]
    for i in range(a -1 , -1, -1):
        acr[i] += acr[i + 1]
    bcr = ncr[b][0:b + 1]
    k = 2 ** (c - 1) % modulo
    r1 = 0
    r  = 0
    result = 0
    if a > b: r1 = b
    else: r1 = 1
    for i in range(1, r1 + 1)            :
        r = acr[i + 1]
        r *= bcr[i]
        r %= modulo
        result += r
        result %= modulo
    result *= k
    print(result % modulo)
