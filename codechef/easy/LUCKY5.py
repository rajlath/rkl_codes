for _ in range(int(input())):
    current = input().strip()
    need  = sum([1 for x in current if x not in ["4", "7"]])
    print(need)
