LEN = 4

def kaprekar(num):
    s = '{:0{}d}'.format(num, LEN)
    s = ''.join(sorted(s))
    a = int(s)
    b = int(s[::-1])
    return b - a

n = 1234
x = 0
while  n != kaprekar(n):
    x += 1
    if x == 10 : break
    print(n)



