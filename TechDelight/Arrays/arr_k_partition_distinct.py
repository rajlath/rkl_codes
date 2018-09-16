#Find count of distinct elements in every sub-array of fixed size k

def find_partition(arr, k):
    i = 0
    dists = []
    while i <= len(arr) - k:
        curr = arr[i:i+k]
        done = []
        distinct = 0
        for x in curr:
            if x not in done:
                done.append(x)
                distinct += 1
        dists.append(distinct)
        i += 1
    print(*dists)

arr =  [2,1,2,3,2,1,4,5]
k   =  5
find_partition(arr, k)

