n, k = [int(x) for x in input().split()]
guest= input()
guest_cnt = {}
for i in guest:
    guest_cnt = get(guest_cnt, 0)+1

doors= {}
ans  = "NO"
for i in guest:
    guest_cnt[i]-=1
    if guest_cnt[i]==0:
        gaurd += 1
    else:




