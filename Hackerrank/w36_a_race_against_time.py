'''
4
5
2 6 2
2 3 2
'''
#!/bin/python3

import sys

def raceAgainstTime(n, mason_height, heights, prices):
    # Complete this function
    curr_height = mason_height
    time_cost   = 0
    for i in range(n-1):
        exchange_cost = prices[i] + abs(curr_height - heights[i])

        if heights[i] <= curr_height:
            if exchange_cost < 1:
                time_cost += exchange_cost
                curr_height = heights[i]
            else:
                time_cost += 1

        else:
            time_cost += exchange_cost
            curr_height = heights[i]
        print(time_cost, exchange_cost)
    return time_cost + 2

if __name__ == "__main__":
    n = int(input().strip())
    mason_height = int(input().strip())
    heights = list(map(int, input().strip().split(' ')))
    prices = list(map(int, input().strip().split(' ')))
    result = raceAgainstTime(n, mason_height, heights, prices)
    print(result)


