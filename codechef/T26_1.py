import bisect
n=int(input())
arr=[0]*n
for _ in range(int(input())):
    l,r=map(int,input().split())
    arr[l-1:r]=list(map(lambda x:x+1,arr[l-1:r]))
arr=sorted(arr)
#print(arr)
for _ in range(int(input())):
    print(len(arr)-bisect.bisect_left(arr,int(input())))
