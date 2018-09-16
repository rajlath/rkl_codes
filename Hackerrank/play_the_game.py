def create_series(n):
    series = ["1"]
    lens   = n
    while lens > 0:
        cur = series[-1]
        l   = len(cur)
        i   = 0
        cnt = 1
        temp=""
        while i < l:
            while i+1 < l and cur[i+1] == cur[i]:
                i += 1
                cnt += 1
            temp += str(cnt)
            temp += cur[i]
            i += 1
            cnt = 1
        series.append(temp)
        lens -= 1
    #print(series)
    return series[n]

n = int(input())
ans = create_series(n-1)
print(ans)
