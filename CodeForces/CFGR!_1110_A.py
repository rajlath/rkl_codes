R=lambda:map(int,input().split())
b,k=R()
a=[*R()]
if b%2==0:
    parity = a[-1]%2
else:
    parity = sum(a)%2
if parity:
    print("odd")
else:
    print("even")