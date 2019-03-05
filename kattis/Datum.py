import datetime
D, M = [int(x) for x in input().split()]
dates = datetime.datetime(2009, M, D)
print(dates.strftime('%A'))
