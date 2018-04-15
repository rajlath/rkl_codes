arr = [1,2,3,4,5]
cnt = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i:j+1] != []:
            cnt += 1