'''
from sys import stdin
dic={}     
ans={}       
def fun1(no):
    global ctr
    global ans
    dic.setdefault(no,1)
    ans[ctr]=len(dic)
    ctr-=1
n,q=map(int,stdin.readline().split())
ctr=n
x=list(map(fun1,stdin.readline().split()[::-1]))
print(dic, ans, x)
for i in range(q):
    que=int(input())
    print(ans[que])
'''    
n_el, n_qr = [int(x) for x in input().split()]    
arr = [int(x) for x in input().split()]
haves = []
icnt  = {}
arr = arr[::-1]
for v, i in enumerate(arr):
    if i not in haves:haves.append(i)
    icnt[n_el-v] = len(haves)
for i in range(n_qr):
    print(icnt[int(input())])    
