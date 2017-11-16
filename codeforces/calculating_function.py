ans = 0
eve = False
for i in range(1, int(input())+1):
    ans += [-1,1][eve]*i
    
    eve = not eve
print(ans)    
