Input = list(map(int,input().split()))
n, pos, l, r = Input[0], Input[1], Input[2], Input[3]
if l == 1 and r != n:
    print(abs(r - pos) + 1)
elif r == n and l != 1:
    print(abs(pos - l) + 1)
elif l == 1 and r == n:
    print('0')
else:
    print(min(abs(pos - l), abs(r - pos)) + r - l + 2)