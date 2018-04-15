'''
5
1
5
2
3 4
3
4 5 6
4
1 2 3 4
5
1 2 3 4 5
'''
mods = 1000000007
for _ in range(int(input())):
    nos = int(input())
    arr = [int(x) for x in input().split()]
    stk = []
    if nos == 1:
        print(arr[0]%mods)
    else:
        ans = 0
        stk.append(arr[0])
        for i in arr[1:]:
            a = stk.pop()
            b = i
            print(a, b)
            ans = (((a + b)%mods + (a * b)%mods)%mods)
            stk.append(ans)
        print(stk)


