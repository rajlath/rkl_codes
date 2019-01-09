import math
n, k = [int(x) for x in input().split()]
ones = bin(n)[2:].count("1")
if not n >= k >= ones:
    print("NO")
else:
    print("YES")
    n += 1
    while k:
        curr = 2 ** (math.floor(math.log(n - k, 2)))
        print(curr, end=" ")
        n -= curr
        k -= 1





