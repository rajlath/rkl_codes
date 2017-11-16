'''
7
1 5 7 5 6 7 5
5
1 2
2 3
4 6
1 7
3 6

0
0
1
1
1


noe = int(input())
arr = "".join(input().split())
cnt = [0] * (noe+2)

for i in range(noe):
    if i == 0:
        l = "0"
        r = arr[1:]        
    elif i == noe-1:
        l = arr[:-1]
        r = 0  
    else:
        l = int(arr[:i])
        r = int(arr[i+1:])
    cnt[i] = int((int(l) + int(r))%30==0)
for i in range(int(input()))   :
    l, r = [int(x)  for x in input().split()]
    print(sum(cnt[l-1:r]))
'''

noe = int(input())
arr = [int(x) for x in input().split()]
sums = sum(arr)

left  = [0] * noe
right = [0] * noe
lucky = [0] * noe

for i in range(noe):
    if i == 0: left[i] = 0
    else:left[i] = left[i-1] + arr[i-1]
    
    right[i] = sums - (left[i] + arr[i])
    
    if (left[i] + right[i]) % 3 == 0:
        fd = [arr[i-1], 0][i == 0]
        sd = [arr[noe-1], 0][i == (noe-1)]
        if (fd + sd ) % 10 == 0:lucky[i] = 1 
    if i > 0:
        lucky[i] += lucky[i-1]        
for _ in range(int(input())):
    l, r = [int(x) for x in input().split()]
    count = [lucky[l-2], 0][lucky[r-1]-(l-2) < 0]
    count = lucky[r-1] - [lucky[l-2], 0][(l-2) < 0]
    print(count)
               
    


    
    
    

