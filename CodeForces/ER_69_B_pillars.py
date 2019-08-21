nb_pillars = int(input())
wheels = [int(s) for s in input().split()]
maxi = wheels.index(max(wheels))
could_be = True
for i in range(maxi):
    could_be &= wheels[i] < wheels[i + 1]
for i in range(maxi, nb_pillars - 1):
    could_be &= wheels[i] > wheels[i + 1]
print(["NO", "YES"][could_be])
