s= list(input())
ans=10**9
for i in range(1,45001):
    sr = str(i*i)
    sri=0
    for j in range(len(s)):
        try:
            if s[j]== sr[sri]:sri+=1
        except IndexError:
            pass
    y = len(s)- len(sr)
    if sri==len(sr):ans=min(ans, y)
ans = [ans,-1][ans==10**9]
print(ans)
