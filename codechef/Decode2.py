def create_series():
    series = ["19"]
    lens   = 20
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
    return series

t = int(input())
g = create_series()
for _ in range(t):
    x = int(input())
    print(g[x-1])
