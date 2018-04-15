'''
1:1:4:7
2:2:5:8
3
    123
    100222
    10003

12
    00222
    -1
'''

def for_2(n, digsum):
    rem = dig_sum%3
    candidate = []
    if rem == 0 and int(n)%2==1:
        for i in range(len(n)-1, 0, -1):
            curr = int(n[:i])

            if int(curr) % 2 == 0:
                candidate.append(curr)
    if len(candidate)>0:
        return(max(candidate))
    else:
        return(-1)




for i in range(int(input())):
    n = input().strip()
    dig_sum = sum([int(x) for x in n])



