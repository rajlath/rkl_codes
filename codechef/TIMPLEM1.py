def seive(ar,n):
    for i in range(2,n):
        if ar[i]==1:
            for j in range(i+i,n,i):
                ar[j]=0
def main():
    t=int(input())
    ar=[1]*100001
    seive(ar,100001)
    ar1=[0]*100001
    for i in range(2,100001):
        if ar[i]==1:
            ar1[i]=pow(i,i,1000000007)
            ar1[i]=(ar1[i]+ar1[i-1])
        else:
            ar1[i]=ar1[i-1]
    for _ in range(t):
        l,r=tuple(map(int,input().split()))
        print((ar1[r]-ar1[l-1])%1000000007)
main()