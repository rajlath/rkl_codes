'''
def merge(arr, left, rite):
    i, j, count = 0, 0, 0
    while i < len(left) or j < len(rite):
        if i == len(left):
            arr[i+j] = rite[j]
            j += 1
        elif j == len(rite)    :
            arr[i+j] = left[i]
            i += 1
        else:
            arr[i+j] = rite[j]
            count += len(left) - i
            j += 1
    return count

def ivc(arr):
    if len(arr) >= 2:
        mid =  len(arr) // 2
        left = arr[:mid]
        rite = arr[mid:]
        return (ivc(left) + ivc(rite) + merge(arr, left, rite))
    else:
        return 0

lens = int(input())
arr  = [int(x) for x in input().split()]
print(ivc(arr))
'''
# O(n log n)

def count_inversion(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count

noe = int(raw_input())
arr = [int(x) for x in raw_input().split()]
print(count_inversion(arr))

'''
#test code
input_array_1 = []  #0
input_array_2 = [1] #0
input_array_3 = [1, 5]  #0
input_array_4 = [4, 1] #1
input_array_5 = [2,3,1,5,4] #3
input_array_6 = [4, 1, 3, 2, 9, 5]  #5
input_array_7 = [4, 1, 3, 2, 9, 1]  #8

print count_inversion(input_array_1)
print count_inversion(input_array_2)
print count_inversion(input_array_3)
print count_inversion(input_array_4)
print count_inversion(input_array_5)
print count_inversion(input_array_6)
print count_inversion(input_array_7)
'''