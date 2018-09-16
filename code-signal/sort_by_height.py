def sortByHeight(a):
    asr = sorted([x for x in a if x != -1])[::-1]
    ans = []
    for i in range(len(a)):
        if a[i] == -1:
            ans.append(-1)
        else:
            ans.append(asr.pop())
    return ans

print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))