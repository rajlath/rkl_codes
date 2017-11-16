'''
1
5
1 2 3 4 5
'''

def len_sum(arr):
    n = len(arr)
    s = set()
    j = 0
    ans = 0
    for i in range(n):
        while j < n and s.isdisjoint([arr[j]]):
            s.add(arr[j])
            j += 1
        ans += ((j - i) * (j - i + 1))/2 
        s.remove(arr[i])  
    return int(ans)
    
for _ in range(int(input()))     :
    _ = input()
    arr = [int(x) for x in input().split()]
    print(len_sum(arr))
    
    
        
