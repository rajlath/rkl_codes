for _ in range(int(input())):
    apples, boxes = [int(x) for x in input().split()]
    print(["YES", "NO"][apples % (boxes * boxes) == 0])
