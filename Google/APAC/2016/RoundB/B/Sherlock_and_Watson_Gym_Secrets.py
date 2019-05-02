mod = 1000000007
nb_test = int(input())
for _ in range(nb_test):
    aa = 1
    a, b, n, k = [int(x) for x in input().split()]
    rv  = [0 for _ in range(k)]
    cta = [0 for _ in range(n)]
    ctb = [0 for _ in range(n)]
    cot = [0 for _ in range(n)]
    for i in range(k):
        cot[i] = (n // k + (n % k >= i)) %  mod
        if i == 0: cot[i]-= 1
        cta[i] = pow(i, a, k)
        cta[b] = pow(i, b, k)
        rv[ctb[i]] = (rv[ctb[i]]+cot[i])%mod
    sums = 0
    for i in range(k):
        sums = (sums+cot[i]*rv[(k-cta[i])%k]%mod)%mod
        if((cta[i]+ctb[i])%k==0):
            sums=(sums-cot[i])%mod
    sums=(sums%mod+mod)%mod
    print("Case #{}: {}".format(aa+1,sums))
    aa += 1




