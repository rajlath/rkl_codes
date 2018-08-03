n, k = [int(x) for x in input().split()]
problems = [int(x) for x in input().split()]
probs = problems[:]
for i in range(2):
    while len(probs) > 0:
        if probs[-1] <= k:
            probs.pop()
        else:break
    probs = probs[::-1]
print(n - len(probs))
