nb_elements = int(input())
elems = [int(x) for x in input().split()]
sums  = sum(elems)
maxs  = max(elems)
if not sums & 1 and (maxs <= (sums - maxs)):
    print("YES")
else:
    print("NO")