MAXNBITS = 10
sumluck = 0
sols = []
MOD = 10e8 + 7
for nbits1 in xrange(1, MAXNBITS):
    base = 1 << nbits1
    add = 1
    for pos in xrange(nbits1):
        num = base + add
        
        add <<= 1        
        sumluck = (sumluck + num) % MOD
        sols.append((num, sumluck))
        
def solve(n):
    res = 0
    for k, v in sols:
        if k > n:
            return res
        res = v
    return -1
    
for i in xrange(input())    :
    print(solve(input()))
          
       
