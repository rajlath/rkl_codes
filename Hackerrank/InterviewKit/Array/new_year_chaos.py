'''
Sample Input

2
5
2 1 5 3 4
5
2 5 1 3 4
Sample Output

3
Too chaotic
'''
#Solution 1
'''
for _ in range(int(input())):
    noe = int(input())
    que = [int(x) for x in input().split()]
    ans = 0
    for i in range(noe-1, -1, -1):
        if que[i] - (i + 1) > 2:
            ans = -1
            print("Too chaotic")
            break
        else:
            j = max(0, que[i] - 2)
            while j < i:
                if que[j] > que[i]:ans += 1
                j += 1
    if ans != -1:print(ans)
'''
for _ in range(int(input())):
    noe = int(input())
    que = [int(x) for x in input().split()]
    ans = 0
    for i, v in enumerate(que):
        if v -1 - i > 2:
            print("Too chaotic")
            ans = -1
            break
    if ans != -1:
        for i in range(noe - 1):
            for j in range(noe - 1):
                if que[j] > que[j+1]:
                    que[j], que[j+1] = que[j+1], que[j]
                    ans += 1
                    swapped = True
            if swapped : swapped = False
            else:break
    if ans != -1 : print(ans)



