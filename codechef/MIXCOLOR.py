'''
Example
Input:
2
3
1 2 3
3
2 1 2

Output:
0
1
'''

for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    has = [arr[0]]
    cnt = 0
    for i in range(1, noe):
        if arr[i] in has:
            for x in arr[:i]:
                if arr[i]+x not in has:
                    cnt += 1
                    has.append(arr[i]+x)
                    break
    print(cnt)



