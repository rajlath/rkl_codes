for _ in range(int(input())):
    lens = int(input())
    score = [int(x) for x in input().split()]
    fowl  = [int(x) for x in input().split()]
    points = [(x*20 - y*10) for x, y in zip(score, fowl)]
    points = [x if x > 0 else 0 for x in points]
    print(max(points))
