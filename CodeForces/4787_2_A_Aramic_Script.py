'''
Examples
inputCopy
5
a aa aaa ab abb
outputCopy
2
inputCopy
3
amer arem mrea
outputCopy
1
'''
n = int(input())
ans = []
arr = [x for x in input().split()]
for a in arr:
    curr = sorted(set(a))
    if curr not in ans:
        ans.append(curr)
print(len(ans))


