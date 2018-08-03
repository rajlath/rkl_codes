'''
###Sample Input 1:
8
GAAATAAA

###Sample Output 1:
5
'''

n = int(input())
s = input()
A = []
for c in s:
    A.append("ACTG".find(c))
count = [0]* 4
for x in A:
    count[x] += 1

each = n // 4
ans = n
if all(x <= each for x in count): print(0)
else:
    j = 0
    ans = n
    for i, x in enumerate(s):
         while j < len(s) and any(x > each for x in count):
             count[A[j]] -= 1
             j += 1
         if all(x <= each for x in count):
             ans = min(ans, j - i)
         count[A[i]] += 1
    print(ans)

