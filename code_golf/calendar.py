import datetime
from string import ascii_uppercase as uc

for _ in range(int(input())):
    y, days = [int(x) for x in input().split()]
    wdays = uc[:days]
    print(wdays)
    ans = datetime.date(y, 1, 1)
    x   = ans.weekday()
    print(x)
    print(wdays[x%days-1])
