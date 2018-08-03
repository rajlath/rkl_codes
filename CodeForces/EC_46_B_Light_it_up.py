n, m = [int(x) for x in input().split()]
a = [0] + [int(x) for x in input().split()]
prev = m
pos  = 0
neg  = 0
on   =  (n%2 == 0)
max_diff = 0
for i in range(n, -1, -1):
    adv = prev - a[i]
    if not on:
        diff = neg -  pos + adv -1
        max_diff = max(max_diff, diff)
        neg += adv
    else:
        pos += adv
    on = not on
    prev = a[i]
print(pos + max_diff)

