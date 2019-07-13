'''
1094. Car Pooling

Difficulty: Medium
You are driving a vehicle that has capacity empty seats initially available for passengers.
The vehicle only drives east (ie. it cannot turn around and drive west.)
Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information
about the i-th trip: the number of passengers that must be picked up,
and the locations to pick them up and drop them off.
The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
'''
class Solution:
    def carPooling(self, trips, capacity):
        trips = sorted(trips, key=lambda x: x[1])
        print(trips)
        car_pool = [0] * 1001
        on_board = 0
        for i in trips:
            car_pool[i[1]] += i[0]
            car_pool[i[2]] -= i[0]
            on_board += car_pool[i[1]]
            print(on_board, car_pool[:10])
            if on_board > capacity:return False
        return True

        '''


        #print(car_pool[:10])
        return True
        '''

print(Solution().carPooling([[5,4,7],[7,4,8],[4,1,8]],17))
