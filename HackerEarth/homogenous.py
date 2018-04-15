from collections import defaultdict
swaps = defaultdict(list)
for _ in range(int(input())):
    s = set([x for x in input().strip()])
    ans = "YES"
    swaps={}
    for _ in range(int(input())):
       arr = [x for x in input().strip().split()]
       swaps[arr[0]] = arr[1]
    for i in s:
            if i in swaps and swaps[i] in swaps :
                continue
            else:
                ans = "NO"
                break

    print(ans)



