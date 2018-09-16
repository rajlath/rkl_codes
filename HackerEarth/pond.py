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
    #heapq.heapify(sizes)
    min_eat = min(eater)
    min_size= min(sizes)
    ans = 0
    for i, v  in enumerate(eater):
        ans += v < min_size and sizes[i] >= min_eat
    print(ans)