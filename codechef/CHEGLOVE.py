'''
Input
4
3
1 2 3
2 3 4
3
1 2 1
1 2 1
3
3 2 1
1 2 3
4
1 3 2 4
1 2 3 5

Output
front
both
back
none
'''
for _ in range(int(input())):
    noe = int(input())
    finger = [int(x) for x in input().split()]
    sheath = [int(x) for x in input().split()]
    ans = 'none'
    if all((b >= a) for a, b in zip(finger, sheath)):ans = 'front'
    if all((b >= a) for a, b in zip(finger, sheath[::-1])):
        if ans == 'front':
            ans = 'both'
        else:
            ans = 'back'
    print(ans)



