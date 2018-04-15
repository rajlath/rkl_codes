'''
6
2 3
10 8
9 2
3 1
6 3
12 4
6
e 1
d 10
e 4e 4
d 12
e 3
e 2
Sample Output 0

10
6
IMPOSSIBLE
DROWNED
'''

from collections import defaultdict
no_of_isles = int(input())
islands = defaultdict(list)
loca    = {}
for i in range(no_of_isles):
    name, height = [int(x) for x in input().split()]
    islands[i+1] = [name, height]
    loca[name] = i+1
print(loca)

for _ in range(int(input())):
    a, b = [x for x in input().split()]
    if a == 'e':
        isle = islands[int(b)]
        height   = isle[1]
        location = isle[0]
        print(height, location)
        if height == 0:
            print("DROWNED")
        else:
            has = False
            for key, value in islands.items():
                #print(value[0], value[1])
                if value[1]>height:
                    print(islands[key][0])
                    has = True
                    break
            if not has:print("IMPOSSIBLE")
    else:
        indx = loca[int(b)]
        islands[indx][1] = 0

        print(islands)










