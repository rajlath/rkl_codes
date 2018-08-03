#create a random array
import random
unsorted_arr = list(range(-100,100))
random.shuffle(unsorted_arr)
sorted_arr   = list(range(-100, 100))

#binarySearch
to_search = random.choice(sorted_arr)
print(to_search)
left = 0
rite = len(sorted_arr)
found = False
while left < rite:
    mid = left + (rite - left)//2
    if sorted_arr[mid] == to_search:
        found = True
        break
    else:
        if sorted_arr[mid] < to_search:
            left = mid+1
        else:
            rite = mid-1
#print(found)

#rotate element by k position

arr1 = sorted_arr[:10]
#print(arr1)
k   = 4
arr2 = sorted_arr[:10] + sorted_arr[:10]
ans = arr2[k:k+len(arr2)//2]
#print(ans)

arr1 = arr = [1, -2, 3, 4, -4, 6, -4, 8, 2]
print(arr1)

max_ending_here = 0
max_all       = 0
for i in arr1:
    max_ending_here = max(max_ending_here, max_ending_here + i)
    if max_ending_here < 0:
        max_ending_here = 0
    max_all = max(max_all, max_ending_here)

print(max_all)
print(sum(arr1))









