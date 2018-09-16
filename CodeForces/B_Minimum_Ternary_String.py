'''
B. Minimum Ternary String

Output
Print a single string — the minimum possible (lexicographically) string you can obtain by using the swaps
described above arbitrary number of times (possibly, zero).

Examples
input
100210
output
001120
input
11222121
output
11112222
input
20
output
20
'''
s = input()
s = s + "2"
t = s.replace("1", '')
i = t.find("2")
print(t[:i] + "1"*s.count("1")+t[i:-1])



