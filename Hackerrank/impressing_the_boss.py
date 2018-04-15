'''
2
8
5 7 7 11 15 12 22 24
9
20 19 18 16 14 15 14 13 11
'''
for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    last_high = 0
    done_once = False
    invalid = False
    for i in range(0,noe-1,2):
        if arr[i]>= last_high:
            if arr[i+1] > arr[i]:
                last_high = arr[i+1]
            else:
                if done_once:
                    invalid = True
                    break
                else:
                    done_once=True
                    last_high = arr[i+1]
        else:
            if done_once:
                invalid = True
                break
            else:
                done_once = True
                last_high = arr[i+1]
    if not invalid:
        if noe % 2 == 1:
            if arr[-1] < last_high:
                if done_once:
                    invalid = True
    print("NO" if  invalid else "YES" )














