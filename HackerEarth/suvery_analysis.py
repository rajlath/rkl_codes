import math
days = [0] * 7
avg  = []
weeksum = 0
for i in range(7):
    days[i] = input().count("1")
    weeksum += days[i]
avg = weeksum / 7
var = 0.0
for i in range(7):
    var += (avg - days[i]) * (avg - days[i])
mean_dev = math.sqrt(var / 7.0)
print("%.4f" % mean_dev)       
    
