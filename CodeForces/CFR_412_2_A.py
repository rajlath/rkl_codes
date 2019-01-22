n = int(input())
a = [[int(x) for x in input().split()] for _ in range(n)]
if any([x-y for x, y in a]):
    print("rated")
else:
    a1 = sorted(a)
    a.reverse()
    if a == a1:
        print("maybe")
    else:
        print("unrated")