def reVal(num):
    if (num >= 0 and num <= 9):
        return chr(num + ord('0'));
    else:
        return chr(num - 10 + ord('A'))

def convert(n, base):
    rets = ''
    while n > 0:
        n, m = divmod(n, base)
        rets += reVal(m)
    return rets[::-1]

for _ in range(int(input())):
n, b = [int(x) for x in input().split()]
print(convert(n, b))