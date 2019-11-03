class Solution:
    def minAvailableduration(self, slots1, slots2, duration):
        slots1 = sorted(slots1)
        slots2 = sorted(slots2)
        for x in slots1:
            for y in slots2:
                if x[0] == y[0]:
                    if x[0] + duration <= y[1]:
                        return (x[0], x[0] + duration)
                elif x[0] > y[0]:
                    if x[0] + duration <= y[1]:
                        return (x[0], x[0] + duration)
                else:
                    if y[0] + duration  < x[1]:
                        return (y[0], y[0] + duration)
        return []

print(Solution ().minAvailableduration([[10,50],[60,120],[140,210]],[[0,15],[60,70]], 8))
