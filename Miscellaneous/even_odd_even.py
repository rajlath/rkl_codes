'''
4
1 2 1 2
'''
n = int(input())
a = [int(x) for x in input().split()]
positive = [0]*(n+1)
negative = [0]*(n+1)
diffs    = 0
ans      = 0

positive[0] = 1
for i in a:
    if i&1==1:
        diffs -= 1
    else:
        diffs += 1

    if diffs < 0:
        ans += negative[-diffs]
        negative[-diffs] += 1
    else:
        ans += positive[diffs]
        positive[diffs]+=1
print(ans)