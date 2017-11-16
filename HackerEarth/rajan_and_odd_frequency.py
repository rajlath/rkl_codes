input()
arr = [int(x) for x in input().split()]
ans = 0
for i in arr:
    ans^=i
print(ans)    
