
for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    if k == 1:
        ans = [1]
    elif k > n // 2:
        ans = [-1]
    else:
        ans = []
        i = 1
        for i in range(1, k + 1):
            ans.append(i * 2)
            i += 1
    print(* ans)
