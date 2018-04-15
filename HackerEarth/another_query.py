N = 100005
bit = [0]*(N+3)
a   = [0]*(N+3)
n   = 0

def update(x, val):
    global bit
    while x > 0:
        bit[x]+= val
        x -= (x and (-x))

def query(x):
    ret = 0
    while x > 0:
        ret += bit[x]
        x -= (x and (-x))
    return ret


n = int(input())
arr = [int(x) for x in input().split()]
arr = [0]+arr
for i, v in enumerate(arr,start=1):
    update(i,v)
    update(i+1,-v)
for _ in range(int(input())):
    ins = [x for x in input().split90]
    if x[0] == "1":
        update(1,-1)
        update(int(x[1]+1,1))
    else:
        l = 1
        r = n
        ans = -1
        mid = (l+r)//2
        tm = int(input())
        if query(mid) <= tm:
            l = mid
        else:
            r = mid
        if query(l) == tm:ans = l
        if query(l+1) == tm : ans = l+1
        print(["No", "Yes"][ans >= 0])










