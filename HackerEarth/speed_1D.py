for i in range(int(input())):
    nos_cars = int(input())
    speeds  =[int(x) for x in input().split()]
    max_speed = speeds[0]
    cnt = 1
    for j in range(1, nos_cars):
        if speeds[j]<=max_speed:
            max_speed = speeds[j]
            cnt += 1
   
    print(cnt)            
