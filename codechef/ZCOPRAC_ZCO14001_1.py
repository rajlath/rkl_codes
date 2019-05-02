def operate(arr,c,h):
    pos=0
    box=0
    for i in c:
        if i==1 and pos>0:
            pos-=1
        elif i==2 and pos<(len(arr)-1):
            pos+=1
        elif i==3 and box==0 and arr[pos]>0:
            box=1
            arr[pos]-=1
        elif i==4 and box==1 and arr[pos]<h:
            box=0
            arr[pos]+=1
        elif i==0:
            return arr

n,h = map(int,input().split())
arr= list(map(int,input().split()))
commands=list(map(int,input().split()))
res=operate(arr,commands,h)
print(*res)