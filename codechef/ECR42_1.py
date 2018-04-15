nd = int(input())
days= [int(x) for x in input().split()]
sd  = sum(days)
tillnow=0
tillall=sd
for i in range(nd):
    tillnow += days[i]
    tillall -= days[i]
    if tillnow >= tillall:
        print(i+1)
        break
