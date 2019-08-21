from collections import defaultdict
from statistics import mean
def meanGroups(a):
    groups = defaultdict(list)
    def get_mean(arr):
        return sum(arr) // len(arr)
    for i, v in enumerate(a):
        curr = mean(v)
        groups[curr].append(i)
    print(groups)
    return sorted(groups.values())
a = [[-1,0,0,0,0],[-1,1], [1], [1,1,1,0,1], [-1,-1,1,0], [1,-1], [0,0], [0,-1,1,0], [1,-1,1,1,0,-1,1]]
print(meanGroups(a))

#[[0,4],  [1],  [2,3]]
'''
a: [[-1,0,0,0,0],
 [-1,1],
 [1],
 [1,1,1,0,1],
 [-1,-1,1,0],
 [1,-1],
 [0,0],
 [0,-1,1,0],
 [1,-1,1,1,0,-1,1]]
Output:
[[0],
 [1,3,4,5,6,7,8],
 [2]]
Expected Output:
[[0],
 [1,5,6,7],
 [2],
 [3],
 [4],
 [8]]
Console Output:
'''
