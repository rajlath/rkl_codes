from math import ceil, floor
km, normal, diffs = [int(x) for x in input().split()]
max_days = ceil(km / normal)
diff_dict = {}
for _ in range(diffs):
    day, kmd = [int(x) for x in input().split()]
    diff_dict[day] = kmd
#diff_dict = sorted(diff_dict.items())
#print(diff_dict)
km_done = 0
days_done= 0
for i in range(1, max_days+1):
    if i in diff_dict:
        km_done += diff_dict[i]
    else:
        km_done += normal
    if km_done >= km:
        break
    #print(i, km_done)
print(i)

