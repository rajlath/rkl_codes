days  =  [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days1 =  [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = [int(x) for x in days]
no_elem = int(input())
have_days = [int(x) for x in input().split()]
ans = "NO"
if have_days.count(29)>2:
    ans = "NO"
else:
    for i, v in enumerate(have_days):
        if v in [28, 29]:
            have_days[i] = 0
    if have_days.count(0)>=2 and len(have_days)< 12:
        ans = "NO"
    for i in range(24-len(have_days)):
        curr = days1[i:i+len(have_days)]
        #print(have_days, curr)
        if curr == have_days:
            ans = "YES"
            break
print(ans)









