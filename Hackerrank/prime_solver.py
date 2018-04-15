a,b=list(input().split());a=int(a);s=len(b)
for i in range(1,a+1):print((i,b[s-i%s:]+b[:s-i%s])[all(i%j for j in range(2,i)) and i!=1])

'''
l=list(input().split());a,b=int(l[0]),l[1];s=len(b)
for i in range(1,a+1):print((i,b[s-i%s:]+b[:s-i%s])[all(i%j for j in range(2,i)) and i!=1])
'''

n,s=list(input().split());a=int(n);l=len(s);k=P=1
while k<n+1:h=-k%l;print(s[h:]+s[:h] if P%k else k);P*=k*k;k+=1