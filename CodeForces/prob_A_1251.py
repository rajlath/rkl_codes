for _ in range(int(input())):
    curr = input()
    if len(curr) == 1:
        print(curr)
    else:
        valid=''
        broken=''
        for i in range(1, len(curr)):
            if curr[i] == curr[i-1]:
                if curr[i] not in broken:
                    broken += curr[i]
            else:
                if curr[i] not in broken:
                    valid+=curr[i]
        print(sorted(valid))
