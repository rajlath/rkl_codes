




nos_elem, nos_qry = [int(x) for x in input().split()]
sums = 0
arr  = [0] + [int(x) for x in input().split()]
for i in range(1,nos_elem+1):
    arr[i] += arr[i-1]
print(arr)    
for i in range(nos_qry):
    l , r = [int(x) for x in input().split()]    
    ans = ((arr[r] - arr[l-1])//(r+1-l))
    print(ans)
    
