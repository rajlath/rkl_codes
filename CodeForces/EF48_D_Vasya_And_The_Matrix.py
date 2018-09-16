from functools import reduce
def xor_array(ar):
    return reduce(lambda x, y: x^y, ar)
n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
x = xor_array(a)
y = xor_array(b)
if x != y:
    print("NO")
else:
    print("YES")
    print(x ^ a[0] ^ b[0], *b[1:])
    for i in range(1, n):
        print(a[i], "0 " * (m - 1))