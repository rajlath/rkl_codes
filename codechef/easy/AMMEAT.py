
for _ in range(int(input())):
    _, need = [int(x) for x in input().split()]
    meatball= sorted([int(x) for x in input().split()])
    if sum(meatball ) < need:
        print(-1)
    else:
        count = 0
        while need > 0:
            need -= meatball.pop()
            count += 1
        print(count)

