n=int(input())
a=list(map(int,raw_input().split()))
b=list(map(int,raw_input().split()))
a.append(0)
b.append(0)
a.sort()
b.sort()
print(a, b)
sa,sb=0,0
while len(a)>1 or len(b)>1:
    if a[-1]>b[-1]:
        sa+=a.pop()
    else:
        b.pop()
    if a[-1]>b[-1]:
        a.pop()
    else:
        sb+=b.pop()
print sa, sb
print sa-sb