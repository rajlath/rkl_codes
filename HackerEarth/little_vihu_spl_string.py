s=input();maxs= -1e9;lens=len(s)
for i in range(lens):
    curr=s[i+1:]+s[:i+1];sums=0
    for j in range(lens):
        sums+=(ord(curr[j])-97)*(2**(-j))
    if sums>maxs:ans,maxs=curr,sums
print(ans)
