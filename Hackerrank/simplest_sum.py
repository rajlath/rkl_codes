def f(k, n):
    sums = 0
    i = 1
    while i <= n:
        sums += i
        i *= k
        i+= 1
    return sums
from collections import Counter
s = []
for _ in range(int(input())):
    k, a, b = [int(x) for x in input().split()]
    alls = 0
    for i in range(a, b+1):
        sums = f(k, i)
        alls += sums
        s.append(sums)
    print(alls)
    s = Counter(s)
    for i in s:
        print("val :{} count: {}".format(i, s[i]))








'''
function f(k, n) {
    sum = 0;

    for (i = 1; i ≤ n; i += 1) {
        sum += i;
        i *= k;
    }

    return sum;
}
'''