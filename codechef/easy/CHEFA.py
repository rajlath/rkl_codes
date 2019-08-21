for _ in range(int(input())):
    lens = int(input())
    elem = sorted([int(x) for x in input().split()])
    answer = 0
    while elem:
        answer += elem.pop()
        if not elem:break
        elem.pop()
    print(answer)