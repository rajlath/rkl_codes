from  itertools import accumulate

lens = int(input())
arrs = [int(x) for x in input().split()]
arrss= sorted(arrs)
arrs = [0] + list(accumulate(arrs))
arrss= [0] + list(accumulate(arrss))
for _ in range(int(input())):
    o, l, r = [int(x) for x in input().split()]
    if o == 1:
        print(arrs[r] - arrs[l - 1])
    else:
        print(arrss[r] - arrss[l - 1])
