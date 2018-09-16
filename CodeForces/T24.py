mod = int(10e9) + 7
for i in range(int(input())):
    a, b = [int(x) for x in input().split()]
    if b == 1 :print(1)
    elif a == 1 :print(b)
    else:
        ans1  = pow(a, b+1, mod)
        ans2  = (b-1)
        ans3  = (ans1 // ans2)%mod
        print((ans3 -1)%mod)
