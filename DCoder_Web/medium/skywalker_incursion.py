'''
def get_nearest_lucas(n):
    a = 2
    b = 1
    if n == 0:return a
    while True:
        if a < n < b:
            if n - a < b - n:
                return a
            else:
                return b
        a, b = b, a + b
'''
def build_lucas_seq(n):
    seq = [2, 1]
    while seq[-1] < n:
        seq.append(seq[-2] + seq[-1])
    return seq

s = build_lucas_seq(10 ** 8)
n = int(input())
for i in range(len(s)):
    if s[i] > n:
        print(s[i])
        break
