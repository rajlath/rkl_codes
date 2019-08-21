from datetime import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        adate = datetime.strptime(date,"%Y-%m-%d")
        day_of_year = adate.timetuple().tm_yday
        return day_of_year

print(Solution().dayOfYear("2003-03-01"))
