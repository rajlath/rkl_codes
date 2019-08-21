lens = input()
given = [int(x) for x in input().split()]
ans = 0
for i in given:
    ans += i%6==0 and i%5!=0
print(ans)    
