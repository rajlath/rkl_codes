'''
def max_sum_from_mid(arr, left, mid, rite):
    sums = 0
    left_sum = int(-1e18)
    for i in range(mid, left - 1, -1):
        sums += arr[i]
        left_sum = max(sums, left_sum)
    sums = 0
    rite_sum = int(-1e18)
    for i in range(mid + 1, rite + 1):
        sums += arr[i]
        rite_sum = max(rite_sum, sums)
    return rite_sum + left_sum

def max_sub_array_sum(arr, left, rite):
    if left == rite: return arr[left]
    mid = (left + rite    ) // 2
    return max(max_sub_array_sum(arr, left, mid),
               max_sub_array_sum(arr, mid+1, rite),
               max_sum_from_mid(arr, left, mid, rite) )

'''

lens = int(input())
elem = [int(x) for x in input().split()]
#print( max_sub_array_sum(elem, 0, lens - 1))
max_ending, max_current = elem[0], elem[0]
for i in elem[1:]:
    max_ending = max(i, max_ending + i)
    max_current= max(max_ending, max_current)
print(max_current)





