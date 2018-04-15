'''
2
3 3
2 1 2
2 1 2
3 3
3 1 3
3 1 3
'''

for i in range(int(input())):
    n, m = [int(x) for x in input().split()]

    blacks = [int(x) for x in input().split()]
    whites = [int(x) for x in input().split()]
    full_row = 0
    nill_row = 0
    ans = "YES"
    if sum(blacks)  != sum(whites):
        ans = "NO"

    else:
        for i in blacks:
            if i == m: full_row += 1
            elif i == 0: nill_row += 1
        for i in whites:
            if i < full_row:
                ans = "NO"
                break
            if i > (n - nill_row):
                ans = "NO"
                break
    print(ans)

