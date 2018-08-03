noi, k = [int(x) for x in input().split()]
seq =  sorted([int(x) for x in input().split()])
if k > 0 :
    if k < noi and seq[k-1] == seq[k]:
        print(-1)
    else:
        print(seq[k-1])
else:
    x = seq[0] - 1
    print(x if x>0 else -1)