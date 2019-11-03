import datetime
import calendar
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        ds = " ".join([str(day),str(month), str(year)])
        onDate = datetime.datetime.strptime(ds, '%d %m %Y').weekday()
        return (calendar.day_name[onDate])

print(Solution().dayOfTheWeek(15,8,1993))