for _ in range(int(input())):
    lens = int(input())
    bldg = list(input())
    count = 0
    for i in range(lens):
        if bldg[i] == "1":
            if i > 0 and bldg[i - 1] == "0":
                count += 1
                bldg[i - 1] == "2"
            if i < lens-1 and bldg[i + 1] == "0":
                count += 1
                bldg[i + 1] = "2"
            bldg[i] = "2"
            count += 1
    print(lens - count)
