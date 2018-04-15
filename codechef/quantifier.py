def tribonnaci(x):
    trib = [0,0,1]
    n = 3
    while True:
        curr = trib[-3]+trib[-2]+trib[-1]
        if curr >x:
            break
        trib.append(curr)
    return trib


t = tribonnaci(1000)
n = int(input())
print([0, 1][n in t])



