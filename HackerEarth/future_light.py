'''
2
1
2 3
4
5 6 7 8 9
'''


for _ in range(int(input())):
    time_till_now = 0
    nos_signal = int(input())
    time_needed = [int(x) for x in input().split()]
    for i,v  in enumerate(time_needed[:-1]):
        time_till_now += v
        if time_till_now % 2 == 0 :
            time_till_now += 1
    time_till_now += time_needed[-1]
    print(time_till_now)


