from math import gcd

t = int(input())
while(t):
    t -= 1
    l, x, y, z = [int(x) for x in input().split()]
    n = [int(x) for x in input().split()]
    lcm = n[0]
    a = [x, y, z]
    c = 0
    for i in n[1:]:
        lcm = lcm * i // gcd(lcm, i)
        for i in n:
            temp = lcm // i
            j = 0
            while(temp > 0 and j < 3):
                # print(lcm,c,k,lcm//i)
                if(i == lcm):
                    c += 1
                    break
                k = a[j]
                if(temp // k == 1):
                    c += 1
                    break
                while(temp % k == 0):
                    temp = temp // k
                    if(temp == 1):
                        c += 1
                        break
                    j += 1
    if(c == l):
        print("She can")
    else:
       print("She can't")
