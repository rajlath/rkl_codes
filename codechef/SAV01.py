import bisect
nb_query = int(input())
medians = []
arr = [input()]
print("{:.1f}".format(float(arr[0])))
for i in range(nb_query-1):
    bisect.insort(arr, input())
    lens = len(arr)
    if lens%2:
        curr =  float(arr[int((lens-1)/2)])
    else:
        curr = (float(arr[(lens - 1)//2]) + float(arr[lens//2]))/2
    print("{:.1f}".format(curr))




