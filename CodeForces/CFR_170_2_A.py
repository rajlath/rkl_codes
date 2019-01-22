nb_elems = [int(x) for x in input().split()]
elems    = [int(x) for x in input().split()]
src, tgt = [int(x) for x in input().split()]
mins = min(src, tgt)
maxs = max(src, tgt)

sums = sum(elems)
clockwise = sum(elems[mins-1:maxs-1])
aclocwise = sums - clockwise
print(min(clockwise, aclocwise))
