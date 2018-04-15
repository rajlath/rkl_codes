'''
Input 1:

4
11
27
27
11
Output 1:

YES
11 27

nput 3:

6
10
20
30
20
10
20
Output 3:

NO
'''
noe = int(input())
arr = []
for i in range(noe):
    arr.append(int(input()))
arr = set(arr)
arr = sorted(arr)
if len(arr) % 2 == 1 :
    print("NO")
else:
    print("YES")
    print(*arr)



