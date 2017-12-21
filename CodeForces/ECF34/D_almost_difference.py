'''
You are given an array a consisting of n integers.
You have to calculate the sum of d(ai, aj) over all pairs (i, j) such that 1 ≤ i ≤ j ≤ n.
function d here return j - i if abs(i - j) > 1 else 0
input
5
1 2 3 1 3
output
4
input
4
6 6 5 5
output
0
input
4
6 6 4 4
output
-8
'''
n = int(input())
cnt = dict()
s = 0
ans = 0
a = list(map(int, input().split()))
for i in range(0, n):
	ans += a[i] * i - s;
	ans -= cnt.get(a[i] - 1, 0)
	ans += cnt.get(a[i] + 1, 0)
	s += a[i]
	cnt[a[i]] = cnt.get(a[i], 0) + 1
print(ans)