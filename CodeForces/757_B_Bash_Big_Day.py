'''
n = int(input())
arr = [int(x) for x in input().split()]
k = 1
s = [0] * 100001
for i in arr:
    s[i] += 1
for i in range(2, 100001)    :
    p = 0
    for j in range(i, 100001, i):
        p += s[j]
    k = max(k, p)
print(k)
'''
n=int(input())
a=list(map(int,input().split()))
ans=1
s=[0]*100001
for i in a:
    s[i]+=1
for i in range(2,100001):
    p=0
    for j in range(i,100001,i):
        p+=s[j]
    ans=max(ans,p)
print(ans)