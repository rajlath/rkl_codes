class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        a, b = min(start, destination), max(start, destination)
        print(a, b)
        clock_distance = sum(distance[a:b])
        anti_clock_distance = 0
        n = len(distance)
        i = b
        while i != a:
            anti_clock_distance += distance[i]
            i = (i + 1) % n
        return min(clock_distance, anti_clock_distance)

print(Solution().distanceBetweenBusStops([1,2,3,4], 0, 3))