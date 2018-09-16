'''
def bin_search(arr, n, x):
    l = 0
    h = n - 1
    while l <= h:
        mid = (l + h)//2
        if arr[mid] <= x:
            l = mid + 1
        else:
            h = mid - 1
    return h
import heapq
for _ in range(int(input())):
    nov = int(input())
    sizes = []
    eater = []
    ans = 0
    for i in range(nov):
        a, b = [int(x) for x in input().split()]
        sizes.append(a)
        eater.append(b)
    heapq.heapify(sizes)
    ans = 0
    for i in eater:
        ans += i < sizes[0]



    for i in eater:
        indx = bin_search(sizes, nov, i)
        if indx == -1:
            ans += 1

    print(ans)
    '''
from collections import defaultdict
for _ in range(int(input())):
    nof = int(input())
    eater= []
    sizes = []
    fish = defaultdict(list)
    for _ in range(nof):
        s, e = [int(x) for x in input().split()]
        sizes.append(s)
        fish[s].append(e)
    sets = set()
    #print(fish)
    mins = min(sizes)
    cnt = 0
    #print(mins)
    for i in fish.keys():
        print(i)
        for j in fish[i]:
            if j < mins:cnt += 1

    print(cnt)










