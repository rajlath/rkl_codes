'''
Sample Input:
1
5 2
50 40 30 20 10

Sample Output:
43.3333333333
'''
for _ in range(int(input())):
        n,x=[int(i) for i in input().split()]
        s=  [int(i) for i in input().split()]
        cg=s[0]
        credits=1
        for i in range(1,n):
            if s[i]>cg:
                cg=s[i]
                credits=i+1

        s[credits-1]=0
        while x>1:
            best=0
            for i in range(n):
                if s[i]!=0:
                    temp=(cg*credits+(i+1)*s[i])/(credits+1+i)
                    if temp>best:
                        best=temp
                        val=i
            credits+=val+1
            cg=best
            s[val]=0
            x-=1

        print(cg)


