for _ in range(int(input())):
    s = input()
    if len(s)<1:print(0)
    else:
        group = 1
        i = 1
        while i < len(s):
            j = i
            curr_cnt = 0
            while s[j] > s[j-1] and j < len(s):
                curr_cnt += 1
                j += 1
            group += 1
            i = j - curr_cnt%2
    print(group)







