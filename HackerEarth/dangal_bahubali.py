N, Q = [int(x) for x in input().split()]
power= [int(x) for x in input().split()]

sums = [0] * (N+1)

sums[0] = power[0]
for i  in range(1,N):
    sums[i] = sums[i-1] + power[i]
 
for i in range(Q)    :
    L, R = [int(x) for x in input().split()]
    ans = (sums[R-1] - sums[L-2]) // (R - L + 1 )
    print(ans)
   
