noe, cost = [int(x) for x in input().split()]
arrs = [int(x) for x in input().split()]
valids = 0
cuts   = []
for i, v in enumerate(arrs[:-1]):
    if v%2:valids += 1
    else:valids -= 1
    if valids == 0:
        cuts.append(abs(arrs[i] - arrs[i+1]))
cuts = sorted(cuts)
done = 0
while done<len(cuts) and cost>=cuts[done]:
    cost-=cuts[done]
    done+=1
print(done)



