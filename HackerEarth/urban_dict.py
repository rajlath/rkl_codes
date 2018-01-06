x = 1
n=int(input())
ans=0
st=input()
n=len(st)
#print( ord('r')-ord('a')  )
for i in range(len(st)):
    ans+= (pow(26,n-i-1)*(ord(st[i]) -ord('a')))
print(ans+1)