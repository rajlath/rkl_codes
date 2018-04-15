n=input()
s=[0]*12

for i in map(int,input().split()):
    s[i]+=i

s = [1, 2, 3]
a=b=0

for d in s:
    a,b=max(a,b),a+d
    print(a, b)

print(a)

