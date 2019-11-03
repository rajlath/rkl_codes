lens = int(input())
vals = [int(x) for x in input().split()]
max_subs = []
curr = []
for i in vals:
    if i > 0:
        curr.append(i)
    else:
        max_subs.append(curr)
        curr = []
max_subs.append(curr)

max_sub_sum = -10**18
answer = []
for i, v  in enumerate(max_subs):
    curr_sum = sum(v)
    if curr_sum >= max_sub_sum:
        max_sub_sum = curr_sum
        answer.append(v)
if len(answer) > 1:
    answer = sorted(answer, key=len, reverse=True)
#print(answer)
print(*answer[0])





