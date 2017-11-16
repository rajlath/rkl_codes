'''
5
1 2 3 4 5
2
1 2
2 3
'''
arr_cnt = int(input())
arr  = [int(x) for x in input().split()]
tmp  = [0] * (arr_cnt+1)
arr.insert(0, 0)

for _ in range(int(input())):
    l, r = [int(x) for x in input().split()]
    tmp[l] += 1
    tmp[r+1] -= 1
for i in range(1,arr_cnt+1):
    tmp[i] = tmp[i] + tmp[i-1]
for i in range(1, arr_cnt+1)    :
    if tmp[i]%2==1:
        arr[i], arr[arr_cnt-i+1] = arr[arr_cnt-i+1], arr[i] 
print(" ".join(map(str, arr[1:])))
    


