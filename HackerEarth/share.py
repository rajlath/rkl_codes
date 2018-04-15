'''
Sample Input 0

8
4 2 2 3 3 4 6 5
5
2
1
3
4
5
Sample Output 0

3
-1
5
6
8
'''
noe = int(input())
arr = [int(x) for x in input().split()]
days = {}
for i in range(noe):
    days[arr[i]] = i+1
for i in range(int(input())):
    try:
        print(days[int(input())])
    except KeyError:
        print(-1)

