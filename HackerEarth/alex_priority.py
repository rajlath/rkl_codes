import bisect
priority = []
times    = []
priority_times = {}

for i in range(int(input())):
    ops = input().split()    
    if ops[0] == "1":
        prior = int(ops[2])
        time  = int(ops[1])
        priority_times[time] = prior
        
        bisect.insort(priority, prior)
        bisect.insort(times, time)        
    if ops[0] == "2":
        time = int(ops[1])
        prior= priority_times[time]
        
        del priority_times[time] 
        priority.remove(prior) 
        times.remove(time) 
    if ops[0] == "3":
        print(min(priority), max(priority)) 
    if ops[0] == "4":
        print(priority_times[max(times)])        



     
