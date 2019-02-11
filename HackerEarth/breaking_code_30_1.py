N, M = [int(x) for x in input().split()]
cookies = [int(x) for x in input().split()]
done = [0] * N
for i in cookies:
    done[i-1] += 1
    valid = True
    for j in done:
        if j == 0:
            print("0", end="")
            valid = False
            break
    if valid:
        print("1", end="")
        done = [x-1 for x in done]
        

