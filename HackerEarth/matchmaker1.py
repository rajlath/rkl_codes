#copied
import operator
def solve(a, b):
    return len(list(set(a) & set(b)))
tc = int(raw_input())
assert(tc>0 and tc<51)
while tc > 0:
    tc = tc - 1
    n, k = map(int, raw_input().split())
    assert(n>0 and n<2001)
    assert(k>0 and k<=n)
    l = raw_input().split(" ")
    assert(len(l) == len(list(set(l))))
    for i in l:
        assert(len(i)>0 and len(i)<27)
    name = list(set(list("littlejhool")))
    ans = {}
    for i in l:
        temp = list(set(list(i)))
        temp2 = solve(temp, name)
        ans[i] = temp2
    finalans = sorted(ans.items(), key=operator.itemgetter(1))
    for i in xrange(k):
        if i == k - 1:
            print finalans[i][0]
        else:
            print finalans[i][0],
