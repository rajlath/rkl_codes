a, b = [int(x) for x in input().split()]
seq  = [a, b]
while len(seq) < 101:
        a, b = b, a + b
        seq.append(b)
for _ in range(int(input())):
    print(["NO", "YES"][int(input()) in seq])