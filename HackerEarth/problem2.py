a = int(input())
c = bin(a)[2:].count("1")
y = 15
ans=0
while c:
    ans += pow(2, y)
    c -= 1
    y -= 1
print(ans)