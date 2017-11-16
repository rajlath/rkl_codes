imax = 10e18
mod  = 10e8 + 7
for i in range(int(input())):
    n = int(input())
    ans = 0
    cur = 2
    flag=True
    times=1
    while flag:
        div = times
        while flag and div:
            t = cur + (cur>>div)
            if t <= n:
                ans+=t
                ans%=mod
            else:
                flag=False
                break
            div-=1
        cur <<= 1
        times +=1
    print(int(ans))    
    
MOD = 1000000007
 
def solve(n):
    res = 0
    for i in xrange(n + 1):
        if bin(i).count("1") == 2:
            res += i
    return res % MOD
 
MAXNBITS = 60
sumluck = 0
sols = []
for nbits1 in xrange(1, MAXNBITS):
    base = 1 << nbits1
    add = 1
    for pos in xrange(nbits1):
        num = base + add
        add <<= 1
        sumluck = (sumluck + num) % MOD
        sols.append((num, sumluck))
 
def solve2(n):
    res = 0
    for k, v in sols:
        if k > n:
            return res
        res = v
    return -1
    
def main():
    t = input()
    for _ in xrange(t):
        n = input()
        print solve2(n)
 
main()    
                
                    
                
    

