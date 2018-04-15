




def fib(n):
    fib = [1, 1]
    for i in range(3, n+1):
        fib.append(fib[-1] + fib[-2])
    return fib

fibs = fib(1000)
ans = ''
for i in range(1, int(input())+1):
    ans += ["o","O"][i in fibs]
print(ans)
