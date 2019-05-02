n=int(input())
s1=input()
s2=input()
l1=[[] for i in range(27)]
l2=[[] for i in range(27)]
for i in range(n):
    if s1[i]=='?':
        l1[26].append(i)
    else:
        l1[ord(s1[i])-ord('a')].append(i)
    if s2[i]=='?':
        l2[26].append(i)
    else:
        l2[ord(s2[i])-ord('a')].append(i)
ans=[]
#print(l1)
#print(l2)
for i in range(26):
    while l1[i]!=[] and l2[i]!=[]:
        ans.append([l1[i][-1]+1,l2[i][-1]+1])
        l1[i].pop()
        l2[i].pop()
rem1=[]
rem2=[]
for i in range(26):
    rem1+=l1[i]
    rem2+=l2[i]
while rem1!=[] and l2[26]!=[]:
    ans.append([rem1[-1]+1,l2[26][-1]+1])
    rem1.pop()
    l2[26].pop()
while rem2!=[] and l1[26]!=[]:
    ans.append([l1[26][-1]+1,rem2[-1]+1])
    rem2.pop()
    l1[26].pop()
while len(l1[26])!=0 and len(l2[26])!=0:
    ans.append([l1[26][-1]+1,l2[26][-1]+1])
    l1[26].pop()
    l2[26].pop()
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])