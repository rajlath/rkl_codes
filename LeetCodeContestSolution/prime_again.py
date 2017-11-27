
MAX = 1e9
MX  = 10005

primes = []
seen   = [True]*(MX)




def create_primes():
    global seen
    for i in range(2, MX):
        if seen[i]==True:
            primes.append(i)
            for j in range(i*i, MX, i):
                seen[j] = False
    return primes

dp  = [int(1e9)]*(MX+5)
primes = create_primes()
primes.extend([4, 27, 3125])
primes = sorted(primes)
for i in range(2, 10):
    j = 0
    while j < len(primes) and primes[j]<= i:

        if dp[i] < dp[i-primes[j]]:
            dp[i] = dp[i]
        else:
            dp[i] = dp[i-primes[j]]+1
        #dp[i] = min(dp[i], dp[i-primes[j]]+1)
        print(dp[i])
        j += 1

print(dp[10])
for _ in range(int(input())):
    print(dp[int(input())])




