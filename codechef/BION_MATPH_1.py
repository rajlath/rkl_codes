import bisect
nos = int(pow(10**11, 0.5))+1
primes = [True]*nos
primes[0] = primes[1] = False
pr = []
for ind, val in enumerate(primes):
    if val:
        pr.append(ind)
        for i in range(ind, nos, ind):
            primes[i] = False
print(len(pr))
exp = []
for i in range(len(pr)):
    for j in range(len(pr)):
        temp = pr[i]**pr[j]
        if temp<=10**11:
            exp.append(temp)
        else: break
print(exp[10])
exp.sort()
for _ in range(int(input())):
    no = int(input())
    if no<4: print(-1)
    elif no<8:print(4)
    else:
        pos = bisect.bisect(exp, no)
        if pos==len(exp):
            print(exp[pos-1])
        elif exp[pos]==no:
            print(exp[pos])
        else:
            print(exp[pos-1])