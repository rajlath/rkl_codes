for _ in range(int(input())):
    current = input()
    ways = 1
    pos = 0
    lens = len(current)
    while pos < lens // 2:
        left , right = current[pos], current[lens - pos - 1]
        if left == right and left == "?" and right == "?":
            ways = (ways * 26) % 10000009
        if left != right and left != "?" and right != "?":
            ways = 0
            break
        pos += 1
    if lens % 2 == 1 and current[lens // 2] == "?":
        ways *= 26
    print(ways)