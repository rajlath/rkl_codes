from math import gcd
def gcd_arr(arr):
    gcd_ = 1
    for i in arr:
        gcd_ = gcd(gcd_, i)
    return gcd_

def runnersMeetings(startPosition, speed):
    print(gcd_arr(speed))

runnersMeetings([1, 4, 2], [27, 18, 24])
