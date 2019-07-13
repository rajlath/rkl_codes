from collections import defaultdict
lens, needed = [int(x) for x in input().split()]
elements = [int(x) for x in input().split()]
sum_count = defaultdict(int)
curr_sum  = 0
found = 0
for i, v in enumerate(elements):
    curr_sum += v
    if curr_sum  == needed:
        found += 1
    if curr_sum - needed in sum_count:
        found += sum_count[curr_sum - needed]
    sum_count[curr_sum] += 1
print(found)

