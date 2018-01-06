'''
week
2
1 4
2 3
Sample Output 0

2
1
'''
#!/bin/python3

import sys
from math import factorial as fact

def answerQuery(l, r):
    single = 0
    double = []
    temp = s[l-1:r]
    print(temp)
    st = set(temp)
    print(st)
    for i in st:
        n = temp.count(i)
        if(n%2 != 0):
            single += 1
        if(n//2 != 0):
            double.append(n//2)
        print(single, double)
    count = fact(sum(double))
    for i in double:
        count = count//fact(i)
    if(single != 0):
        return single*(count)%(10**9 + 7)
    return count%(10**9 + 7)

if __name__ == "__main__":
    s = input().strip()
    q = int(input().strip())
    for a0 in range(q):
        l, r = input().strip().split(' ')
        l, r = [int(l), int(r)]
        result = answerQuery(l,r)
        print(result)