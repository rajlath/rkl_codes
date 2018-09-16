
import  math
for i in range(int(input())):
    n,a,k=[int(x) for x in input().split()]
    d=(n-2)*180 - n*a
    y=(n*(n-1))//2
    x=a*y+d*(k-1)
    te=math.gcd(x,y)
    print(*[int(a//te) for a in [x, y]])

