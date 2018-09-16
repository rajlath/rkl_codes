'''
mod = int(10e9) + 7
for i in range(int(input())):
    a, b = [int(x) for x in input().split()]
    if b == 1 :print(1)
    elif a == 1 :print(b)
    else:
        ans1  = pow(a, b+ 1, mod)
        print(ans1)
        ans1 = (ans1 / (b - 1))%mod
        print(ans1)
        print(ans1 - 1)

'''
mod = int(10e9 + 7)
for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    if n >= 2:
        ans = ((pow(n, k+1) - 1) // (n - 1) - 1) % mod
        print(ans )
    else:
        print(n)
'''
n = 6
k = 6
if n > 2:
    ans = (pow(n, k+1) - 1) // (n - 1) - 1
    print(ans)
else: print(n)
'''




