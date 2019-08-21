'''
Helper h = new Helper();

    int partTime = h.getSeconds(part);
    int totalTime = h.getSeconds(total);
    int divisor = h.gcd(partTime, totalTime);
    return new int[]{partTime / divisor, totalTime / divisor};
'''
from math import gcd
def videoPart(part, total):
    def timeToSeconds(s):
        ftr = [3600,60,1]
        return sum([a*b for a,b in zip(ftr, map(int,s.split(':')))])
    part_time = timeToSeconds(part)
    total_time= timeToSeconds(total)
    divisor = gcd(part_time, total_time)
    return (part_time // divisor, total_time // divisor)

print(videoPart("02:20:00" ,"07:00:00"))
