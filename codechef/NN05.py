def ways(n):
    way_indx = [1] + [0] * (n+1)

    for i in range(1, n):
        for j in range(i, n+1):
            way_indx[j]+= way_indx[j-i]
    return way_indx[n]

for i in range(int(input())):
    print(ways(int(input())))

