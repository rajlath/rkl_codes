# thanks to varunvora
for _ in range(int(input())):
    pattern = input().strip()
    lens = len(pattern)
    arrs = [i for i  in range(1, lens + 2)]
    curr = 1
    while curr <= lens:
        last = curr
        while curr <= lens and pattern[curr - 1] == "-":
            curr += 1
        arrs[last - 1: curr] = arrs[last - 1:curr][::-1]
        curr += 1
    print(*arrs)
