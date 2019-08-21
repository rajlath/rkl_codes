for _ in range(int(input())):
    lens = int(input())
    size = sorted([int(x) for x in input().split()], reverse = True)
    base = size[:2]
    ladders = [x for x in size[2:] if x > 0]
    if len(ladders) < min(base):
        print(len(ladders))
    elif len(ladders) >= min(base):
            print(min(base) - 1)
    else:
        print(0)
