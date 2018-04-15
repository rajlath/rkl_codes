'''
2
aabb
2
32 162
192 26
aaaa
2
24 212
44 200
'''


mods = int(10e9 + 7)
def fact(n):
    k = 1
    i = n
    while i:
        k=((k%mods)*(n%mods))%mods
        n -= 1
        i -= 1
    return k

def fac(n):
    return 1%mods if (n < 1) else n * fac(n-1)%mods

for _ in range(int(input())):
    str = input()
    noc = int(input())
    ans = 0
    for _ in range(noc):
        a, b = [int(x) for x in input().split()]
        ch   = chr((a + b) // 2)
        cnt  = fact(str.count(ch))
        ans = ((ans%mods)+(cnt%mods))%mods;


    print(ans)





