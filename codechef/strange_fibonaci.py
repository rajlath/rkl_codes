'''
Input:
2
0 1 2
7 12 23
Output:
4
93500136
'''
mods = int(10e9) + 7
for _ in range(int(input())):
    a, b, n = [int(x) for x in input().split()]
    for i in range(2, n-1):
        a, b = b, ((5*a) + (4*b))%mods
    print(b%mods, a%mods)

'''
MOD = int(1e9) + 7
mul = [[0, 1], [1, 0]]
ed, od = 4, 20
for i in range(2, 1000001):
	if i & 1:
		mul.append([(mul[i - 2][0] + od) % MOD, (mul[i - 2][1] + od) % MOD])
		od *= 25; od %= MOD
	else:
		mul.append([(mul[i - 2][0] + ed) % MOD, (mul[i - 2][1] + ed) % MOD])
		ed *= 25; ed %= MOD
t = int(input().strip())
while t:
	f0, f1, n = map(int, input().strip().split()); t -= 1
	print(((mul[n][0] * f1) % MOD + (mul[n][1] * f0) % MOD) % MOD)
'''



