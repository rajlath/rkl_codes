n = int(raw_input())
one = [0 for i in range(n)]
neg = [0 for i in range(n)]
zero = [0 for i in range(n)]
sign = [0 for i in range(n)]

numbers = [int(j) for j in raw_input().split()]
if numbers[0] == 1:
    one[0] = 1
elif numbers[0] == 0:
    zero[0] = 1
elif numbers[0] == -1:
    sign[0] = 1
elif numbers[0] < 0:
    neg[0] = 1

for i in range(1,n):
    one[i] = one[i-1]
    zero[i] = zero[i-1]
    neg[i] = neg[i-1]
    sign[i] = sign[i-1]

    if numbers[i] == 1:
        one[i] = one[i-1] + 1
    elif numbers[i] == 0:
        zero[i] = zero[i-1] + 1
    elif numbers[i] == -1:
        sign[i] = sign[i-1] + 1
    elif numbers[i] < 0:
        neg[i] = neg[i-1] + 1

q = int(raw_input())
for i in range(q):
    l = raw_input().split()
    a, b = int(l[0]) - 1, int(l[1]) - 1
    ans =b - a + 1
    if ans == 1:
        print 1
        continue

    if a != 0:
        ondu = one[b] - one[a-1]
        signdu = sign[b] - sign[a-1]
        o = zero[b] - zero[a-1]
        negdu = neg[b] - neg[a-1]
    else:
        ondu = one[b]
        signdu = sign[b]
        o = zero[b]
        negdu = neg[b]

    ans -= o
    ans -= ondu
    ans -= signdu
    if ans == 0 and ondu == 0:
        if signdu>1:
            print 2
            continue
        else:
            print 1
            continue
    elif ondu != 0 and ans == 0:
        print 1
        continue


    if negdu % 2 == 0:
        print ans
    elif signdu > 0:
        print ans + 1
    else:
        print ans - 1