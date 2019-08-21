import datetime
def checkYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

def dayOfWeek(birthdayDate):
    month, day,year = [int(x) for x in birthdayDate.split("-")]
    isLeap = day == 29 and month == 2
    #print(day, month, year, isLeap)
    wday = datetime.date(year, month, day).weekday()
    count = 0
    i = 0
    while i < 100:
        if isLeap:
            year += 4
            count += 4
            while not checkYear(year):
                year += 4
                count += 4
        else:
            year += 1
            count += 1
        print(year, month, day)
        if  datetime.datetime(year, month, day).weekday()==wday:
            break

    return count
print(dayOfWeek("02-29-2072"))
