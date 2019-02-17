from collections import defaultdict
N, M = [int(x) for x in input().split()]
boxes = defaultdict(list)
for i in range(N):
    val, nb = [int(x) for x in input().split()]
    boxes[nb].append(val)
values = [max(x) for x in boxes.values()]
values = sorted(values, reverse=True)
if len(values) <= M:
    print(sum(values))
else:
    print(sum(values[:M]))
