from collections import Counter
n = input()
a = Counter([int(x) for x in input().split()])
p = [1<<x for x in range(31)]
cnt = 0
print(sum(a[x]for x in a if not any(y-x in a and(y!=x*2or a[x]>1)for y in p)))

