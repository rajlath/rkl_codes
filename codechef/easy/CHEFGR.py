for _ in range(int(input())):
    lens, has = [int(x) for x in input().split()]
    heights = [int(x) for x in input().split()]
    sums = sum(heights) + has
    if sums % lens == 0:
        hts = sums // lens
        d = 0
        if max(heights) > hts: d = 1
        print(["No", "Yes"][d == 0])
    else:
        print("No")
