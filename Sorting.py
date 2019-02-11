from random import randint
import operator

def generate_list(nb_elements, lower, upper, unsigned=False):
    rets = []
    if unsigned:
        lower = -1 * lower

    for i in range(nb_elements):
        rets.append(randint(lower, upper))
    return rets

sample_list_1 = generate_list(10, 100, 100, True)
sample_list_2 = generate_list(10, 100, 10000)

def bubble_sort(arr):
    lens = len(arr)
    for i in range(lens):
        changed = False
        for j in range(lens-1):
            if arr[j] > arr[j+1]:
                changed = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not changed:break
    return arr

def quick_sort(arr):
    less   = []
    equal  = []
    more   = []
    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if   x < pivot:less.append(x)
            elif x == pivot:equal.append(x)
            else: more.append(x)
        return quick_sort(less) + equal + quick_sort(more)
    return arr

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        min_value = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < min_value:
                min_index = j
                min_value = arr[j]
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

def merge(left, rite, compare)    :
    result = []
    i, j   = 0, 0
    while i < len(left) and j < len(rite):
        if compare(left[i], rite[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(rite[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(rite):
        result.append(rite[j])
        j += 1
    return result


def merge_sort(arr, compare=operator.lt):
    if len(arr) < 2: return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle], compare)
        rite = merge_sort(arr[middle:], compare)
        return merge(left, rite, compare)

def heapify(arr, n, i):
    largest = i
    left    = 2 * i + 1
    right   = 2 * i + 2
    if left < n and arr[i] < arr[left]:largest = left
    if right< n and arr[largest] < arr[right]:largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


print("List : signed integer:", end= " ")
print(sample_list_1)
print("Bubble sorted 1      :", end = " ")
print(bubble_sort(sample_list_1))
print("Quick sorted  1      :", end = " ")
print(quick_sort(sample_list_1))
print("Selection sorted  1  :", end = " ")
print(selection_sort(sample_list_1))
print("Insertion sorted  1  :", end = " ")
print(insertion_sort(sample_list_1))
print("Merge sorted  1      :", end = " ")
print(merge_sort(sample_list_1))
print("heap  sorted  1      :", end = " ")
print(heap_sort(sample_list_1))

print("List : unsigned Integer:", end = " ")
print(sample_list_2)
print("Bubble sorted 2        :", end = " ")
print(bubble_sort(sample_list_2))
print("Quick sorted 2         :",  end = " ")
print(quick_sort(sample_list_2))
print("Selection sorted       :", end = " ")
print(selection_sort(sample_list_2))
print("Insertion sorted       :", end = " ")
print(insertion_sort(sample_list_2))
print("Merge sorted           :", end = " ")
print(merge_sort(sample_list_2))
print("Heap  sorted           :", end = " ")
print(heap_sort(sample_list_2))

'''
List : signed integer: [30, -99, -21, 70, 79, -14, 10, 98, 17, 23]
Bubble sorted 1      : [-99, -21, -14, 10, 17, 23, 30, 70, 79, 98]
Quick sorted  1      : [-99, -21, -14, 10, 17, 23, 30, 70, 79, 98]
Selection sorted  1  : [-99, -21, -14, 10, 17, 23, 30, 70, 79, 98]
Insertion sorted  1  : [-99, -21, -14, 10, 17, 23, 30, 70, 79, 98]
Merge sorted  1      : [-99, -21, -14, 10, 17, 23, 30, 70, 79, 98]
heap  sorted  1      : [-99, -21, -14, 10, 17, 23, 30, 70, 79, 98]
List : unsigned Integer: [2183, 9533, 6504, 4080, 7279, 6024, 8249, 4373, 2329, 323]
Bubble sorted 2        : [323, 2183, 2329, 4080, 4373, 6024, 6504, 7279, 8249, 9533]
Quick sorted 2         : [323, 2183, 2329, 4080, 4373, 6024, 6504, 7279, 8249, 9533]
Selection sorted       : [323, 2183, 2329, 4080, 4373, 6024, 6504, 7279, 8249, 9533]
Insertion sorted       : [323, 2183, 2329, 4080, 4373, 6024, 6504, 7279, 8249, 9533]
Merge sorted           : [323, 2183, 2329, 4080, 4373, 6024, 6504, 7279, 8249, 9533]
Heap  sorted           : [323, 2183, 2329, 4080, 4373, 6024, 6504, 7279, 8249, 9533]
'''





