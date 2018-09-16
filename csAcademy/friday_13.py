days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
curr_day_indx  = week_days.index(input())
#print(curr_day_indx)
ans = 0
for i in range(12):
    days_in_month = days[i]
    for j in range(1, days_in_month+1):
        #if i == 10 and j == 12:print(curr_day_indx)
        #print(curr_day_indx, i, j)
        if curr_day_indx == 4 and j == 13:
            ans += 1
            #print(i, j, curr_day_indx)
        curr_day_indx = (curr_day_indx+1)%7

print(ans)





