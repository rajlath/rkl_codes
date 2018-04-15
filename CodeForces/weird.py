'''
If a = 0 or b = 0, end the process. Otherwise, go to step 2;
If a ≥ 2·b, then set the value of a to a - 2·b, and repeat step 1. Otherwise, go to step 3;
If b ≥ 2·a, then set the value of b to b - 2·a, and repeat step 1. Otherwise, end the process.
'''
a, b = [int(x) for x in input().split()]
while a * b :
    if a >= (b * 2): a%= (2*b)
    elif b >= (a * 2):b%=(2*a)
    else:break
print(a, b)




