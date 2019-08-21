MOD = 1000000007
for _ in range(int(input())):
    threes = sorted([int(x) for x in input().split()])
    threes[0] = threes[0] % MOD
    threes[1] = (threes[1] - 1) % MOD
    threes[1] = (threes[1] * threes[0]) % MOD
    threes[2] = (threes[2] - 2) % MOD
    result = (threes[1] * threes[2]) % MOD
    print(result)
               
               