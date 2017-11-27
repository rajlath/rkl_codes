s = input()
max_till_now = 0
curr_max = 0
for i in s:
    if i in "aeiou":
        curr_max += 1
    else:
        max_till_now = max(max_till_now, curr_max)
        curr_max = 0
max_till_now = max(max_till_now, curr_max)
print(max_till_now)

