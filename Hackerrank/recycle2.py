from bisect import bisect_left

def rotate(x):
    return x[-1]+x[:-1]

l = int(raw_input())
arr = map(int,raw_input().split())
s = set([])
arr.sort()
for i in arr:
    temp = str(i)
    for j in xrange(len(str(i))-1):
        temp = rotate(str(temp))
        try:
            if temp[0]!="0" and arr[bisect_left(arr,int(temp))]==int(temp) and int(temp)!=i:
                s.add(((min(i,int(temp))),max(i,int(temp))))
        except:
            pass
print len(s)