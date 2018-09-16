noe, k = [int(x) for x in input().split()]
problems = [(int(x), i) for i, x in enumerate(input().split())]
probss   = sorted(problems, key= lambda x:x[0], reverse=True)[:k]
print(sum(x[0] for x in probss))
indxs = sorted(i for v, i in probss)
indxs[-1] = noe - 1

print(*[y-x for x, y in zip([-1]+indxs, indxs)])

'''
maxs = sorted(problems, reverse= True)[:k][::-1]
print(sum(maxs))
last = -1
nexts= 0
maxs[-1]=noe-1
print(' '.join(str(y-x) for x,y in zip([-1]+maxs,maxs)))


for i, v in enumerate(problems):
    if problems[i] == maxs[nexts]:
        print(i-last, end=" ")
        nexts += 1
        k -= 1
        if k == 0: break
'''








