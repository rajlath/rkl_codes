
mods  = 1000000007
for _ in range(int(input())):

    l, r = [int(x) for x in input().split()]
    l = l - 1
    rsum = ((r * (r + 1) * (r + 2) + (r + 3) * (r + 4)))
    lsum = ((l * (l + 1) * (l + 2) + (l + 3) * (l + 4)))
    rsum = rsum // 5
    lsum = lsum // 5
    print((rsum - lsum) % mods)
'''
t = int(input())
mod = 1000000007
      
for i in range (0,t):
    l,r=map(int,input().split())
    l=l-1
    right=(r*(r+1)*(r+2)*(r+3)*(r+4))
    right=right//5
    left=(l*(l+1)*(l+2)*(l+3)*(l+4))
    left=left//5
    print((right-left)%mod)
'''