a, b = 1, 1
n = int(input())
for i in range(1, n+1):
    while b < i:
        a, b = b, a+b
    print(["o","O"][b==i], end="")
#OOOoOooOooooOoo