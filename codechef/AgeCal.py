from itertools import accumulate
for _ in range(int(input())):
    nb_months = int(input())
    days_month= [int(x) for x in input().split()]
    cumm_days = list(accumulate(days_month))
    birth_year, birth_month, birth_day = [int(x) for x in input().split()]
    now_year, now_month, now_day = [int(x) for x in input().split()]
    days_at_birth = (birth_year-1) *sum(days_month) + sum(days_month[:birth_month-1])  + birth_day + (birth_year - 1)// 4
    print(days_at_birth)
    days_at_now   = (now_year  -1) * sum(days_month) + sum(days_month[now_month-1])  + now_day   + (now_year-1)    // 4
    print(days_at_now)
    print(days_at_now - days_at_birth + 1)
