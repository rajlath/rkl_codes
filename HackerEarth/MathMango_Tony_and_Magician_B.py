s = list(range(1, 11))
N = 7

Thanos= sum(s)

Tony = 0
for i in range(len(s)):
    Tony += (pow(s[i], N) + s[i] - N)
print(Tony%Thanos)





