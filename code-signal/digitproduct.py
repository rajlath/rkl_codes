'''
def digitsProduct(n):
    if n < 10:return 10 + n
    else:
        ans = ''
        for i in range(9, 1, -1):
            while n % i == 0:
                n/=i
                ans=str(i)+ans
        if n > 10:return -1
        return int(ans)


'''
f=lambda n,a=0,u=1,i=9:n<2and(a or 1)or-(i<2)or n%i<1and f(n/i,a+i*u,u*10)or f(n,a,u,i-1)
print(f(9))